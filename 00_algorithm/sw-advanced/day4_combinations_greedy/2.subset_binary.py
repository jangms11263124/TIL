arr = [1, 2, 3, 4]
n = len(arr)

def get_subset1():
    # 1. 0 ~ 부분 집합의 수 만큼 반복
    # - i: 부분집합의 번호
    for i in range(1 << n):
        # i를 이진수로 생각하고, 각 자리 수를 비교
        for idx in range(n):
            if i & (1 << idx):
                print(arr[idx], end=' ')
        print()

get_subset1()

