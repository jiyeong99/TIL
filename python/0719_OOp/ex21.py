number = 1234
sum = 0

def cnt(number):
    c = 0
    while number != 0:
        number //= 10
        c += 1
    return c

c = cnt(number) - 1

while number > 0:
    num = number % 10
    number //= 10
    num = num*10**c
    c -= 1
    sum += num
print(sum)