import sys
sys.stdin = open("input.txt", "r")

# 탈주범 검거
# 지도 (이차원 리스트)
# 지하터널
# - 터널들을 이동 (상하좌우)
#   - 델타배열 써야하는구나
# - 이동 못하는 경우들도 존재
#   - 현재 내 위치에서 뚫려있는 곳만 이동 가능
#   - 다음 위치의 입구가 뚫려있는 곳으로만 이동 가능
# - 시간 (L)
#   - 시간 내로 이동 가능한 위치의 개수
#
# ------------------- 설계
#
# 맨홀 뚜껑(y,x)으로 부터 시간 내로 갈 수 있는 모든 위치의 수
# - 특정 좌표로 부터 점점 넓혀나가는 그림
#   --> BFS 로 접근하자!
#
# - BFS 의 복잡도
#   - queue 에 얼마나 많은 데이터가 들어가는가 ?
#   - O(V + E)
#     - V: 정점의 수 / E: 간선의 수
#       - 정점의 수 = 최대 2,500개
#       - 간선의 수 = 2500 * 4(상하좌우) = 10,000개
#       -> 12,500 ==> 여유롭다.

# BFS 상세
# - 탐색 : 상하좌우
# - 이동이 불가능한 케이스
#   - [델타 배열 기본] 범위 밖으로 나가면 못감
#   - [방문 기록 기본] 이미 방문한 곳은 못감
#   - [0이면 못감]
#   - [문제 조건]
#     - 현재 내 위치에서 뚫려있는 곳만 이동 가능
#     - 다음 위치의 입구가 뚫려있는 곳으로만 이동 가능
#       -> 델타배열과 동일한 순서로 "이동 가능 여부를 기록"하면 좋다

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 터널들의 종류에 따라서, 이동 가능 여부
types = {
    # 상하좌우 순서
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}


def bfs(R, C):
    q = deque([(R, C)])
    visited[R][C] = 1

    while q:
        now_y, now_x = q.popleft()
        dirs = types[graph[now_y][now_x]]

        # 현재 좌표로부터 갈 수 있는 모든 노드를 확인
        # - 우리 문제에서는 상하좌우
        # - 이동이 가능한 다음 좌표만 q에 추가
        for dir in range(4):
            # i 방향이 안뚫리면 못감 -> 다음 방향을 보자
            if dirs[dir] == 0:
                continue

            ny = now_y + dy[dir]
            nx = now_x + dx[dir]

            # [델타 배열 기본] 범위 밖으로 나가면 못감
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            # [방문 기록 기본] 이미 방문한 곳은 못감
            if visited[ny][nx]:
                continue

            # [0이면 못감]
            if graph[ny][nx] == 0:
                continue

            # 다음 위치의 입구가 뚫려있는 곳으로만 이동 가능
            next_dirs = types[graph[ny][nx]]

            # 현재 상좌 -> next_dirs 가 하우가 안뚫리면 못감
            if dir % 2 == 0 and next_dirs[dir + 1] == 0:
                continue

            # 현재 하우 -> next_dirs 가 상좌가 안뚫리면 못감
            if dir % 2 == 1 and next_dirs[dir - 1] == 0:
                continue

            # L 시간을 넘어가면 안봐도 된다
            if visited[ny][nx] + 1 > L:
                continue
            
            # 시간을 + 1 누적하면서 이동
            visited[ny][nx] = visited[now_y][now_x] + 1
            q.append((ny, nx))


T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    bfs(R, C)

    cnt = 0
    # L 시간 내로 방문한 곳을 count
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')


