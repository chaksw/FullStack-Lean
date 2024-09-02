from django import forms
from .models import Grade

# forms.Form 多用于处理与数据模型无关的数据
# forms.ModelForm 则是处理基于数据模型的数据


# ModelForm 根据与之关联的模型自动生成表单字段。每个模型字段都对应一个表单字段。例如，CharField 转换为 forms.CharField，DateField 转换为 forms.DateField，等等。
# ModelForm 自动继承并执行模型定义中的验证逻辑，如字段的 max_length、unique、blank、null 等约束条件。
# ModelForm 提供了 clean() 方法，可以对整个表单的数据进行验证和清理。你还可以为特定字段定义 clean_<fieldname>() 方法，以对单个字段进行自定义验证和清理。
# ModelForm 提供了 save() 方法，允许你轻松将表单数据保存到数据库。默认情况下，它会将表单数据保存为与模型关联的新对象，或者更新现有对象。
class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        # 通过定义 fields， GradeForm 会自动生成与 Grade 模型字段对应的表单字段
        # 并根据模型字段的定义提供相应数据验证功能
        fields = ['grade_name', 'grade_number']
