from re import A
from django.shortcuts import redirect, render, reverse
from .models import Director
from .forms import DirectorForm

def directors_list(request):
    directors = Director.objects.all()
    return render(request, template_name='director/directors_list.html', context={'directors': directors})

def director_create(request):
    if request.method == 'POST':
        form = DirectorForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('director:list'))
    elif request.method == 'GET':
        form = DirectorForm()  
    return render(request, template_name='director/director_create.html', context={'form': form})

def director_details(request, pk):
    director = Director.objects.get(pk=pk)
    return render(request, template_name='director/director_details.html', context={'director': director})

def director_update(request, pk):
    director = Director.objects.get(pk=pk)
    if request.method == 'POST':
        form = DirectorForm(data=request.POST, files=request.FILES, instance=director)
        if form.is_valid():
            form.save()
            return redirect(reverse('director:list'))
    elif request.method == 'GET':
        form = DirectorForm(instance=director)
        return render(request, template_name='director/director_update.html', context={'form': form, 'director': director})

def director_delete(request, pk):
    director = Director.objects.get(pk=pk)
    director.delete()
    return redirect(reverse('director:list'))
