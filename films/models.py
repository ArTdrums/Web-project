from django.db import models
from django.urls import reverse

# модельки для БД
class Genre(models.Model):
    '''Жанры фильмов'''
    name = models.CharField('Название', max_length=20)
    description = models.TextField('описание', blank=True)  # создаем атрибуты класса
    url = models.SlugField(max_length=50,
                           unique=True)  # это поле отвеает за урл по которому мы можем попасть на страницу данной котегории

    # unique=True делает ссылки уникальными
    def __str__(self):  # магический метод выволит в алмин панель
        return self.name

    class Meta:  # позволяет указать уровни абстрации, единственное или множ чсило
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Direction(models.Model):
    '''Создаем класс резесcеры'''
    name = models.CharField('Имя режесcера', max_length=100)
    descriptions = models.TextField('Биография', blank=True)
    imag = models.ImageField(upload_to='image/descriptions/%Y')

    def __str__(self):  # магический метод выволит в аlмин панель
        return self.name

    class Meta:  # позволяет указать уровни абстрации, единственное или множ чсило
        verbose_name = 'Режиссеры'
        verbose_name_plural = 'Режиссер'


class Film(models.Model):
    '''Фильмы'''
    title = models.CharField(max_length=100)  # создание названия / заголовка
    imag = models.ImageField(upload_to='image/%Y')  # создание картинки
    descriptions = models.TextField(blank=True)  # описание фильма
    data_puble = models.DateField('Дата публикации')  # создаем дату публикации
    direction = models.ManyToManyField(Direction, verbose_name='Режиссеры', related_name='film_direct')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры')
    url = models.SlugField(max_length=100, unique=True)  # адрес нашего фильма

    def __str__(self):
        return f'{self.title}, {self.data_puble}'

    def get_absolute_url(self):
        return reverse('film_detail', kwargs={'slug': self.url})

    class Meta:  # позволяет указать уровни абстрации, единственное или множ чсило
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Reviews(models.Model):
    '''отзывы'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text_reviews = models.TextField('Текст отзыва', max_length=2000)
    film = models.ForeignKey(Film, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.film}'


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
