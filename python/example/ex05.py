# 주어진 숫자의 평균을 구하는 코드를 작성하시오.
# sum(), len()  함수 사용 금지

numbers = [3, 10, 20]
k = 0
num = 0
i = 0   
for i in numbers :
    k += 1
    num += i
print(num/k)