from django.shortcuts import render
from .models import Skill, Project, Achievement
from .forms import ContactForm
from django.contrib import messages

def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    achievements = Achievement.objects.all()

    return render(request, 'home.html', {
        'skills': skills,
        'projects': projects,
        'achievements': achievements,
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
