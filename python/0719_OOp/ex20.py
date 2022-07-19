# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
import sys
sys.stdin = open('input.txt', 'r')
number = int(input())
sum = 0

while number > 0:
    num = number % 10
    number //= 10
    sum += num
print(sum)
    