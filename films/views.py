from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Film
from .form import ReviewForm


class FilmViews(View):
    '''Список фильмов'''

    def get(self, request):
        films = Film.objects.all()  # берем все поля, которые у нас есть в фильмах, все что мы написали в моделе
        return render(request, 'films/film.html',
                      {'film_list': films})  # обьединяет указанный шаблон со словарем и возвращает http
        # обьект со все отображаемым текстом т сло всем, что мы подтянули из бд


# Create your views here.

class FilmDetail(View):
    '''страница одного фильма'''

    def get(self, request, slug):
        film = Film.objects.get(url=slug)
        return render(request, 'films/film_detail.html', {'film': film})

class AddReview(View):
    '''добавление отзывов'''
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        film =Film.objects.get(id=pk)
        if form.is_valid(): # проверка на валидность, это конструкция джанго
            form = form.save(commit=False)
            form.film = film
            form.save()
        return redirect(film.get_absolute_url())

