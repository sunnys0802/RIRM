from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from enroll.models import StudentInfo,StudentAcademics
from .forms import StudentRegistration,StudentInfoForm

# Create your views here.
def show(request):
    context = {}
    search = request.GET.get('search')
    if search:
        student = StudentInfo.objects.filter(name = search)
    else:
        student = StudentInfo.objects.all()
    context['stu'] = student
    return render(request, 'list.html' , context)

def create_or_update(request, id = None):
    context = {}
    if id:
        try:
            stud_info = StudentInfo.objects.get(roll_no = id)
            stud_acadmic = StudentAcademics.objects.get(roll_no__roll_no = id)
        except StudentInfo.DoesNotExist:
            return HttpResponse({"error":["id doesnot exist"]})
        stu_info = StudentInfoForm(request.POST or None, instance=stud_info)
        stu_academic = StudentRegistration(request.POST or None, instance=stud_acadmic)
        context['stu_info'] = stu_info
        context['stu_academic'] = stu_academic
        
    else:
        stu_info = StudentInfoForm(request.POST or None)
        stu_academic = StudentRegistration(request.POST or None)
        context['stu_info'] = stu_info
        context['stu_academic'] = stu_academic

    if request.method =='POST':
        if stu_info.is_valid() and stu_academic.is_valid():
            stu_info = stu_info.save()
            stu_academic = stu_academic.save(commit=False)
            stu_academic.roll_no = stu_info
            stu_academic.save()
            return redirect('/')
        else:
            context['stu_info'] = stu_info
            context['stu_academic'] = stu_academic
    return render(request, 'create_or_update.html' , context)

def stu_delete(request, id = None):
    try:
        student = StudentInfo.objects.get(roll_no = id)
    except StudentInfo.DoesNotExist:
        return HttpResponse({"error":["id doesnot exist"]})
    student.delete()
    return redirect('/')

def view_details(request,id):
    context = {}
    stu_details = StudentAcademics.objects.get(roll_no__roll_no = id )
    context['stu_details'] = stu_details
    return render(request, 'details.html' , context)

