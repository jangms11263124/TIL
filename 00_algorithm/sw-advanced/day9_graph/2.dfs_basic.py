import sys
sys.stdin = open("input.txt", "r")


def dfs(node):
    print(node, end=' ')
    # 다음 재귀 호출
    # - node 에서 갈 수 있는 모든 노드를 확인 (graph[node])
    # - 이미 방문한 노드라면 continue
    # - 방문하지 않았다면 방문처리 후 이동
    for next_node in graph[node]:
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)


V, E = map(int, input().split())

# 인접 리스트 (연결된 정보만 저장)
graph = [[] for _ in range(V)]
visited = [0] * V  # 방문 여부 기록
visited[0] = 1

for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)  # 양방향

dfs(0)