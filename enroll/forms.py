from django import forms
from .models import StudentInfo,StudentAcademics

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model=  StudentInfo
        fields = "__all__"

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=  StudentAcademics
        exclude = ("roll_no",)