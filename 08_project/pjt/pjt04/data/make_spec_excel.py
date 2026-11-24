"""
PDF 명세서 → 엑셀 재현 스크립트
(26_0417) 관통템플릿_[파이썬]_[금융]_[15기]_[4회차].pdf 내용을
통합 문서1.xlsx 에 PDF와 동일한 레이아웃으로 재현합니다.
"""

from openpyxl import load_workbook
from openpyxl.styles import (
    Font, PatternFill, Alignment, Border, Side, GradientFill
)
from openpyxl.utils import get_column_letter

wb = load_workbook('통합 문서1.xlsx')

# ── 헬퍼 ──────────────────────────────────────────────
def make_border(style='thin'):
    s = Side(style=style, color='000000')
    return Border(left=s, right=s, top=s, bottom=s)

def make_side_border(left=None, right=None, top=None, bottom=None):
    return Border(
        left  =Side(style=left,   color='000000') if left   else Side(style=None),
        right =Side(style=right,  color='000000') if right  else Side(style=None),
        top   =Side(style=top,    color='000000') if top    else Side(style=None),
        bottom=Side(style=bottom, color='000000') if bottom else Side(style=None),
    )

GRAY_FILL   = PatternFill('solid', fgColor='595959')   # 헤더 진한 회색
LGRAY_FILL  = PatternFill('solid', fgColor='D9D9D9')   # 테이블 헤더 연회색
WHITE_FILL  = PatternFill('solid', fgColor='FFFFFF')
YELLOW_FILL = PatternFill('solid', fgColor='FFF2CC')   # 필수 강조

def cell_write(ws, row, col, value,
               bold=False, size=11, color='000000',
               fill=None, align_h='left', align_v='center',
               wrap=True, border=None, italic=False):
    c = ws.cell(row=row, column=col, value=value)
    c.font      = Font(name='맑은 고딕', bold=bold, size=size,
                       color=color, italic=italic)
    c.alignment = Alignment(horizontal=align_h, vertical=align_v,
                            wrap_text=wrap)
    if fill:   c.fill   = fill
    if border: c.border = border
    return c

def merge_write(ws, r1, c1, r2, c2, value, **kwargs):
    ws.merge_cells(start_row=r1, start_column=c1,
                   end_row=r2,   end_column=c2)
    cell_write(ws, r1, c1, value, **kwargs)

# ── 시트 준비 ──────────────────────────────────────────
def setup_sheet(ws, title):
    ws.title = title
    ws.sheet_view.showGridLines = False
    ws.page_setup.paperSize     = 9          # A4
    ws.page_setup.orientation   = 'portrait'
    ws.page_setup.fitToWidth    = 1
    ws.page_setup.fitToHeight   = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins.left   = 0.5
    ws.page_margins.right  = 0.5
    ws.page_margins.top    = 0.7
    ws.page_margins.bottom = 0.7

# ══════════════════════════════════════════════════════
#  시트 1 : 표지
# ══════════════════════════════════════════════════════
ws1 = wb.worksheets[0]
setup_sheet(ws1, '1_표지')

# 열 너비
for col, w in [(1,3),(2,20),(3,20),(4,20),(5,20),(6,3)]:
    ws1.column_dimensions[get_column_letter(col)].width = w
# 행 높이
for r,h in [(1,15),(2,50),(3,30),(4,30),(5,30),(6,30),(7,30),(8,40)]:
    ws1.row_dimensions[r].height = h

# 상단 회색 바 (對外秘)
ws1.merge_cells('A1:F1')
cell_write(ws1,1,1,'對外秘', bold=True, size=10, color='FFFFFF',
           fill=GRAY_FILL, align_h='right', align_v='center')

# 메인 타이틀
merge_write(ws1,2,1,2,6,'프로젝트  명세서',
            bold=True, size=28, align_h='center', align_v='center')

# 부제목들
merge_write(ws1,3,1,3,6,'금융 자산 정보 토론 게시판',
            bold=True, size=20, align_h='center', align_v='center')
merge_write(ws1,4,1,4,6,'(Python)',
            bold=False, size=14, align_h='center', align_v='center')
merge_write(ws1,5,1,5,6,'"금융 상품 비교 애플리케이션"',
            bold=False, size=13, align_h='center', align_v='center', italic=True)
