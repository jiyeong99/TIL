# 절댓값 계산기

num = -10

## 조건은 그대로
# 1. 양수면 그대로
if num >= 0:
    value = num

# 2. 음수면 - 붙여서
else:
    value = -num
print(num, value)

# print할 필요가 없을 때 이렇게 사용 가능
value = num if num >= 0 else -num

# 실습문제
