# 상태를 나타내는 플래그들 (각 상태는 1비트를 사용)
WALK = 1 << 0    # 1번 비트: 걷기 상태
ATTACK = 1 << 1  # 2번 비트: 공격 상태
JUMP = 1 << 2    # 3번 비트: 점프 상태

# 현재 상태를 나타내는 변수 (초기 상태는 아무것도 하지 않음)
character_state = 0

# 상태 설정 함수 (비트 연산을 사용하여 상태를 추가)
def set_state(state, flag):
    return state | flag

# 상태 제거 함수 (비트 연산을 사용하여 상태를 제거)
def unset_state(state, flag):
    return state & ~flag

# 상태 확인 함수 (비트 연산을 사용하여 상태를 확인)
def is_state_active(state, flag):
    return state & flag != 0

# 1. 상태 설정: "걷기 중"과 "점프 중" 설정
character_state = set_state(character_state, WALK)
character_state = set_state(character_state, JUMP)

# 상태 확인: "걷기 중"인지, "점프 중"인지 확인
print("현재 캐릭터의 상태:")
if is_state_active(character_state, WALK):
    print("- 캐릭터는 걷고 있습니다.")
if is_state_active(character_state, JUMP):
    print("- 캐릭터는 점프 중입니다.")

# 2. 상태 변경: "공격 중" 추가
character_state = set_state(character_state, ATTACK)

# 상태 확인: "공격 중"인지 확인
print("\n상태 변경 후 캐릭터의 상태:")
if is_state_active(character_state, ATTACK):
    print("- 캐릭터는 공격 중입니다.")

# 3. 상태 제거: "점프 중" 상태를 제거
character_state = unset_state(character_state, JUMP)

# 상태 확인: "점프 중" 상태가 제거되었는지 확인
print("\n상태 제거 후 캐릭터의 상태:")
if is_state_active(character_state, JUMP):
    print("- 캐릭터는 점프 중입니다.")
else:
    print("- 캐릭터는 점프 중이지 않습니다.")
