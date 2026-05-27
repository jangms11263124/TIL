from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.db.models import Count
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):

    # 전체 article 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
       # 200_OK

    # 단일 article 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 성공 201_CREATED
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 실패 400_BAD_REQUEST
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         

@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    # annoate(num_of_comments=Count('comment')) # 추가 세부사항
    article = Article.objects.annoate(num_of_comments=Count('comment')).get(pk=article_id)

    # 단일 article 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 단일 article 삭제
    elif request.method == 'DELETE':
        pk = article.pk
        title = article.title
        data = {
            'message1': f'{article.pk}번 글{article.title}이 삭제됐습니다.',
            'message2': f'{pk}번 글{title}이 삭제됐습니다.',
        }
        article.delete()
        # 삭제 잘 됐어요 알려줄 수 있고 
        # 삭제 다 하고서 메시지 담아서, 200_OK
        return Response(data, status=status.HTTP_200_OK)

        # 알아서 내가 지웠어 
        # 204_NO_CONTENT
        # article.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        

    # 단일 article 모든 필드 수정 
    elif request.method == 'PUT':
        # ArticleForm(instance=article, data=request.POST) # 한번 따라해보기 좋은 로직
        serializer = ArticleSerializer(instance=article, data=request.data, partial=False)
        # 잘 저장했으면 데이터만 쑝 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # 저장 못했으면 에러와 함께 400_BAD_REQUEST
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 단일 article 일부 필드 수정 
    # elif request.method == 'PATCH':
        # 잘 저장했으면 데이터만 쑝 
        # 저장 못했으면 에러와 함께 400_BAD_REQUEST
        # ArticleForm(instance=article, data=request.POST) # 한번 따라해보기 좋은 로직
        serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        # 잘 저장했으면 데이터만 쑝 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # 저장 못했으면 에러와 함께 400_BAD_REQUEST
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def comment_list(request):
   comments = Comment.objects.all()
   serializer = CommentSerializer(comments, many=True)
   return Response(serializer.data)



@api_view(['GET', 'PATCH', 'DELETE'])
def comment_detail(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        pk = comment.pk
        content = comment.content
        data = {
            'message': f'{pk}번 글{content}이 삭제됐습니다.',
        }
        comment.delete()
        # 삭제 잘 됐어요 알려줄 수 있고 
        # 삭제 다 하고서 메시지 담아서, 200_OK
        return Response(data, status=status.HTTP_200_OK)
    
        # comment.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PATCH':
       serializer = CommentSerializer(instance=comment, data=request.data, partial=True)
       if serializer.is_valid(raise_exception=True):
           serializer.save()
           return Response(serializer.data)
           

       


@api_view(['POST'])
def comment_create(request, article_id):
    article = Article.objects.get(pk=article_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # 장고 drf
        serializer.save(article=article)
        # 장고
        # fk 외래키 필드 에다가 객체를 저장
        # mtm 참조 필드에다가 추가 제거
        return Response(serializer.data, status=status.HTTP_201_CREATED)