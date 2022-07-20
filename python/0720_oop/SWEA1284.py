p,q,r,s,w = map(int, input().split())
a = w*p
b = q if w <= r else q+s*(w-r)
if a < b:
    print(a)
else : print(b)