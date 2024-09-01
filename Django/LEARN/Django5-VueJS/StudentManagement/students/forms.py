from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['student_name', 'student_number', 'grade', 'gender', 'birthday', 'contact_number', 'address']
