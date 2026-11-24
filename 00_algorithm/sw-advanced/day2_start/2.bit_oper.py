secret_code = 1004

print(7070 ^ secret_code)
print(6258 ^ secret_code)  # 원래 숫자로 되돌아온다.

# --------------------------
# 비트 연산 응용

# 1. 1 << n -> 2 ^ n 을 구할 수 있다.
# - 부분 집합의 수를 바로 계산할 수 있다.
arr = [7, 1, 3, 5]

print(f"부분 집합의 수 : {1 << len(arr)}개")

# 2. 전체 부분 집합을 구할 수 있다.
# i = 부분집합 번호
for i in range(1 << len(arr)):
    print(f"{i}번 째 부분집합: ", end=' ')
    subset = []
    # 각 자리수를 모두 확인
    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            print(arr[idx], end=' ')

    print()

# 3. [부분 집합 예시] 합이 10인 부분집합만 구해라
arr = [1, 2, 3, 4, 5, 6]
for i in range(1 << len(arr)):
    subset = []  # 여기에 각 부분집합을 저장
    total = 0

    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]

    if total == 10:
        print(f'합이 10인 부분집합 : {subset}')

