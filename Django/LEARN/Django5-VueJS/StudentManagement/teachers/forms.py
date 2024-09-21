from django.core.exceptions import ValidationError
import datetime
from django import forms
from .models import Teacher
from grades.models import Grade

GENDER_CHOICES = [
    ('M', '男'),
    ('F', '女'),
]


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'phone_number', 'gender', 'birthday', 'grade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 为前端表单重新定义 grade的排序方式
        # 重新定义 外键 grade 为 Grade 的 object 的排序方式，并以 grade_number 进行排序（默认升序）
        self.fields.get('grade').queryset = Grade.objects.all().order_by('grade_number')
        self.fields['grade'].empty_label = '请选择班级'
        self.fields['gender'].widget = forms.Select(choices=GENDER_CHOICES)

    def clean_teacher_name(self):
        teacher_name = self.cleaned_data.get('teacher_name')
        if len(teacher_name) < 2 or len(teacher_name) > 50:
            raise ValidationError('请填写正确的姓名')
        return teacher_name

    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        if not isinstance(birthday, datetime.date):
            raise ValidationError('生日日期格式错误，正确格式为如：2024-05-01')
        if birthday > datetime.date.today():
            raise ValidationError('生日日期不能大于今天')
        return birthday

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if len(phone_number) != 11:
            raise ValidationError('请填写正确的手机号（长度应为11位）')
        return phone_number
