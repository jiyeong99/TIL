import sys
sys.stdin = open('input.txt','r')
number = list(map(int, input().split()))
avg = sum(number)/len(number)
print("%d"%round(avg))
