# 1부터 사용자가 입력한 양의 정수까지
# 총합을 구하는 코드를 작성하시오
# 1. n을 0부터 1개씩 증가시킨 수를 total에 저장 한 후
# 2. 기존의 n과 total을 더한다.

n = 0
total = 0
user_input = int(input())

while n < user_input :
    n = n + 1 # n += 1
    total = n + total # total += n
print(total)
