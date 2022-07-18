# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

number = 22020718
cnt = 0
while number > 0 or number <0 :
    number = number // 10
    # print(number)
    cnt += 1
print(cnt)
# print(len(number))

# TypeError: object of type 'int' has no len()
# int값은 len() 메소드를 사용하지 않습니다.