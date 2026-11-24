arr = [7, 4, 2, 9, 11, 23, 19]

# [주의!] 이진 검색은 항상 정렬된 데이터에 적용
arr.sort()  # 2, 4, 7, 9, 11, 19, 23


def binary_search_while(target):
    left = 0                # 검색 시작점
    right = len(arr) - 1    # 검색 끝점
    cnt = 0                 # 검색 횟수 추가

    # 교차가 되는 순간이 탐색 못한 순간
    while left <= right:
        mid = (left + right) // 2
        cnt += 1

        # 정답을 찾으면 종료
        if arr[mid] == target:
            return mid, cnt

        # arr[mid] 가 target 보다 더 큰 경우 (target 이 왼쪽에 위치)
        # - 왼쪽을 탐색
        if target < arr[mid]:
            right = mid - 1
        # arr[mid] 가 target 보다 작은 경우 (target 이 오른쪽에 위치)
        # - 오른쪽을 탐색
        else:
            left = mid + 1

    return -1, cnt

targets = [9, 2, 20]

for target in targets:
    result = binary_search_while(target)
    if result == -1:
        print(f'{target}은 배열에 없습니다')
    else:
        print(f'{target}은 {result}위치에 있습니다.')


# ----------------------------
# [참고] 이진 검색 재귀 호출
def binary_search_recur(left, right, target):
    # left, right 를 작업 영역으로 검색
    # left <= right 만족하면 반복
    if left > right:
        return -1

    mid = (left + right) // 2
    # 검색하면 종료
    if target == arr[mid]:
        return mid

    # 한 번 할 때마다 left 와 right 를 mid 기준으로 이동시켜 주면서 진행
    # 왼쪽을 봐야한다
    if target < arr[mid]:
        return binary_search_recur(left, mid - 1, target)
    # 오른쪽을 봐야한다.
    else:
        return binary_search_recur(mid + 1, right, target)