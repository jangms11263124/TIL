import sys
sys.stdin = open("input1.txt", "r")

from heapq import heappop, heappush


def prim():
    # (비용, 노드) 형태로 저장
    pq = [(0, 0)]  # 0번 노드부터 MST 구성
    visited = [0] * N  # 방문 여부 기록
    min_cost = 0

    dists = [float('inf')] * N  # 현재까지의 최소 비용을 저장
    dists[0] = 0

    while pq:
        cost, node = heappop(pq)

        if visited[node]:
            continue

        # node 로 가는 길을 확정
        visited[node] = 1
        min_cost += cost

        # 모든 섬에 다 연결될 수 있다
        for next_node in range(N):
            if visited[next_node]:
                continue

            # node -> next_node 거리 계산
            # ((x좌표 차이 ** 2) + (y좌표 차이 ** 2)) * tax
            next_cost = ((x_list[next_node] - x_list[node]) ** 2 +
                         (y_list[next_node] - y_list[node]) ** 2) * tax

            # 더 작은 비용으로 next_node로 갈 수 있을 때만 pq에 넣자!
            if next_cost < dists[next_node]:
                dists[next_node] = next_cost
                heappush(pq, (next_cost, next_node))

    return round(min_cost)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    min_result = prim()
    print(f"#{tc} {min_result}")

