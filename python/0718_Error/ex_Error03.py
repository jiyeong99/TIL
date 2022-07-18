# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# numbers = input().split()
numbers = list(map(int,input().split()))
print(sum(numbers))


# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# input은 입력값을 문자열로 받는 함수이고, sum은 iterable한 int값들을 받는 함수이기 때문에 생긴 오류
# numbers를 int값을 받는 list로 선언해준다.