from django.shortcuts import render, redirect, HttpResponse
from time import localtime, strftime
import random
from django.contrib import messages
from .models import Show, ShowManager

# ============= main page =================

def shows(request):

    context = {
        "show_list" : Show.objects.all()
    }

    return render(request,'shows.html',context)

# ============= add show page ==============

def new(request):



    return render(request,'new_show.html')

# ============= create show =================

def create(request):

    errors = Show.objects.show_validator(request.POST)
    
    if len(errors) > 0:
        
        for value in errors.items():
            messages.error(request, value)
        
        return redirect('/shows/new')
    else:
        cshow = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release'],
            description = request.POST['description']
        )

        messages.success(request, "Show successfully updated")

        return redirect(f'/shows/{cshow.id}')

# ============= edit show page ==============

def edit(request, show_id):

    context = {
    "change" : Show.objects.get(id=show_id)
    }
    return render(request,'edit_show.html',context)

# ============= show view page ==============

def show_view(request, show_id):

    context = {
        "guide" : Show.objects.get(id=show_id)    }

    return render(request,'show_view.html',context)

# ===== delete item from show page =============

def delete(request, show_id):
    delete_show = Show.objects.get(id=show_id)
    delete_show.delete()
    return redirect('/shows')

# ============= edit show  view ============

def update(request, show_id):

    errors = Show.objects.show_validator(request.POST)

    if len(errors) > 0:
        
        for value in errors.items():
            messages.error(request, value)
        
        return redirect(f'/shows/{show_id}/edit')
    else:
        modify = Show.objects.get(id=show_id)
    
        modify.title = request.POST['title']
        modify.network = request.POST['network']
        modify.release_date = request.POST['release']
        modify.description = request.POST['description']

        modify.save()

        messages.success(request, "Show successfully updated")

        return redirect(f'/shows/{show_id}')

# ===== root pagge =============

def root(request):
    
    return redirect('/shows')

