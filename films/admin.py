from django.contrib import admin
from .models import Film, Direction, Genre, Reviews
'''Тут мы регистрируем таблицы'''

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'data_puble') # отображение данных
    search_fields = ('title',)# поиск
    list_filter = ('genre', 'data_puble') # фильт по жанрам и дате публикации



@admin.register(Direction)
class Direction_admin(admin.ModelAdmin):
    list_display = ('name',)



# делаем регестрацию таблиц
@admin.register(Genre)
class Genre_admin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Reviews)
class Reviews_admin(admin.ModelAdmin):
    list_display = ('name', 'film')
    readonly_fields = ('name', 'email')  # закрываем редоктирование полей для имени и почты
