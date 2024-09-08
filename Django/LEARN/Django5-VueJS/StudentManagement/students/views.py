from pathlib import Path
import datetime
import openpyxl
from io import BytesIO
import json
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse, JsonResponse
from .forms import StudentForm
from .models import Student
from grades.models import Grade
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from utils.handle_excel import ReadExcel, WriteExcel, ExportExcel

# Create your views here.


class StudentListView(ListView):
    model = Student
    template_name = 'students/students_list.html'
    # fields = []
    context_object_name = 'students'

    paginate_by = 10

    # 在原始context(student)的基础上，添加 grade 数据到上下文(context)
    def get_context_data(self):
        context = super().get_context_data()
        # 获取所有班级，并添加到上下文
        context['grades'] = Grade.objects.all().order_by('grade_number')
        # 尝试获取当前请求中被选中的班级信息，如果没有返回 ''
        context['current_grade'] = self.request.GET.get('grade', '')
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    # success_url = reverse_lazy('students_list')
    # 当 type='sumbit' 的按钮按下后，会提交表单，产生一个 post 请求，将表单数据发送到服务器
    # 服务器接收到数据后，CreateView 会调用 ModelForm 中的各种方法，包括 form.is_valid(), clean_<field_name> 方法来验证数据是否合法
    #
    # 如果数据有效，默认情况下 form_valid() 会被执行， 其中会自动调用 form.save() 将数据保存到数据库中，（如果重写了 form_valid()，则不会自动调用 form.save(), 而需要显示调用)
    # 如果数据保存，会重定向到 success_url 中指定的页面
    # 表单字段验证

    def form_valid(self, form):
        # 接收字段
        student_name = form.cleaned_data.get('student_name')
        student_number = form.cleaned_data.get('student_number')
        # 写入 auth_user 表，username为 student_name + student_number, 密码为 student_number 后6位
        username = f"{student_name}_{student_number}"
        password = student_number[-6:]
        users = User.objects.filter(username=username)
        if users.exists():
            # 如果已存在相同 username 的 user，直接将存在的user赋给创建的 student 数据
            user = users.first()
        else:
            # 如果不存在，使用 django 自带的 User.objects.create_user(), 该方法会自动对密码进行加密
            user = User.objects.create_user(username=username, password=password)
        # 将用户写入 student, 模型实例关联
        form.instance.user = user
        form.save()
        # 返回 json 相应
        return JsonResponse({
            'status': 'success',
            'messages': '操作成功'
        }, status=200)

    # 重写父类方法，定义表单验证失败时的逻辑
    def form_invalid(self, form):
        errors = form.errors.as_json()
        return JsonResponse({
            'status': 'error',
            'messages': errors
        }, status=400)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'

    def form_valid(self, form):
        # 获取学生对象实例, commont=False: 表示暂时不将实例保存到数据库中
        student = form.save(commit=False)
        # form.changed_data 返回一个包含表单中已更改字段名称的列表
        if 'studnet_name' in form.changed_data or 'student_number' in form.changed_data:
            # 更改 user username & password
            student_name = form.cleaned_data.get('student_name')
            student_number = form.cleaned_data.get('student_number')
            student.user.username = f"{student_name}_{student_number}"
            # 使用 make_password 对修改的密码进行加密 （create 时是使用 User.objects.create_user，这里面会调用 make_password
            student.user.password = make_password(student_number[-6:])
            student.user.save()  # 保存更改
        student.save()
        # 返回 json 相应
        return JsonResponse({
            'status': 'success',
            'messages': '操作成功'
        }, status=200)

    # 重写父类方法，定义表单验证失败时的逻辑
    def form_invalid(self, form):
        errors = form.errors.as_json()
        return JsonResponse({
            'status': 'error',
            'messages': errors
        }, status=400)


class StudentDeleteView(DeleteView):
    model = Student
    # form_class = StudentForm
    success_url = reverse_lazy('students_list')

    # 重写父类 delete() 方法
    def delete(self, request, *args, **kwargs):
        # 获取要删除的对象数据
        self.object = self.get_object()
        try:
            self.object.delete()
            return JsonResponse({
                'status': 'success',
                'messages': '删除成功',
            }, status=200)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'messages': '删除失败:' + str(e)
            }, status=500)


class StudentBulkDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students_list')

    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist('student_ids')
        if not selected_ids:
            return JsonResponse({
                'status': 'error',
                'messages': '请选择要删除的学生信息'
            }, status=400)
        # self.get_queryset() 是从 视图类（通常是 Django 的类视图，如 ListView 或 DetailView）中获取的查询集。它调用视图中的 get_queryset() 方法，通常用于获取视图中默认使用的查询集。
        # 这是面向对象编程的方式，依赖于类视图的上下文。如果你在类视图中重写了 get_queryset() 方法，你可以灵活地改变查询集的来源。
        # 适合在类视图中使用，因为类视图通常可以处理通用查询，而 get_queryset() 提供了灵活性。
        self.object_list = self.get_queryset().filter(id__in=selected_ids)
        # Student.objects.filter() 是直接使用 Django 的模型管理器 objects，它会从数据库中直接查询 Student 模型，返回所有符合条件的记录。
        # 这是直接从模型进行查询，与类视图的上下文无关，通常适用于函数视图或者你不需要动态改变查询集的情况下。
        # selected_students = Student.objects.filter(id__in=selected_ids)
        try:
            # 删除该视图所处理的查询集中的所有对象
            self.object_list.delete()
            return JsonResponse({
                'status': 'success',
                'messages': '删除成功'
            }, status=200)
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'messages': '删除失败' + str(e)
            }, status=500)


