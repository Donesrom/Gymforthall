from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    trainers = Trainers.objects.all()
    benefits = Benefits.objects.all()
    heros = Hero.objects.all()
    historys = History.objects.all()
    steps = Step.objects.all()
    testimonials = Testimonial.objects.all()
    members = Members.objects.all()
    context = {

        'trainers' : trainers,
        'benefits' : benefits, 
        'heros' : heros,
        'historys' : historys,
        'steps': steps,
        'testimonials' : testimonials,
        'members' : members,

        }
    return render(request, "index.html", context)


def classes(request):
    heros = Hero.objects.all()
    context = {
        'heros' : heros, 
    }
    return render(request, "class.html", context)

def contact(request):
    return render(request, "contact.html")

