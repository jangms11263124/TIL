import sys
sys.stdin = open("input.txt", "r")

from collections import deque


def bfs(start_node):
    # dq: 후보 대기열 (다음에 방문해야 할 노드들)
    dq = deque([start_node])  # 시작점 deque 에 넣기

    while dq:
        now = dq.popleft()

        print(now, end=' ')

        # 1. now 에서 갈 수 있는 노드들을 모두 검사
        # 2. 방문하지 않았다면 방문처리 + queue 에 넣기
        for next_node in graph[now]:
            if visited[next_node]:
                continue

            visited[next_node] = 1  # 방문처리는 여기서 해주어야 한다.
            dq.append(next_node)


V, E = map(int, input().split())

# 인접 리스트 (연결된 정보만 저장)
graph = [[] for _ in range(V)]
visited = [0] * V  # 방문 여부 기록
visited[0] = 1

for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)  # 양방향

bfs(0)