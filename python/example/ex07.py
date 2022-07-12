# 주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
# min() 함수 사용 금지

numbers = [0, 100, 20]
i = 0
m = numbers[0]
for i in numbers :
    if i < m :
        m = i
    else : continue
print(m)