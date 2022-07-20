import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    n = map(int, input().split())
    result = 0
    for i in n:
        if i % 2 == 1:
            result += i
    print('#%d %d'%(test_case, result))



