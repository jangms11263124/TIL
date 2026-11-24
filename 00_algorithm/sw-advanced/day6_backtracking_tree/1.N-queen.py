
def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가 ?
    for i in range(row):
        if visited[i][col]:
            return True

    # 2. 좌상단 대각선에 놓은 적이 있는가 ? (\)
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return True

        i -= 1
        j -= 1

    # [참고] 두 가지 변수를 동시에 반복 --> zip 을 활용
    # for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
    #     if visited[i][j]:
    #         return True


    # 3. 우상단 대각선에 놓은 적이 있는가 ? (/)
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j]:
            return True

        i -= 1
        j += 1

    return False

# depth: 모든 행에 퀸을 놓았는가? (N개)
# branch: 모든 열에 퀸을 놓았는가? (N개)
def recur(row):
    global answer

    if row == N:
        answer += 1
        # print(*path)
        return

    for col in range(N):
        # 유망하지 않는 경우는 못 보도록 continue
        # - 가지치기
        if check(row, col):
            continue

        visited[row][col] = 1
        path.append(col)
        recur(row + 1)
        path.pop()
        visited[row][col] = 0


N = 4       # 판 크기
answer = 0  # 가능한 정답 수
path = []
# N * N 모든 위치의 방문 여부를 기록
visited = [[0] * N for _ in range(N)]
recur(0)
print(f'경우의 수 = {answer}')

# N값이 커지면 가지치기를 많이 해도 엄청 느리다!

# N = 20       # 판 크기
# answer = 0  # 가능한 정답 수
# path = []
# # N * N 모든 위치의 방문 여부를 기록
# visited = [[0] * N for _ in range(N)]
# recur(0)
# print(f'경우의 수 = {answer}')
