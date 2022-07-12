# 1부터 n까지의 곱을 구하여 출력하는 코드를 
# 1) while 문 2) for 문으로 각각 작성하시오.

# 1) while

# n = int(input())
# m = 0
# k = 1
# while m < n :
#     m += 1
#     k = k * m
# print(k)

# 2) for
n = int(input())
m = 0
k = 1
for m in range(n) :
    m += 1
    k = k * m
print(k)