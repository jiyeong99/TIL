# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

# n = int(input())
# total = 0
# i = 0
# while i < n :
#     i += 1
#     total += i
# print(total)

n = int(input())
total = 0
for i in range(n) :
    i += 1
    total += i
print(total)