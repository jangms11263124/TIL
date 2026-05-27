from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'articles' # 갈곳 
urlpatterns = [
    path('', views.index, name='index'),
    # C R U D
    # R C D U 
    # C R D U
    path('create/', views.create, name='create'), # 별명 
    path('<int:pk>/', views.detail, name='detail'), 
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/update', views.update, name='update'),
]