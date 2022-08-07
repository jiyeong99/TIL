# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 2의 i제곱
n = int(input())
k = 1
for i in range(n+1):
    print(2**i,end=' ')