merge_write(ws1,6,1,6,6,'4회차',
            bold=True, size=16, align_h='center', align_v='center')

# ══════════════════════════════════════════════════════
#  시트 2 : 목차
# ══════════════════════════════════════════════════════
wb.create_sheet('2_목차')
ws2 = wb['2_목차']
setup_sheet(ws2, '2_목차')

for col, w in [(1,3),(2,60),(3,8),(4,3)]:
    ws2.column_dimensions[get_column_letter(col)].width = w
for r,h in [(1,15),(2,35),(3,18),(4,18),(5,18),(6,18),(7,18),(8,18)]:
    ws2.row_dimensions[r].height = h

ws2.merge_cells('A1:D1')
cell_write(ws2,1,1,'對外秘  2', bold=True, size=10, color='FFFFFF',
           fill=GRAY_FILL, align_h='right')

merge_write(ws2,2,1,2,4,'목  차', bold=True, size=18, align_h='left', align_v='bottom')

toc = [
    ('1. 금융 자산 정보 토론 게시판', '3'),
    ('    1.1 목표', '3'),
    ('    1.2 준비사항', '3'),
    ('    1.3 작업 순서', '4'),
    ('    1.4 요구사항', '4'),
    ('    1.5 참고자료', '16'),
    ('    1.6 프로젝트 결과', '16'),
]
for i,(text,page) in enumerate(toc,3):
    cell_write(ws2, i, 2, text, size=11)
    cell_write(ws2, i, 3, page, size=11, align_h='right')
    ws2.row_dimensions[i].height = 18

# ══════════════════════════════════════════════════════
#  시트 3 : 개요 & 목표 & 준비사항
# ══════════════════════════════════════════════════════
wb.create_sheet('3_개요및목표')
ws3 = wb['3_개요및목표']
setup_sheet(ws3, '3_개요및목표')

for col,w in [(1,3),(2,12),(3,18),(4,18),(5,10),(6,3)]:
    ws3.column_dimensions[get_column_letter(col)].width = w

def rh(ws,r,h): ws.row_dimensions[r].height = h

# 헤더
ws3.merge_cells('A1:F1')
cell_write(ws3,1,1,'對外秘  3', bold=True, size=10, color='FFFFFF',
           fill=GRAY_FILL, align_h='right')
rh(ws3,1,15)

# 프로젝트 정보 표
info = [
    ('PJT명',       '금융 자산 정보 토론 게시판'),
    ('단계',        '04 PJT'),
    ('진행일자',    '2026.04.17'),
    ('예상 구현 시간', '필수기능  6H\n심화기능  2H'),
]
b = make_border()
for i,(label,val) in enumerate(info,2):
    rh(ws3,i,22)
    cell_write(ws3,i,2,label, bold=True, size=10, fill=LGRAY_FILL,
               border=b, align_h='center')
    ws3.merge_cells(start_row=i,start_column=3,end_row=i,end_column=5)
    cell_write(ws3,i,3,val, size=10, border=b)

# 1. 제목
rh(ws3,7,20); rh(ws3,8,16)
merge_write(ws3,7,1,7,6,'1. 금융 자산 정보 토론 게시판',
            bold=True, size=13, align_v='bottom')
merge_write(ws3,8,1,8,6,'1.1 목표', bold=True, size=11, align_v='bottom')

rh(ws3,9,14)
merge_write(ws3,9,1,9,6,'이번 프로젝트의 목표는 다음과 같습니다.', size=10)

goals = [
    '- Django의 URL 라우팅, View, Template, Model을 활용해 CRUD 흐름을 이해한다.',
    '- JSON 파일 기반의 초기 데이터를 읽어 웹 화면에 출력하는 방법을 익힌다.',
    '- 금융 자산별 게시판 구조를 설계하고 게시글 작성/조회/수정/삭제 기능을 구현한다.',
    '- 예외 상황(잘못된 자산 ID 등)에 대한 404 처리로 안정적인 사용자 경험을 제공한다.',
    '- (심화) LLM API를 활용해 게시글의 부적절 표현을 사전 차단하는 콘텐츠 필터링을 구현한다.',
]
for j,g in enumerate(goals,10):
    rh(ws3,j,14)
    merge_write(ws3,j,1,j,6,g, size=10)

