# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number

# 리스트의 개수를 세는 count가 for문 바깥에 있습니다.
# 집어넣어줍니다.
# count += 1
    count += 1
# print(total // count)
# '//' 연산자는 몫을 버리고 나머지만 구하는 연산자 입니다.
# 몫과 나머지를 전부 계산하는 '/'를 사용해줍니다.
print(total/count)
