# 퀵 정렬 중 lomuto partition 을 활용한 코드입니다.
# i, j 가 hoare 와는 다르게 앞에서부터 함께 이동한다는 점을 이해해주시면 됩니다.
#  - hoare 와 동일하게 i 는 pivot 보다 큰 값을, j 는 작은 값을 찾아나갑니다.

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]


def lomuto_partition(left, right):
    pivot = arr[right]

    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(left, right):
    if left < right:
        pivot = lomuto_partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)
