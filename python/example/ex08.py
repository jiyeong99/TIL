# 주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
# max() 함수 사용 금지

# 이건 꼼수
numbers = [0, 20, 200, 60, 80, 100, 900]

n = 0
M = numbers[0]
M_s = numbers[0]

# for i in numbers :
#     if i > M :
#         M = i
#     else : continue
# numbers.remove(M)

# for i in numbers :
#     if i > M_s :
#         M_s = i
#     else : continue
# print(M_s)
# numbers.append(M)
# print(numbers)

for n in numbers:
    if M < n:
        M_s = M
        M = n
    elif M_s > n and n > M :
        M_s = n
print(M_s)