import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    n = map(int, input().split())
    max = 0
    for i in n:
        if max < i :
            max = i        
    print('#%d %d'%(test_case, max))
