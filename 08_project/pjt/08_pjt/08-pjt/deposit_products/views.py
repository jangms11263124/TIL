from django.shortcuts import render

import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from rest_framework import status
from django.db.models import Max



@api_view(['GET'])
def save_deposit_products(request):
    # 1. API 키 및 URL 설정 [cite: 57]
    api_key = settings.API_KEY
    print(api_key)
    # url = f'http://finlife.fss.or.kr/cedif/option/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    # url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=0200000&pageNo=1'
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=2'

    
    # 2. API 데이터 요청 [cite: 104]
    response = requests.get(url).json()
    print(response)
    # 3. 상품 정보(baseList) 저장 [cite: 105, 106]
    for product in response.get('result').get('baseList'):
        fin_prdt_cd = product.get('fin_prdt_cd')
        
        # 중복 저장 방지를 위해 get_or_create 사용
        DepositProducts.objects.get_or_create(
            fin_prdt_cd=fin_prdt_cd,
            defaults={
                'kor_co_nm': product.get('kor_co_nm'),
                'fin_prdt_nm': product.get('fin_prdt_nm'),
                'join_way': product.get('join_way'),
                'spcl_cnd': product.get('spcl_cnd'),
                'join_member': product.get('join_member'),
                'join_deny': product.get('join_deny'),
                'etc_note': product.get('etc_note'),
            }
        )

    # 4. 옵션 정보(optionList) 저장 [cite: 105, 107]
    for option in response.get('result').get('optionList'):
        fin_prdt_cd = option.get('fin_prdt_cd')
        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        
        # 금리 데이터가 없을 경우 -1 처리 [cite: 108]
        intr_rate = option.get('intr_rate') if option.get('intr_rate') is not None else -1
        intr_rate2 = option.get('intr_rate2') if option.get('intr_rate2') is not None else -1

        DepositOptions.objects.get_or_create(
            product=product,
            fin_prdt_cd=fin_prdt_cd,
            intr_rate_type_nm=option.get('intr_rate_type_nm'),
            save_trm=option.get('save_trm'),
            defaults={
                'intr_rate': intr_rate,
                'intr_rate2': intr_rate2,
            }
        )

    return Response({"message": "okay"})


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
    # 1. DB에서 모든 정기예금 상품 조회
        products = DepositProducts.objects.all()
        # 2. Serializer를 활용해 직렬화 (데이터가 여러 개이므로 many=True 설정)
        serializer = DepositProductsSerializer(products, many=True)
        # 3. JSON 형태로 응답 반환
        return Response(serializer.data)


    elif request.method == 'POST':
        # 1. 사용자로부터 받은 데이터를 Serializer에 넣음
        serializer = DepositProductsSerializer(data=request.data)
        
        # 2. 유효성 검사 (필드 누락, 데이터 형식 등 확인)
        if serializer.is_valid():
            # 3. 중복 데이터 확인 등 추가 로직이 필요하다면 여기서 처리 후 저장
            serializer.save()
            return Response(
                {"message": "데이터 삽입 성공"}, 
                status=status.HTTP_201_CREATED
            )
        
        # 4. 검증 실패 시 에러 메시지 반환 (명세서 요구사항 F803-⑤)
        return Response(
            {"message": "데이터 삽입 실패", "errors": serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    # 1. 외래키인 fin_prdt_cd를 기준으로 해당 상품의 모든 옵션 조회
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    
    # 2. 조회된 옵션들을 직렬화 (여러 개일 수 있으므로 many=True)
    serializer = DepositOptionsSerializer(options, many=True)
    
    # 3. 결과 반환
    return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    # 1. 모든 옵션 중 최고 우대금리(intr_rate2)의 최댓값을 찾음
    max_rate = DepositOptions.objects.aggregate(Max('intr_rate2'))['intr_rate2__max']
    
    # 2. 해당 금리를 가진 옵션 중 하나를 가져옴 (동일 금리가 여러 개일 경우 첫 번째)
    top_option = DepositOptions.objects.filter(intr_rate2=max_rate).first()
    
    # 3. 해당 옵션과 연결된 상품 정보를 가져옴
    product = DepositProducts.objects.get(fin_prdt_cd=top_option.fin_prdt_cd)
    # 4. 상품 정보와 옵션 정보를 각각 직렬화하여 하나의 JSON으로 합침
    serializer_product = DepositProductsSerializer(product)
    serializer_option = DepositOptionsSerializer(top_option)
    
    result = {
        "product": serializer_product.data,
        "option": serializer_option.data
    }
    
    return Response(result)