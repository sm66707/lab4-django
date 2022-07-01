from django.shortcuts import render, redirect, reverse
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

def movies_list(request):
    movies = Movie.objects.all()
    return render(request, template_name='movie/movies_list.html', context={'movies': movies})

@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('movie:list'))
    elif request.method == 'GET':
        form = MovieForm()  
    return render(request, template_name='movie/movie_create.html', context={'form': form})

def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, template_name='movie/movie_details.html', context={'movie': movie})

def movie_update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect(reverse('movie:list'))
    elif request.method == 'GET':
        form = MovieForm(instance=movie)
        return render(request, template_name='movie/movie_update.html', context={'form': form, 'movie': movie})

def movie_delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect(reverse('movie:list'))
