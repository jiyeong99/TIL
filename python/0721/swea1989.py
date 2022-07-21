# 2
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    a= input().strip()
    if a == a[::-1] :
        r = 1
    else : r = 0
    print(a,a[::-1])
    print('#%d %d'%(test_case, r))

