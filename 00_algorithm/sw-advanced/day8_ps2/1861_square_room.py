import sys
sys.stdin = open("square_room_input.txt", "r")

# 어떻게 이런 아이디어를 생각하게 될까 ?
# 1. 완전 탐색 (DFS, BFS) 로 설계 -> 시간 초과 위험성
# 2. 이차원 리스트 한 번 반복하고나면 얻을 수 있는 정보는 뭐가 있을까?
#    - 상하좌우에 해당 좌표에서 이동할 수 있는 지 없는 지
#    - 저장된 숫자가 모두 다르구나
#      -> 일차원 리스트에 모두 저장하자!

# 설계
# 1. 현재 숫자 위치 기준
# - 상하좌우에 이동 가능하면 visited[num] = 1 / 0 을 저장
# 2. 연속된 1의 개수가 가장 긴 곳을 찾자

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1번 ~ N*N번 까지 이동 가능 여부
    visited = [0] * (N * N + 1)

    # 1. 현재 숫자 위치 기준
    # - 상하좌우에 이동 가능하면 visited[num] = 1 / 0 을 저장
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                # 범위 밖 체크
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                # 정확히 1 크다면 이동 가능
                if arr[ny][nx] == arr[y][x] + 1:
                    num = arr[y][x]
                    visited[num] = 1
                    break  # 다른 방향엔 그런 숫자가 없다

    # 2. 연속된 1의 개수가 가장 긴 곳을 찾자
    max_cnt = 0     # 정답
    cnt = 0         # 몇 개가 연속되고 있는지?
    start = 0       # 숫자를 세기 시작한 번호

    for i in range(1, N * N + 1):
        if visited[i] == 1:
            cnt += 1
        else:  # 0을 만나면 실제 계산
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt
            cnt = 0

    print(f"#{tc} {start} {max_cnt + 1}")

