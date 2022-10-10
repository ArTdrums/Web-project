from django.urls import path
from . import views

urlpatterns =[
    path('', views.FilmViews.as_view(), name='home'),
    path('<slug:slug>/', views.FilmDetail.as_view(), name='film_detail'), # просписываем ссылку для перехода на конккретную страницу фильма
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review')

]

