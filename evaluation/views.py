from django.shortcuts import render,redirect
from django.contrib.auth.models import User

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
            print(row)
        return render(request,'evaluation/course.html')
    else:
        return render(request,'evaluation/course.html')
