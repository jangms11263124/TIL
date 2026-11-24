# 재귀함수: 자기자신을 호출하는 함수
# - 끝나는 지점이 필요하구나!
#   - 1. 시작
#   - 2. 끝
#   - 3. 누적된 값

# 0 ~ 10을 출력
# - 0부터 시작
# - 10에서 종료 (10보다 커지면 종료)
# - 다음 재귀 호출: num을 1씩 증가
def recur(num):
    if num > 3:
        return

    print(num, end=' ')
    recur(num + 1)

print("recur 기본")
recur(0)
print()
print()


# 0 ~ 10을 출력하고, 다시 10 ~ 0을 출력하려면 ?
# 0 1 2 3 ... 9 10 10 9 8 7 ... 1
def recur1(num):
    if num > 3:
        return

    print(num, end=' ')
    recur1(num + 1)
    print(num, end=' ')


print("되돌아오면서 출력하기")
recur1(0)
print()
print()


# 상태 공간 트리의
# - 높이 : 기저조건 (종료조건)
# - 가지의 수 : 재귀호출 수
#   - 가지의 수가 많다면 반복문으로 만들 수 있다
# - 핵심
#   - 1. 상태공간 트리 그리기
#   - 2. 트리를 보고 코드로 구현하기
def recur3(num):
    # 트리의 높이와 같다
    if num > 3:
        return

    # 가지의 수 만큼 재귀호출 코드가 돌아간다.
    for i in range(1, 7):
        recur3(num + 1)