rh(ws3,16,16)
merge_write(ws3,16,1,16,6,'1.2 준비사항', bold=True, size=11, align_v='bottom')
rh(ws3,17,14)
merge_write(ws3,17,1,17,6,'1) 개발언어 및 툴', bold=True, size=10)

tools = ['- Python, Django','- JSON','- SQLite',
         '- python-dotenv(환경변수 관리)','- Visual Studio Code',
         '- OpenAI 또는 Upstage API (심화)']
for k,t in enumerate(tools,18):
    rh(ws3,k,14)
    merge_write(ws3,k,1,k,6,t, size=10)

# ══════════════════════════════════════════════════════
#  시트 4 : 요구사항 테이블 (F401~NF402)
# ══════════════════════════════════════════════════════
wb.create_sheet('4_요구사항')
ws4 = wb['4_요구사항']
setup_sheet(ws4, '4_요구사항')

for col,w in [(1,3),(2,7),(3,8),(4,14),(5,35),(6,9),(7,3)]:
    ws4.column_dimensions[get_column_letter(col)].width = w

ws4.merge_cells('A1:G1')
cell_write(ws4,1,1,'對外秘  4', bold=True, size=10, color='FFFFFF',
           fill=GRAY_FILL, align_h='right')
rh(ws4,1,15)

rh(ws4,2,20)
merge_write(ws4,2,1,2,7,'1.3 작업 순서', bold=True, size=11, align_v='bottom')

steps = [
    '1) 페어와 같이 요구사항(기본/심화)을 분석한다.',
    '2) 페어와 함께 개발 시 역할을 분담한다.',
    '3) 팀장/네비게이터 등 역할 분담',
    '4) [선택] 추가적인 아이디어를 적용하여 구현하고 프로젝트를 완성한다.',
    '5) 코드 및 산출물을 정리하여 Git에 반영한다.',
]
for i,s in enumerate(steps,3):
    rh(ws4,i,14)
    merge_write(ws4,i,1,i,7,s, size=10)

rh(ws4,9,20)
merge_write(ws4,9,1,9,7,'1.4 요구사항', bold=True, size=11, align_v='bottom')

desc = ('본 프로젝트는 금융 자산 목록 데이터를 기반으로 자산별 토론 게시판을 제공하는 '
        'Django CRUD 웹 애플리케이션 구현을 목표로 한다. data/assets.json 파일에서 자산 '
        '정보를 로드하여 목록 화면에 출력하고, 각 자산 상세 페이지에서 게시글 CRUD 기능을 수행할 수 있도록 구성한다.\n'
        '이를 통해 파일 데이터 연동, 데이터베이스 기반 웹 개발, 예외 처리(404) 등 Django '
        '핵심 개발 흐름을 종합적으로 학습할 수 있다.')
rh(ws4,10,50)
merge_write(ws4,10,1,10,7,desc, size=10, wrap=True)

# ─── 기능적 요구사항 헤더 ───────────────────────────────
rh(ws4,12,16)
merge_write(ws4,12,1,12,7,'기능적 요구사항', bold=True, size=11, fill=LGRAY_FILL,
            border=make_border(), align_h='center')

rh(ws4,13,16)
headers = ['번호','분류','요구사항명','요구사항 상세','우선순위']
hcols   = [2,3,4,5,6]
for h,c in zip(headers,hcols):
    cell_write(ws4,13,c,h, bold=True, size=10, fill=LGRAY_FILL,
               border=make_border(), align_h='center')

