import sys
sys.stdin = open("swimming_pool_input.txt", "r")

# depth: 12 (12월을 모두 고려한 경우)
# branch: 4개 (1일, 1달, 3달, 1년)
def recur(month, total_cost):
    global min_answer

    if month > 12:
        min_answer = min(min_answer, total_cost)
        return

    # 현재 시점에서 1일권 vs 1달권 비교가 가능하니 조건문으로 적으면 더 효율적이다
    # if days[month] * cost_day < cost_month:
    #     # 1일 권으로 사는 경우
    #     recur(month + 1, total_cost + (days[month] * cost_day))
    # else:
    #     # 1달 권으로 사는 경우
    #     recur(month + 1, total_cost + cost_month)

    # 1일 권으로 사는 경우
    recur(month + 1, total_cost + (days[month] * cost_day))
    # 1달 권으로 사는 경우
    recur(month + 1, total_cost + cost_month)
    # 3달 권으로 사는 경우
    recur(month + 3, total_cost + cost_month3)


T = int(input())

for tc in range(1, T + 1):
    # 이용권 가격
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 12월의 이용 계획 (1번 index 부터 활용)
    days = [0] + list(map(int, input().split()))
    min_answer = 31 * 12 * 3000  # 최대 금액 (31일 * 12달 * 3000원)
    recur(1, 0)
    # 1년 권과 가격 비교
    min_answer = min(min_answer, cost_year)
    print(f'#{tc} {min_answer}')

