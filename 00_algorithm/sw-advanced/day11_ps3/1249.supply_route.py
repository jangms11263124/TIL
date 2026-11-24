import sys
sys.stdin = open("input2.txt", "r")

from heapq import heappop, heappush

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dijkstra():
    # 누적거리, y, x
    pq = [(0, 0, 0)]
    # 최단거리를 저장할 2차원 리스트
    dists = [[float('inf')] * N for _ in range(N)]
    dists[0][0] = 0

    while pq:
        dist, y, x = heappop(pq)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위 밖이면 continue
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            # 누적거리 계산
            # - 누적거리가 기존보다 크거나 같으면 continue
            new_dist = dist + graph[ny][nx]

            if dists[ny][nx] <= new_dist:
                continue

            # - dists 갱신
            # - pq 에 저장
            dists[ny][nx] = new_dist
            heappush(pq, (new_dist, ny, nx))

    return dists[N-1][N-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().strip())) for _ in range(N)]

    result = dijkstra()
    print(f"#{tc} {result}")