# 기능 요구사항 데이터
func_reqs = [
    ('F401','자산\n데이터','자산 목록\n출력하기',
     '제공된 assets.json 파일을 읽어 자산 목록 페이지에 출력한다.\n'
     '각 항목에는 자산명, 코드(또는 식별자), 게시판 이동 링크를 포함한다.','필수'),
    ('F402','모델\n설계','게시판 모델\n작성',
     '게시글 저장을 위한 모델(Post)을 정의한다.\n세부 스키마는 상세 요구사항에서 제공된다.','필수'),
    ('F403','게시판\n화면','자산별 게시판\n구현',
     'URL 파라미터의 asset_id를 기준으로 해당 자산 게시판을 제공한다.\n'
     '자산 정보와 함께 해당 자산의 게시글 목록을 출력한다.','필수'),
    ('F404','게시글\n관리','게시글 생성',
     '게시글 작성 폼을 제공하고, 유효한 입력값(제목/내용)을 받아 DB에 저장한다.\n'
     '저장 후 해당 자산 게시판 목록으로 리다이렉트한다.','필수'),
    ('F405','게시글\n관리','게시글 상세\n조회',
     '게시글 목록에서 특정 게시글 선택 시 상세 페이지를 제공한다.\n'
     '제목, 내용, 작성자, 작성일 정보를 표시한다.','필수'),
    ('F406','게시글\n관리','게시글 수정',
     '기존 게시글 데이터를 폼에 바인딩하여 수정 가능하게 한다.\n'
     '수정 완료 시 DB 반영 후 상세 페이지로 이동한다.','필수'),
    ('F407','게시글\n관리','게시글 삭제',
     '삭제 요청(POST) 시 해당 게시글을 DB에서 제거한다.\n'
     '삭제 완료 후 자산별 게시판 목록으로 이동하고 안내 메시지를 표시한다.','필수'),
    ('F408','예외\n처리','잘못된 경로/ID\n처리',
     '존재하지 않는 asset_id 또는 post_id 접근 시 404 상태 코드를 반환한다.\n'
     '사용자에게 오류 안내 페이지(또는 기본 404 페이지)를 제공한다.','필수'),
    ('F411','환경\n설정','환경변수 설정',
     '.env의 MODE(OPENAI/UPSTAGE) 및 API 키를 읽어 공급자별 호출 처리,\n'
     '실패 시 안전하게 우회','심화'),
    ('F412','콘텐츠\n검증','LLM 부적절 표현\n필터링',
     '게시글 등록/수정 시 욕설·비방 등 부적절 문구를 LLM으로 검사 후 차단','심화'),
]

for idx,(no,cat,name,detail,priority) in enumerate(func_reqs, 14):
    rh(ws4,idx,42)
    b = make_border()
    pri_fill = YELLOW_FILL if priority=='심화' else WHITE_FILL
    for col,val,bld in [(2,no,True),(3,cat,False),(4,name,False),(5,detail,False)]:
        cell_write(ws4,idx,col,val, size=9, border=b,
                   bold=bld, align_h='center', align_v='center')
    cell_write(ws4,idx,6,priority, size=9, border=b,
               bold=True, align_h='center', align_v='center', fill=pri_fill)

# ─── 비기능 요구사항 ────────────────────────────────────
nf_row = 14 + len(func_reqs) + 1
rh(ws4,nf_row,16)
merge_write(ws4,nf_row,1,nf_row,7,'비기능적 요구사항',
            bold=True, size=11, fill=LGRAY_FILL,
            border=make_border(), align_h='center')

rh(ws4,nf_row+1,16)
for h,c in zip(headers,hcols):
    cell_write(ws4,nf_row+1,c,h, bold=True, size=10, fill=LGRAY_FILL,
               border=make_border(), align_h='center')

nf_reqs = [
    ('NF401','문서화','README 작성',
     '분석 흐름과 학습 내용, 어려웠던 점을 README.md에 기록하여 제출','필수'),
    ('NF402','유지보수','코드 정리',
     '.gitignore를 추가하여 불필요한 파일 제외','필수'),
]
for idx2,(no,cat,name,detail,priority) in enumerate(nf_reqs, nf_row+2):
    rh(ws4,idx2,35)
    b = make_border()
    for col,val in [(2,no),(3,cat),(4,name),(5,detail)]:
        cell_write(ws4,idx2,col,val, size=9, border=b,
                   align_h='center', align_v='center',
                   bold=(col==2))
    cell_write(ws4,idx2,6,priority, size=9, border=b,
               bold=True, align_h='center', align_v='center')

# ══════════════════════════════════════════════════════
#  시트 5 : DB 모델 스키마 (F402 상세)
# ══════════════════════════════════════════════════════
wb.create_sheet('5_DB모델스키마')
ws5 = wb['5_DB모델스키마']
setup_sheet(ws5, '5_DB모델스키마')

for col,w in [(1,3),(2,16),(3,16),(4,18),(5,22),(6,3)]:
    ws5.column_dimensions[get_column_letter(col)].width = w

ws5.merge_cells('A1:F1')
cell_write(ws5,1,1,'對外秘  5', bold=True, size=10, color='FFFFFF',
           fill=GRAY_FILL, align_h='right')
rh(ws5,1,15)

