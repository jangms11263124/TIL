from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.asset_list, name='asset_list'),
    path('<str:asset_id>/', views.board_list, name='board_list'),
    path('<str:asset_id>/create/', views.post_create, name='post_create'),
    path('<str:asset_id>/<int:post_id>/', views.post_detail, name='post_detail'),
    path('<str:asset_id>/<int:post_id>/update/', views.post_update, name='post_update'),
    path('<str:asset_id>/<int:post_id>/delete/', views.post_delete, name='post_delete'),
]
