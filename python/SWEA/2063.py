# import sys
# sys.stdin = open("input.txt", "r")
# T = int(input())
# print(T)
n = list(map(int, input().split()))
n.sort()
k = len(n)//2
print(n[k])
# print('#%d %d'%(test_case, result))
