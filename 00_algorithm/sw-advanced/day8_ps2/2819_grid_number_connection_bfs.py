import sys
sys.stdin = open("grid_number_connection_input.txt", "r")

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx, start_number):
    q = deque([(sy, sx, start_number)])

    while q:
        y, x, number = q.popleft()

        # 현재 숫자가 7자리라면 상하좌우 체크 X
        if len(number) == 7:
            result.add(number)
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                continue

            q.append((ny, nx, number + matrix[ny][nx]))


T = int(input())

for tc in range(1, T + 1):
    # 숫자를 이어붙일거라 문자열로 입력
    matrix = [input().split() for _ in range(4)]
    result = set()

    # 특정 좌표로 부터 출발해서 7자리를 만들자!
    for sy in range(4):
        for sx in range(4):
            bfs(sy, sx, matrix[sy][sx])

    print(f'#{tc} {len(result)}')
