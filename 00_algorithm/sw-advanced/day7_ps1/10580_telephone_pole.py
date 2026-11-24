import sys
sys.stdin = open("input.txt", "r")

# 전봇대
# 전선 N개
# - 교차점 발생
# - 교차점의 개수를 count

# 교차점 발생 규칙
# 새로운 선이
# 1. 기존의 선보다 시작점은 높고, 도착점은 낮다
# 2. 기존의 선보다 시작점은 낮고, 도착점은 높다
# 새로운 선이 들어오면, 기존의 모든 선들과 비교
# -> 완전 탐색
#   - 시간복잡도 - O(N^2) , 연산 횟수 - 1 + 2 + 3 + ... + N - 1 (약 50만 번)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    wires = []  # 기존선들을 저장할 리스트
    answer = 0  # 교차점의 수

    for _ in range(N):
        start, end = map(int, input().split())

        # 기존의 모든 선들과 시작점, 도착점을 비교
        for prev_start, prev_end in wires:
            # 1. 기존의 선보다 시작점은 높고, 도착점은 낮다
            if start > prev_start and end < prev_end:
                answer += 1

            # 2. 기존의 선보다 시작점은 낮고, 도착점은 높다
            if start < prev_start and end > prev_end:
                answer += 1

        # 기존 목록에 start, end 를 추가
        wires.append((start, end))

    print(f'#{tc} {answer}')
