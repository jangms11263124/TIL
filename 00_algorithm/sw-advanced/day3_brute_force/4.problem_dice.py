# 주사위 3개를 던져서 합이 10이하인 케이스의 수

# 상태 공간 트리
# - 주사위 3개 -> depth: 3
# - branch 수 : 1~6숫자 -> 6

result = 0
path = []

def recur(cnt):
    global result

    if cnt == 3:
        # 경로의 합이 10 이하라면
        if sum(path) <= 10:
            print(*path)
            result += 1
        return

    for num in range(1, 7):
        path.append(num)
        recur(cnt + 1)
        path.pop()

recur(0)


print("--------------------- 심화")

# [심화 버전]

result2 = 0
def recur2(cnt, total):
    global result2

    # 이미 10을 넘었으면, 이 케이스는 더 이상 볼 필요없다
    # - [심화]백트래킹의 원리
    if total > 10:
        return

    if cnt == 3:
        # 경로의 합이 10 이하라면
        if total <= 10:
            result2 += 1
        return

    for num in range(1, 7):
        recur2(cnt + 1, total + num)


recur2(0, 0)
print(f"10이하인 개수 = {result2}")
