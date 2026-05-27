from django.shortcuts import render
import random

def index(request):
    context = {
        'name': 'Haley',
        # 'login': False,
        # 'nums': [1, 2, 3],
    }
    # render 함수를 리턴 해야하고 
    # 1. request
    # 2. templates 경로 주의
    # (3). context <- template 넘겼을때 사용할 값들의 주머니
    # 어지간하면 ..꼭 dict 
    # 장고가 알아서 templates/ 부터 찾아가기 때문에 template 경로에는 tempplates/ 추가 금지!! 
    return render(request, 'articles/index.html', context)
    # redirect 


# def dinner(request):
#     foods = ['국밥', '국수', '카레', '탕수육']
#     picked = random.choice(foods)
#     context = {
#         'foods': foods,
#         'picked': picked,
#     }
#     return render(request, 'articles/dinner.html', context)


# def search(request):
#     return render(request, 'articles/search.html')


# def throw(request):
#     return render(request, 'articles/throw.html')


# # 사용자 입력 데이터를 추출해서 응답 페이지에 보여주기
# def catch(request):
#     # 사용자 입력데이터는 대체 어디에 있을까? -> request 객체
#     # print(request.GET)  # <QueryDict: {'message': ['ssafy']}>
#     # print(request.GET.get('message'))  # ssafy
#     message = request.GET.get('message')
    
#     context = {
#         'message': message,
#     }
#     return render(request, 'articles/catch.html', context)


# def detail(request, num):
#     context = {
#         'num': num,
#     }
#     return render(request, 'articles/detail.html', context)


# def greeting(request, name):
#     context = {
#         'name': name,
#     }
#     return render(request, 'articles/greeting.html', context)