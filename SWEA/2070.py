a, b = map(int, input().split())
if a > b :
    p = ">"
elif a < b :
    p = "<"
else :
    p = "="
print('#%d %s'%(test_case, p))