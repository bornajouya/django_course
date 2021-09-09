from django.urls import path

from . import views

urlpatterns = [
    path('getbooks/', views.book_list),
    path('sp-book/', views.sp_book),
    path('create/', views.create),
    path('uploadphoto/', views.uploadphoto),
    path('deletebook/', views.delete),
]