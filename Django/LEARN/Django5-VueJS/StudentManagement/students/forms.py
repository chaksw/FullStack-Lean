import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Student
from grades.models import Grade


class StudentForm(forms.ModelForm):
    # 重写 form 的 __init__ 方法
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 重新定义 外键 grade 为 Grade 的 object，并以 grade_number 进行排序（默认升序）
        self.fields.get('grade').queryset = Grade.objects.all().order_by('grade_number')
    # 定义字段验证方法： clean_<field_name>

    def clean_student_name(self):
        # self.cleaned_data 为提交的全部表单信息
        student_name = self.cleaned_data.get('student_name')
        if len(student_name) < 2 or len(student_name) > 50:
            raise ValidationError('请填写正确的学生名')
        return student_name

    def clean_student_number(self):
        student_number = self.cleaned_data.get('student_number')
        if len(student_number) != 19:
            raise ValidationError('请填写正确的学籍号（长度应为19位）')
        return student_number

    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        if not isinstance(birthday, datetime.date):
            raise ValidationError('生日日期格式错误，正确格式为如：2024-05-01')
        if birthday > datetime.date.today():
            raise ValidationError('生日日期不能大于今天')

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if len(contact_number) != 11:
            raise ValidationError('请填写正确的手机号（长度应为11位）')
        return contact_number

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['student_name', 'student_number', 'grade', 'gender', 'birthday', 'contact_number', 'address']
