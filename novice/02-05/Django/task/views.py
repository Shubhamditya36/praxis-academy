from django.shortcuts import render, redirect

# Create your views here.
from . import models

def index(req):
    if req.POST:
        models.Task.objects.create(name=req.POST['name'], genre=req.POST['genre'], deskripsi=req.POST['deskripsi'])

    tasks = models.Task.objects.all()
    return render(req, 'task/index.html', {
        'data': tasks,
    })

def detail(req, id):
    task = models.Task.objects.filter(pk=id).first()    
    return render(req, 'task/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Task.objects.filter(pk=id).delete()
    return redirect('/')

def update(req, id):
    if req.POST:
        task = models.Task.objects.filter(pk=id).update(name=req.POST['name'], genre=req.POST['genre'], deskripsi=req.POST['deskripsi'])
        return redirect('/')

    task = models.Task.objects.filter(pk=id).first()    
    return render(req, 'task/update.html', {
        'data': task,
    })
