import sys
sys.stdin = open("grid_number_connection_input.txt", "r")

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# DFS 버전
# 종료조건: 숫자가 7자리가 되면 종료
# 가지의 수 : 4가지 (상하좌우)
def recur(y, x, number):
    if len(number) == 7:  # 7자리면 종료
        result.add(number)
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 밖 체크
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        recur(ny, nx, number + matrix[ny][nx])


T = int(input())

for tc in range(1, T + 1):
    # 숫자를 이어붙일거라 문자열로 입력
    matrix = [input().split() for _ in range(4)]
    result = set()

    # 특정 좌표로 부터 출발해서 7자리를 만들자!
    for sy in range(4):
        for sx in range(4):
            recur(sy, sx, matrix[sy][sx])

    print(f'#{tc} {len(result)}')
