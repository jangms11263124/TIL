import sys
sys.stdin = open("input4.txt", "r")


# 종료조건: 첫 번째 숫자부터 시작, 숫자를 모두 고려하면 종료
# 가지의수: 최대 4개(사칙연산)
# 누적값 (현재 시점의 값과 다음 시점의 값은 무엇이어야 하는가?)
#   - 계산된 결과
#   - 남은 연산자의 수
def recur(cnt, total, plus, minus, mul, div):
    global min_result
    global max_result

    if cnt == N:
        # 최대, 최소 계산
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return
    
    # 덧셈
    if plus > 0:
        recur(cnt + 1, total + numbers[cnt], plus - 1, minus, mul, div)

    # 뺄셈
    if minus > 0:
        recur(cnt + 1, total - numbers[cnt], plus, minus - 1, mul, div)

    # 곱셈
    if mul > 0:
        recur(cnt + 1, total * numbers[cnt], plus, minus, mul - 1, div)

    # 나눗셈
    if div > 0:
        recur(cnt + 1, int(total / numbers[cnt]), plus, minus, mul, div - 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 덧셈, 뺄셈, 곱셈, 나눗셈
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_result, max_result = 21e8, -21e8

    # 첫 번째 숫자부터 시작하기 때문에, 첫 번째 숫자도 함께 전달
    recur(1, numbers[0], opers[0], opers[1], opers[2], opers[3])
    print(f"#{tc} {max_result - min_result}")
