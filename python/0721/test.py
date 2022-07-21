n = int(input())
for i in str(n):
    print('f = %s'%i,type(i))
    if str(i) in '369':
        for r in i:
            print('s = %s'%r)