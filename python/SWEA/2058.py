n = int(input())
k = 0
while n != 0:    
    c = n % 10
    n //= 10
    k += c
print(k)
    