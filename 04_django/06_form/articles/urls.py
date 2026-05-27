from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # read
    path('<int:pk>/', views.detail, name='detail'),

    # create
    # GET
    path('new/', views.new, name='new'), # form 태그를 보여줘서 입력 받는 곳 
    # POST
    path('create/', views.create, name='create'), # 생성 후 저장
    
    # delete
    path('<int:pk>/delete', views.delete, name='delete'),
    
    # update
    # GET
    path('<int:pk>/edit/', views.edit, name='edit'),  # form 태그를 보여줘서 입력 기존 데이터 보여주고 새로운 입력 받는 곳 
    # POST
    path('<int:pk>/update/', views.update, name='update'), # 기존 값에서 변경된 사항을 저장

    # path('', views.index, name='index'),
    # path('<int:article_id>/', views.detail, name='detail'),
    # path('new/', views.new, name='new'),
    # path('create/', views.create, name='create'),
    # path('<int:article_id>/delete/', views.delete, name='delete'),
    # path('<int:article_id>/edit/', views.edit, name='edit'),
    # path('<int:article_id>/update/', views.update, name='update'),
]