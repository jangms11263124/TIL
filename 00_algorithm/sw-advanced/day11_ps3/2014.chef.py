import sys
sys.stdin = open("input3.txt", "r")


# 실제 시너지 계산
def cal_snergy(li):
    total = 0

    # 재료를 두 개씩 선택해서 모든 시너지 합산
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            a, b = li[i], li[j]
            total += arr[a][b] + arr[b][a]

    return total


# visited 를 보고 1이면 A_list 에 추가 / 0이면 B_list 에 추가
def get_snergy():
    A_list, B_list = [], []
    for i in range(N):
        if visited[i]:
            A_list.append(i)
        else:
            B_list.append(i)

    return cal_snergy(A_list), cal_snergy(B_list)


# 종료조건: 절반의 재료를 선택했을 때 종료 / 시너지 계산
# branch: 모든 재료(N)
def recur(cnt, prev):
    global min_answer

    if cnt == N//2:
        # 시너지 계산
        a_total, b_total = get_snergy()
        min_answer = min(min_answer, abs(a_total - b_total))
        return

    for food_number in range(prev + 1, N):
        if visited[food_number]:
            continue

        visited[food_number] = 1
        recur(cnt + 1, food_number)
        visited[food_number] = 0  # 선택 정보 초기화


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N  # 0 이면 B 음식, 1이면 A 음식에 투입된다.
    min_answer = 21e8
    recur(0, 0)
    print(f"#{tc} {min_answer}")
