# 3 시각 덧셈
# 시분으로 이루어진 두개의 시각을 받아 덧셈
# 시 h1,h2, 분 m1,m2를 받는데, 
# h1,h2의 합인 hours가 12를 넘어가면 12로 나눈 나머지를 반환,
# 분 두개의 합인 min이 60을 넘어가면 60으로 나눈 나머지를 반환하고 hours에 1 증가

import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):

    h1,m1,h2,m2 = map(int, input().split())
    if h1 + h2 >= 12:
        hours = (h1 + h2) % 12
    else : hours = h1 + h2
    if m1+m2 >= 60 :
        hours = hours + 1
        min = (m1+m2) % 60
    else : min = m1 + m2

    print('#%d %d %d'%(test_case, hours, min))
