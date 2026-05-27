from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # read
    path('<int:pk>/', views.detail, name='detail'),
    # create
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # delete
    path('<int:pk>/delete', views.delete, name='delete'),
    # update
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]