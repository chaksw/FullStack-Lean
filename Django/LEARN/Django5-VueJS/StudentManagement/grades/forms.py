from django import forms
from .models import Grade

# forms.Form 多用于处理与数据模型无关的数据
# forms.ModelForm 则是处理基于数据模型的数据


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        # 通过定义 fields， GradeForm 会自动生成与 Grade 模型字段对应的表单字段
        # 并根据模型字段的定义提供相应数据验证功能
        fields = ['grade_name', 'grade_number']
