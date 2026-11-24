from django.db import models

# Create your models here.
from django.db import models

class DepositProducts(models.Model):
    # 금융 상품 코드 (기본키 대용 혹은 고유 식별자)
    fin_prdt_cd = models.TextField(unique=True)
    # 금융 회사명 (예: 우리은행)
    kor_co_nm = models.TextField()
    # 금융 상품명 (예: WON플러스예금)
    fin_prdt_nm = models.TextField()
    # 가입 방법
    join_way = models.TextField()
    # 우대 조건
    spcl_cnd = models.TextField()
    # 가입 대상
    join_member = models.TextField()
    # 가입 제한 (1: 제한없음, 2: 서민전용, 3: 일부제한)
    join_deny = models.IntegerField()
    # 기타 유의사항
    etc_note = models.TextField()


class DepositOptions(models.Model):
    # DepositProducts 모델과의 외래키 관계 설정
    # product_id 대신 fin_prdt_cd를 기준으로 참조하는 것이 일반적입니다.
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    # 금융 상품 코드
    fin_prdt_cd = models.TextField()
    # 저축 금리 유형명 (예: 단리, 복리)
    intr_rate_type_nm = models.CharField(max_length=100)
    # 저축 기간 (단위: 개월)
    save_trm = models.IntegerField()
    # 저축 금리 (데이터가 없을 경우 -1 처리)
    intr_rate = models.FloatField(default=-1)
    # 최고 우대 금리 (데이터가 없을 경우 -1 처리)
    intr_rate2 = models.FloatField(default=-1)