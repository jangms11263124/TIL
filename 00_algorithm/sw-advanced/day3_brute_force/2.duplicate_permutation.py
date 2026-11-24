# 중복 순열
# [0, 1, 2] 3개의 카드가 존재 (2개를 뽑는 모든 경우)

# 기저조건: 2개의 카드를 모두 뽑았을 경우
#  - 시작: 0개의 카드를 고른 상태부터 시작
# 다음 재귀 호출: 카드 3개 중 하나를 선택

path = []


def recur(cnt):
    if cnt == 2:
        print(path)
        return

    # 한 번의 선택에서 3가지 경우의 수
    for i in range(3):
        path.append(i)  # 해당 숫자를 경로에 추가
        recur(cnt + 1)
        path.pop()      # 숫자를 뽑은 적이 없도록 초기화

    # # 0을 선택
    # path.append(0)
    # recur(cnt + 1)
    # path.pop()
    #
    # # 1을 선택
    # path.append(1)
    # recur(cnt + 1)
    # path.pop()
    #
    # # 2를 선택
    # path.append(2)
    # recur(cnt + 1)
    # path.pop()


recur(0)

# [심화] 경로를 전역변수 쓰지 않고 하는 방법
# - 경로를 누적하면서 파라미터로 전달한다.
def recur2(cnt, p):
    if cnt == 2:
        print(*p)
        return

    for i in range(3):
        recur2(cnt + 1, p + [i])


recur2(0, [])






