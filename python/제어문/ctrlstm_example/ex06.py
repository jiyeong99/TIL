# 주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
# max() 함수 사용 금지

# numbers = [0, 100, 20]
# numbers = [0, 20, 100, 50, -60, 50, 100] # 50
# numbers = [0, 100, 10] # 0
# numbers = [-10, -100, -30] # -30
i = 0
M = numbers[0]
for i in numbers :
    if i > M :
        M = i
    else : continue
print(M)