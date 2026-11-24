path = []


def recur(cnt):
    if cnt == 2:
        print(path)
        return

    # 한 번의 선택에서 3가지 경우의 수
    for i in range(3):
        # [주의!!!!!!!!] in 은 O(N) 이라서 너무 느리다! 시간초과 가능성이 너무 높다.
        if i in path:  # 이미 뽑은 숫자라면 다음 숫자를 고려하자
            continue

        path.append(i)
        recur(cnt + 1)
        path.pop()

recur(0)

# --------------------- 중복없애기

path = []
N = 7
used = [0] * N  # N 개의 종류가 있을 경우 N개 만큼 만든다.

def recur2(cnt):
    if cnt == 3:
        print(*path)
        return

    for i in range(1, 7):
        if used[i]:     # 이미 i 를 사용한 적이 있다면
            continue

        used[i] = 1     # 방문처리
        path.append(i)
        recur2(cnt + 1)
        path.pop()
        used[i] = 0     # 방문기록 초기화


recur2(0)







