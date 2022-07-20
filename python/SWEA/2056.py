import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    y = input()
    def date(y):
        yr = int(y[:4])
        m = int(y[4:6])
        d = int(y[6:])
        result = '%04d/%02d/%02d'%(yr,m,d)
        if m > 12 or m <1:
            result = '-1'
        if m in [1,3,5,7,8,10,12]:
            if d < 1 or d > 31:
                result = '-1'
        if m in [4, 6, 9, 11]:
            if d < 1 or d > 30:
                result = '-1'
        if m == 2 :
            if d > 28 :
                result = '-1'
        return result
    print('#%d %s'%(test_case,date(y)))
