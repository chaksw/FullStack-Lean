from pathlib import Path
import json
from io import BytesIO
import openpyxl
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
import openpyxl.workbook
from .models import Score
from .forms import ScoreForm
from students.models import Student
from grades.models import Grade
from django.urls import reverse_lazy
from utils.handle_excel import ReadExcel, WriteExcel
# Create your views here.


# 使用 transaction.atomic() 确保如果某些操作失败，所有更改会被回滚。
@transaction.atomic
def upload_student_scores(file):
    read_excel = ReadExcel(file)
    read_excel.get_data()
    if read_excel.data[0] != ['考试名称', '班级', '姓名', '学号', '语文成绩', '数学成绩', '英语成绩']:
        return {'status': 'error', 'messages': 'Excel格式有误'}
    for row in read_excel.data[1:]:
        title, grade_name, student_name, student_number, chinese_score, math_score, english_score = row
        if len(student_name) < 2 or len(student_number) > 50:
            return {'status': 'error', 'messages': '学生姓名长度不能超过50'}
        if not student_name:
            return {'status': 'error', 'messages': '学生姓名不能为空'}
        if not student_number or len(student_number) != 19:
            return {'status': 'error', 'messages': '学籍号不能为空，并且长度应为19位'}
        # grade = Grade.objects.get(grade_name=grade_name)
        grade = Grade.objects.filter(grade_name=grade_name).first()
        if not grade:
            return {'status': 'error', 'messages': f'班级名称"{grade_name}"不存在'}

        # 判断学生信息是否已经存在
        try:
            student = Student.objects.get(
                student_name=student_name,
                student_number=student_number,
                grade=grade
            )
        except Student.DoesNotExist:
            return {'status': 'error', 'messages': '学生信息不存在'}

        # 创建成绩记录
        Score.objects.create(
            title=title,
            student_name=student_name,
            student_number=student_number,
            grade=grade,
            chinese_score=chinese_score,
            math_score=math_score,
            english_score=english_score
        )
    return {'status': 'success', 'messages': '文件上传成功'}


def upload_scores(request):
    if request.method == 'POST':
        try:
            file = request.FILES.get('excel_file')
            if not file:
                return JsonResponse({'status': 'error', 'messages': '请上传Excel文件'}, status=400)
            # 检查前缀
            ext = Path(file.name).suffix
            if ext.lower() != '.xlsx':
                return JsonResponse({'status': 'error', 'messages': '文件类型错误，请上传.xlsx格式的文件'}, status=400)

            result = upload_student_scores(file)
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({'status': 'error', 'messages': '上传失败' + str(e)}, status=500)
    return JsonResponse({'error': '无效的请求'}, status=400)


