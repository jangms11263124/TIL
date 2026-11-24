import sys
sys.stdin = open("mst_input.txt", "r")

# import heapq
from heapq import heappush, heappop


# 특정 정점 기준으로 시작
# - 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 간다
# --> 작은 노드를 먼저 꺼내기 위해 우선순위큐(heapq)를 활용한다
def prim(start_node):
    pq = [(0, start_node)]  # (가중치, 노드) 형태
    MST = [0] * V  # visited 와 동일하다
    min_weight = 0  # 최소 비용

    while pq:
        weight, node = heappop(pq)  # 가장 작은 가중치

        # 이미 방문한 노드라면 continue
        if MST[node]:
            continue

        # queue 에서 pop 될 때 MST 에 포함되는 게 확정!
        MST[node] = 1           # node 로 가는 최소 비용이 선택되었다
        min_weight += weight    # 누적합 추가

        for next_weight, next_node in graph[node]:
            # 이미 방문했으면 continue
            if MST[next_node]:
                continue

            # 원래 BFS 에서는 여기서 방문 처리  -> 최소 비용 문제에서는 여기서 하면 안된다!
            # --> 최소 비용이 보장이 안되기 때문에 안된다!
            heappush(pq, (next_weight, next_node))

    return min_weight



V, E = map(int, input().split())
graph = [[] for _ in range(V)]  # 인접 리스트

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))
    graph[end].append((weight, start))  # 양방향

result = prim(4)  # 출발 정점과 함께 시작
                # 출발 정점을 바꾸어도, 최소비용은 똑같다
                # 단, 그래프가 다르게 나올수는 있다.
print(f'최소 비용 = {result}')