def upload_student(request):
    """Upload student data from excel file

    Args:
        request (Request): request include file path from front-end
    """
    if request.method == 'POST':
        file = request.FILES.get('excel_file')
        if not file:
            return JsonResponse({
                'status': 'error',
                'messages': '请上传excel文件'
            }, status=400)
        # 判断是否为excel类型
        ext = Path(file.name).suffix
        # print(f'ext: {ext}')
        if ext.lower() != '.xlsx':
            return JsonResponse({
                'status': 'error',
                'messages': '文件类型错误， 请上传.xlsx格式的文件'
            }, status=400)
        read_excel = ReadExcel(file)
        read_excel.get_data()
        print(read_excel.data[0])
        if read_excel.data[0] != ['班级', '姓名', '学号', '性别', '出生日期', '联系电话', '家庭住址']:
            return JsonResponse({
                'status': 'error',
                'messages': 'Excel中学生信息不是指定的格式'
            }, status=400)
        for row in read_excel.data[1:]:
            grade, student_name, student_number, gender, birthday, contact_number, address = row
            # 判断班级是否存在
            grade_name = Grade.objects.filter(grade_name=grade).first()
            if not grade_name:
                return JsonResponse({
                    'status': 'error',
                    'messages': f'上传数据中包含不存在的班级: {grade}'
                }, status=400)
            # 学生名不能为空
            if not student_name:
                return JsonResponse({'status': 'error', 'messages': '学生姓名不能为空'}, status=400)
            # 学籍号不能为空，且长度为19位
            if not student_number or len(student_number) != 19:
                return JsonResponse({'status': 'error', 'messages': '学籍号不能为空，且长度应为19位'}, status=400)
            # 学籍号不能和已存在的相同
            if Student.objects.filter(student_number=student_number).exists():
                return JsonResponse({'status': 'error', 'messages': f'学籍号：{student_number}已经存在'}, status=400)
            # 检查日期格式
            if not isinstance(birthday, datetime.datetime):
                return JsonResponse({'status': 'error', 'messages': '出生日期格式错误'}, status=400)
            # 写入数据
            try:
                username = f'{student_name}_{student_number}'
                pasword = student_number[-6:]
                users = User.objects.filter(username=username)
                if users.exists():
                    user = users.first()
                else:
                    user = User.objects.create_user(username=username, password=pasword)
                Student.objects.create(
                    student_name=student_name,
                    student_number=student_number,
                    gender='M' if gender == '男' else 'F',
                    birthday=birthday,
                    contact_number=contact_number,
                    address=address,
                    grade=grade_name,
                    user=user
                )

            except Exception as e:
                return JsonResponse({'status': 'error', 'messages': '上传失败' + str(e)}, status=500)
        return JsonResponse({
            'status': 'success',
            'messages': '上传成功',
        }, status=200)


def export_excel(request):
    """export stduent data with selected grade name

    Args:
        request (_type_): _description_
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        grade_id = data.get('grade')
        # 判断传入的值是否为空
        if not grade_id:
            return JsonResponse({'status': 'error', 'messages': '班级数据缺失'}, status=400)
        # 判断班级是否存在
        try:
            grade = Grade.objects.get(id=grade_id)
        except Grade.DoesNotExist:
            return JsonResponse({'status': 'error', 'messages': '班级不存在'}, status=404)
        students = Student.objects.filter(grade=grade)
        if not students.exists():
            return JsonResponse({'status': 'error', 'messages': '找不到指定班级的学生信息'}, status=400)
        # export_data = []

        # for student in students:
        #     row_data = [student.grade.grade_name, student.student_name,
        #                 student.student_number, student.gender, student.birthday, student.contact_number, student.address]
        #     export_data.append(row_data)
        # export_excel = ExportExcel(export_data)
        # excel_file = export_excel.export_to_execel()
        wb = openpyxl.Workbook()
        ws = wb.active
        first_column = ['班级', '姓名', '学号', '性别', '出生日期', '联系电话', '家庭住址']
        ws.append(first_column)
        for student in students:
            gender = '男' if student.gender == 'M' else '女'
            row_data = [student.grade.grade_name, student.student_name,
                        student.student_number, gender, student.birthday, student.contact_number, student.address]
            ws.append(row_data)
        excel_file = BytesIO()
        wb.save(excel_file)
        wb.close()
        # 重置文件位置
        excel_file.seek(0)
        #
        response = HttpResponse(
            excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="students.xlsx"'
        return response
