from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Course,Attendance
import csv

def uploadMarksView(request):
    if request.method=="POST":
        return render(request,'evaluation/marks.html')
    else:
        return render(request,'evaluation/marks.html')

def uploadCourseView(request):
    if request.method == 'POST':
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            course=Course(name=row['Course'])
            course.save()
            course=None
        return render(request,'evaluation/course.html')
    else:
        return render(request,'evaluation/course.html')

def uploadAttendanceView(request):
    if request.method == 'POST':
        print(request)
        file = request.FILES['file']
        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        course = Course.objects.get(name=request.POST['course'])
        for row in reader:
            print(row)
            name=row['Name']
            user=User.objects.get(username=name)
            attendance=Attendance(user=user,course=course,total_classes=row['total_classes'],attendance=row['attendance'])
            attendance.save()
            attendance=None
        course = Course.objects.all()
        return render(request,'evaluation/attendance.html',{'course':course})
    else:
        course = Course.objects.all()
        return render(request,'evaluation/attendance.html',{'course':course})