rh(ws5,2,20)
merge_write(ws5,2,1,2,6,'게시판 모델 작성 (F402)', bold=True, size=13, align_v='bottom')

rh(ws5,3,14)
merge_write(ws5,3,1,3,6,'② 게시글 저장을 위한 모델 Post 를 정의한다.', size=10)

# 스키마 헤더
rh(ws5,5,18)
schema_headers = ['필드명 (Field)','타입 (Type)','제약조건 (Constraints)','설명 (Description)']
for i,h in enumerate(schema_headers,2):
    cell_write(ws5,5,i,h, bold=True, size=10, fill=LGRAY_FILL,
               border=make_border(), align_h='center')

schema_data = [
    ('asset_id','CharField','max_length=50','금융 자산 ID'),
    ('title','CharField','max_length=200','게시글 제목'),
    ('content','TextField','X','게시글 내용'),
    ('author','CharField','default="익명"','게시글 작성자'),
    ('created_at','DateTimeField','자동 생성','생성 일자'),
    ('updated_at','DateTimeField','자동 갱신','수정 일자'),
]
for idx,(fn,ft,fc,fd) in enumerate(schema_data,6):
    rh(ws5,idx,18)
    b = make_border()
    for c,v in zip([2,3,4,5],[fn,ft,fc,fd]):
        cell_write(ws5,idx,c,v, size=10, border=b, align_h='center', align_v='center')

rh(ws5,13,14)
merge_write(ws5,13,1,13,6,'④ 마이그레이션 명령어를 통해 데이터베이스에 반영한다.',size=10)
rh(ws5,14,14)
merge_write(ws5,14,1,14,6,'   python manage.py makemigrations  →  python manage.py migrate',
            size=10, italic=True, color='1F497D')

# ══════════════════════════════════════════════════════
#  시트 6 : 참고자료 & 결과물
# ══════════════════════════════════════════════════════
wb.create_sheet('6_참고자료및결과')
ws6 = wb['6_참고자료및결과']
setup_sheet(ws6, '6_참고자료및결과')

for col,w in [(1,3),(2,60),(3,3)]:
    ws6.column_dimensions[get_column_letter(col)].width = w

ws6.merge_cells('A1:C1')
cell_write(ws6,1,1,'對外秘  6', bold=True, size=10, color='FFFFFF',
           fill=GRAY_FILL, align_h='right')
rh(ws6,1,15)

rh(ws6,2,20)
merge_write(ws6,2,1,2,3,'1.5 참고자료', bold=True, size=13, align_v='bottom')

refs = [
    '1) Django 공식 문서',
    '   ● https://docs.djangoproject.com/',
    '2) OpenAI API 문서 (심화 기능용)',
    '   ● https://platform.openai.com/docs/',
    '3) Upstage API 문서 (심화 기능용)',
    '   ● https://console.upstage.ai/docs/getting-started',
]
for i,r in enumerate(refs,3):
    rh(ws6,i,16)
    is_link = '●' in r
    merge_write(ws6,i,1,i,3,r, size=10,
                color='1155CC' if is_link else '000000',
                italic=is_link)

rh(ws6,10,20)
merge_write(ws6,10,1,10,3,'1.6 프로젝트 결과', bold=True, size=13, align_v='bottom')

results = [
    '최종적으로 제출해야 할 항목은 아래와 같다',
    '◼ 산출물과 제출',
    '1) 구현 소스 코드',
    '   ◆ Django 프로젝트 전체 소스 코드',
    '2) README.md',
    '   ◆ 구현 기능 설명, 학습 내용, 느낀 점 포함',
    '3) 위 내용을 모두 포함하여 GitLab에 업로드한다.',
    '   ◆ GitLab 프로젝트 이름은 프로젝트 번호 + pjt 형식으로 지정한다 (04_pjt)',
]
for i,res in enumerate(results,11):
    rh(ws6,i,16)
    merge_write(ws6,i,1,i,3,res, size=10)

rh(ws6,20,20)
merge_write(ws6,20,1,20,3,'- 以上 -', bold=True, size=10, align_h='center')

# ── 저장 ──────────────────────────────────────────────
wb.save('통합 문서1.xlsx')
print("✅ 통합 문서1.xlsx 저장 완료! (총 6개 시트)")
print("   시트 구성: 표지 | 목차 | 개요/목표/준비사항 | 요구사항 | DB스키마 | 참고자료/결과")
