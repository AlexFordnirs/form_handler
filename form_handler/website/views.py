from django.shortcuts import render

from website.models import Student
from website.forms import  StudentForm


def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        form.save()
        # post = {
        #     'first_name': request.POST.get('first_name', None),
        #     'last_name': request.POST.get('last_name', None),
        #     'birth': request.POST.get('birth', None),
        #     'phone': request.POST.get('phone', None)
        # }
        # Student.objects.create(**post)
    context = {
        'form': StudentForm(),
        'students': Student.objects.all()
    }
    return render(request, 'index.html', context=context)
