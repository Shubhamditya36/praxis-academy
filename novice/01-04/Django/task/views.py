from django.shortcuts import render

# Create your views here.
from . import models

def index (req):
    if req.POST:
        models.Task.objects.create(name=req.POST['name'])

    tasks = models.Task.objects.all()
    return render(req, 'task/index.html', {
        'data': tasks,
    })