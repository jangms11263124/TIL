
# 1. 각 섬을 연결하는 간선들을 만들자
# 2. MST 구성 (prim, kruskal)

def find_set(x):
    if x == parents[x]:  # 대표자 발견했다면 종료
        return x

    # 경로 압축 코드
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:  # 이미 같은 집합이면 병합 X
        return False

    parents[ry] = rx  # 병합
    return True


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    # 1. 간선들 정보를 모두 저장
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            # x 좌표차이 ** 2 + y 좌표차이 ** 2 * 세율
            cost = ((x_list[i] - x_list[j]) ** 2 +
                    (y_list[i] - y_list[j]) ** 2) * tax

            edges.append((i, j, cost))

    # 2. 가중치 기준 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    # 3. 싸이클 검사하면서, 앞에서부터 간선들을 선택
    # --> 언제까지? MST 완성 (N-1 개 선택까지)
    parents = [i for i in range(N)]  # make-set

    cnt = 0
    min_cost = 0
    for u, v, w in edges:
        # if find_set(u) != find_set(v):  # 같은 집합이 아니라면
        #     union(u, v)
        #
        #     min_cost += w
        #     cnt += 1
        #
        # if cnt == N - 1:
        #     break

        if union(u, v):
            min_cost += w
            cnt += 1

        if cnt == N - 1:
            break

    print(f'#{tc} {min_cost:.0f}')

