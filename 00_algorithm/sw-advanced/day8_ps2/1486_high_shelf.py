import sys
sys.stdin = open("high_shelf_input.txt", "r")

# N 명의 점원을 다양하게 선택
# - R명 선택 기준이 X
#   - 부분집합 문제
#   - 집합에 포함 된다 or 안된다

# - 가지치기는 없을까? (유망하지 않는 후보)
#   - 이미 높이가 B 이상이다
#     - 어차피 쌓아봐야 정답에서 더 멀어진다
#   - 만약, 1 <= B <= S(점원들의 키의 합) 조건이 없었다면 ?
#     - 남은 인원을 모두 쌓아도 B 이상이 안되는 경우
#     -> B 까지 남은 높이를 같이 전달하면서 구현

# depth: N명의 점원을 검토 (N)
# branch: 집합에 현재 원소가 포함 O X (두 가지)
def recur(idx, total_height):
    global min_answer

    # 가지치기: 이미 높이가 B이상이면
    if total_height >= B:
        min_answer = min(min_answer, total_height)
        return

    if idx == N:
        return

    # idx 번 째 점원이 집합에 포함 되는 경우
    recur(idx + 1, total_height + heights[idx])

    # idx 번 째 점원이 집합에 포함 안되는 경우
    recur(idx + 1, total_height)


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_answer = 10000 * N  # 나올 수 있는 최대 범위
    recur(0, 0)
    print(f'#{tc} {min_answer - B}')


