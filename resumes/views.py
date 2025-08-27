from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume

def home(request):
    return render(request, 'resumes/home.html')

def submit_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'resumes/submit_resume.html', {'form': form})

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resumes/resume_list.html', {'resumes': resumes})
