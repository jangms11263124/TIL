# 그래프를 표현하는 두 가지 방식

import sys
sys.stdin = open("input.txt", "r")

V, E = map(int, input().split())

# 인접 행렬 (0, 1 로 연결 유무를 모두 저장)
# 노드의 수와 노드 번호에 따라 V or V+1 잘 확인하기
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1  # 양방향

for row in graph:
    print(row)


# 인접 리스트 (연결된 정보만 저장)
graph = [[] for _ in range(V)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)  # 양방향

print('--------------------')
for row in graph:
    print(row)

