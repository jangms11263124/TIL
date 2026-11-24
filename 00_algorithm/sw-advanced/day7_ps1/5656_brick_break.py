import sys
sys.stdin = open("input.txt", "r")

# 벽돌깨기
# 1. 최소 벽돌
# - 현재 벽돌이 다 깨지면 더 이상 할 필요 없다 (현재 벽돌 수를 관리)

# 2. N번의 구슬을 쏘자
# - 모든 케이스를 보아야 한다 (0000 ~ 11 11 11 11)
# - 한 번 쏘았을 때
#   - 연쇄 작용 (bfs)
#     - 델타 배열
#   - 빈칸 메우기
# - 연쇄작용하면 원본 배열이 수정될 수 있다
#   1. 원본 배열을 저장해두고, 수정 후 원상복구하자
#   2. 원본 배열을 복사해서 복사된 배열을 수정하고 다음 재귀로 전달하자

from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# depth: 4
# branch: 12 (0~11 번째 열에 쏜다)
def recur(cnt, remain_blocks, now_arr):
    global min_answer

    if cnt == N or remain_blocks == 0:
        min_answer = min(min_answer, remain_blocks)
        return

    # 모든 열에 구슬을 쏴본다
    for col in range(W):
        # 연쇄 작용
        # - col 에 구슬을 쏘기 전 상태를 복사
        #   - [주의] 얕은 복사 주의! 깊은 복사로 해주어야 한다.
        # - 복사된 리스트의 col 자리에 구슬을 떨군다
        copy_arr = [row[:] for row in now_arr]

        # 폭발이 시작되는 row 를 찾아야한다
        row = -1
        for r in range(H):
            if copy_arr[r][col]:
                row = r
                break

        # 벽돌이 없는 열은 검사하지 않는다.
        if row == -1:
            continue

        # 해당 row, col 의 숫자부터 시작해서 bfs
        # - 좌표 + 해당 벽돌의 숫자
        q = deque([(row, col, copy_arr[row][col])])
        now_remains = remain_blocks - 1  # 남아있는 벽돌 수
        copy_arr[row][col] = 0  # 구슬이 처음 만나는 벽돌 깨고 시작

        # 주변 벽돌을 파괴
        while q:
            r, c, p = q.popleft()

            for k in range(1, p):
                for i in range(4):
                    nr = r + (dy[i] * k)
                    nc = c + (dx[i] * k)

                    # 범위 밖이면 통과
                    if nr < 0 or nr >= H or nc < 0 or nc >= W:
                        continue

                    # 벽돌이 없으면 통과
                    if copy_arr[nr][nc] == 0:
                        continue

                    q.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0
                    now_remains -= 1

        # 빈칸 메우기
        for c in range(W):
            idx = H - 1
            for r in range(H - 1, -1, -1):
                if copy_arr[r][c]:  # 벽돌이 있다면
                    copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        # 다음 구슬로 이동
        recur(cnt + 1, now_remains, copy_arr)


T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_answer = 1e9  # 최소 벽돌 수 (정답)

    # 현재 블록 수 계산
    blocks = 0  # 현재 블록 수
    for i in range(H):
        for j in range(W):
            if arr[i][j]:
                blocks += 1

    recur(0, blocks, arr)
    print(f'#{tc} {min_answer}')
