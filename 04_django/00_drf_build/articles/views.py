from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


# Create your views here.
# @api_view(['GET', 'POST'])
def article_list(request):
    pass

    # if request.method == 'GET':
       
    
    # elif request.method == 'POST':
        
        

    
# @api_view(['GET', 'DELETE', 'PATCH'])
def article_detail(request, article_id):
    pass 

    # if request.method == 'GET':
        
    # elif request.method == 'DELETE':
        
    # elif request.method == 'PATCH':
        



# @api_view(['GET'])
def comment_list(request):
   pass


# @api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_id):
    pass
    # if request.method == 'GET':
       
    
    # elif request.method == 'PUT':
       

    # elif request.method == 'DELETE':
       


# @api_view(['POST'])
def comment_create(request, article_id):
    pass