def export_scores(request):
    if request.method == 'POST':
        # 获取请求体
        data = json.loads(request.body)
        # 要到处的成绩信息的班级
        grade_id = data.get('grade')
        # 确认有被选择的班级
        if not grade_id:
            return JsonResponse({'status': 'error', 'messages': '班级参数缺失'}, status=400)
        try:
            grade = Grade.objects.get(id=grade_id)
        except Grade.DoesNotExist:
            return JsonResponse({'status': 'error', 'messages': '班级不存在'}, status=404)
        # 查询班级对应的成绩信息
        scores = Score.objects.filter(grade=grade)
        if not scores.exists():
            return JsonResponse({'status': 'error', 'messages': '找不到指定班级的成绩信息'}, status=404)
        # 使用 openpyxl 导出
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'Score'
        # 添加标题行
        columns = ['考试名称', '班级', '姓名', '学号', '语文成绩', '数学成绩', '英语成绩']
        ws.append(columns)

        for score in scores:
            row = [score.title, score.grade.grade_name, score.student_name,
                   score.student_number, score.chinese_score, score.math_score, score.english_score]
            ws.append(row)
        excel_file = BytesIO()
        wb.save(excel_file)
        excel_file.seek(0)
        # 设置响应
        response = HttpResponse(
            excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="students.xlsx"'
        return response


class ScoreBaseView():
    model = Score
    success_url = reverse_lazy('scores_list')


class ScoreListView(ScoreBaseView, ListView):
    template_name = "scores/scores_list.html"
    context_object_name = 'scores'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        grade_queryset = self.request.GET.get('grade')
        search_queryset = self.request.GET.get('search')
        if grade_queryset:
            queryset = queryset.filter(grade__pk=grade_queryset)
        if search_queryset:
            filter = Q(student_name__icontains=search_queryset) | Q(student_number__icontains=search_queryset)
            queryset = queryset.filter(filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ScoreListView, self).get_context_data(**kwargs)
        context['grades'] = Grade.objects.all().order_by('grade_number')
        context['current_grade'] = self.request.GET.get('grade', '')
        return context


class ScoreCreateView(ScoreBaseView, CreateView):
    form_class = ScoreForm
    template_name = "scores/score_form.html"

    def form_valid(self, form):
        student_name = form.cleaned_data.get('student_name')
        student_number = form.cleaned_data.get('student_number')
        grade_id = form.cleaned_data.get('grade')
        try:
            student = Student.objects.get(
                student_name=student_name,
                student_number=student_number,
                grade=grade_id
            )
        except Student.DoesNotExist:
            errors = {'general': [{
                'message': '学生信息不存在',
                'code': 'not_found'
            }]}
            response = {
                'status': 'error',
                'messages': errors
            }
            return JsonResponse(response, status=404)
        form.save()
        return JsonResponse({
            'status': 'success',
            'messages': '操作成功',
        })

    def form_invalid(self, form):
        # Convert form errors to a structured JSON format
        errors = {field: [{'message': error, 'code': ''} for error in errors_list]
                  for field, errors_list in form.errors.items()}
        return JsonResponse({'status': 'error', 'messages': errors}, status=400)


class ScoreUpdateView(ScoreBaseView, UpdateView):
    form_class = ScoreForm
    template_name = "scores/score_form.html"

    def form_valid(self, form):
        form.save()
        # 返回JSON响应
        return JsonResponse({
            'status': 'success',
            'messages': '操作成功',
        })

    def form_invalid(self, form):
        # Convert form errors to a structured JSON format
        errors = {field: [{'message': error, 'code': ''} for error in errors_list]
                  for field, errors_list in form.errors.items()}
        return JsonResponse({'status': 'error', 'messages': errors}, status=400)


class ScoreDeleteView(ScoreBaseView, DeleteView):
    template_name = "scores/scores_list.html"

    def delete(self, request, *args, **kwargs):
        # 检查是否为 AJAX 请求
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            response = super().delete(request, *args, **kwargs)
            if response.status_code == 302:  # 删除成功
                return JsonResponse({'status': 'success', 'messages': '学生成绩已删除'})
            else:
                return JsonResponse({'status': 'error', 'messages': '删除失败'}, status=400)
        else:
            return super().delete(request, *args, **kwargs)


class ScoreDeleteMultipleView(ScoreBaseView, DeleteView):
    template_name = "scores/scores_list.html"

    def post(self, request, *args, **kwargs):
        print("执行post操作")
        # 获取的是post请求的body中的score_ids的数据
        selected_ids = self.request.POST.getlist('score_ids')
        if not selected_ids:
            return JsonResponse({'status': 'error', 'messages': '请选择要删除的成绩'})
        print('获取选中的id')
        print(selected_ids)
        try:
            self.object_list = self.get_queryset().filter(id__in=selected_ids)
            self.object_list.delete()
        except Exception as e:
            print(e)
        # 判断是否为 AJAX 请求
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest' or self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success', 'messages': '成绩已删除'})
        else:
            return self.get_success_url()


class ScoreDetailView(DetailView):
    model = Score
    template_name = "scores/score_detail.html"


class MyScoreListView(ListView):
    model = Score
    template_name = "scores/my_score_list.html"
    context_object_name = 'scores'
    paginate_by = 10

    def get_queryset(self):
        # 仅返回当前用户的成绩
        student_number = self.request.user.student.student_number
        score = Score.objects.filter(student_number=student_number)
        return score
