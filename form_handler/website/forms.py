from django import forms

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=30, empty_value=False)
#     last_name = forms.CharField(max_length=30, empty_value=False)
#     birth = forms.DateField()
#     phone = forms.CharField(max_length=20)
from website.models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = 'created', 'updated'