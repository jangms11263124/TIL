
# 2. 병합하는 과정 (이때, 정렬하면서 병합)
# - 왼쪽, 오른쪽 리스트 중 작은 원소부터 정답 리스트에 추가하자
def merge(left, right):
    # 두 리스트를 합한 크기만큼 나온다
    result = [0] * (len(left) + len(right))
    l = r = 0       # 현재 바라보고 있는 인덱스

    # 두 리스트에서 비교할 대상이 남을 때 까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 남은 데이터들을 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


# 1. 분할하는 과정
# - depth: 리스트의 길이가 1이 되면 끝
# - branch: 왼쪽과 오른쪽으로 리스트를 분할 (2개)
def merge_sort(li):
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left = li[:mid]     # 왼쪽 절반 리스트
    right = li[mid:]    # 오른쪽 절반 리스트

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    merge_list = merge(left_list, right_list)
    return merge_list


arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)
