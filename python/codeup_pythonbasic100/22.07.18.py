# 6047
# 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10

# a,b = map(int, input().split())
# print(a<<b)
#################################################
# 6048
# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, 
# a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

# a, b = map(int, input().split())
# if a < b:
#     print('True')
# else : print('False')
#################################################
# 6049
# 두 정수(a, b)를 입력받아
# a와 b의 값이 같으면 True 를, 
# 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

# a, b = map(int, input().split())
# if a == b :
#     print('True')
# else : print('False')
#################################################
# 6050
# 두 정수(a, b)를 입력받아
# b의 값이 a의 값 보다 크거나 같으면 True 를, 
# 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

# a, b = map(int, input().split())
# if a <= b :
#     print('True')
# else : print('False')

#################################################
# 6051
# 두 정수(a, b)를 입력받아
# a의 값이 b의 값과 서로 다르면 True 를, 
# 같으면 False 를 출력하는 프로그램을 작성해보자.

# a, b = map(int, input().split())
# if a != b :
#     print('True')
# else : print('False')
#################################################
# 6052
# 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.

# num = int(input())
# if num == 0:
#     print('False')
# else : print('True')
###############################################
# 6053
# 정수값이 입력될 때,
# 그 불 값을 반대로 출력하는 프로그램을 작성해보자.

# a = bool(int(input()))
# print(not a)
###############################################
# 6054
# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

# a, b = input().split()
# print(bool(int(a)) and bool(int(b)))
##############################################3
# 6055
# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만
#  True 를 출력하는 프로그램을 작성해보자.

# a, b = input().split()
# print(bool(int(a)) or bool(int(b)))

##############################################
# 6056
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

# a, b = map(int, input().split())
# c = bool(a)
# d = bool(b)
# print((c and (not d)) or ((not c) and d))

##############################################
# 6057
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 
# 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.

# a, b = map(int, input().split())
# c = bool(a)
# d = bool(b)
# print(((not c) and (not d)) or (c and d))

##############################################
# 6058
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 
# True 를 출력하는 프로그램을 작성해보자.

# a, b = map(int, input().split())
# c = bool(a)
# d = bool(b)
# print(not(c or d))
##############################################
# 6059
# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
# n = int(input())
# print(~n)

##############################################
# 6060
# 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.

# a, b = map(int, input().split())
# print(a & b)
#########################3333333333##########3
# 6063
# 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

# a, b = map(int, input().split())
# c = (a if (a>b) else b)
# print(int(c))
##############################################
# 6064

# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

# a, b, c = map(int, input().split())
# d = (a if a<b else b) if((a if a<b else b)< c) else c
# print(int(d))
##############################################
# 6065
# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.
# a, b, c = map(int, input().split())
# if a % 2 == 0:
#     print(a)
# if b % 2 == 0:
#     print(b)
# if c % 2 == 0:
#     print(c)
##############################################
# 6066
# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.
# a, b, c = map(int, input().split())
# if a % 2 == 0:
#     print('even')
# else : print('odd')

# if b % 2 == 0:
#     print('even')
# else : print('odd')

# if c % 2 == 0:
#     print('even')
# else : print('odd')
##############################################
# 6067
# 0이 아닌 정수 1개가 입력되었을 때, 
# 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D
# 를 출력한다.

# a = int(input())
# if a < 0 and a % 2 == 0:
#     print('A')
# elif a < 0 and a % 2 != 0:
#     print('B')
# elif a > 0 and a % 2 == 0:
#     print('C')
# else : print('D')

##############################################
# 6068
# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.
# a = int(input())
# if a < 40 :
#     print('D')
# elif a >= 40 and a < 70 :
#     print('C')
# elif a >= 70 and a < 90 :
#     print('B')
# else : print('A')
##############################################
# 6069
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?
# a = input()
# if a == 'A':
#     print('best!!!')
# elif a == 'B':
#     print('good!!')
# elif a == 'C':
#     print('run!')
# elif a == 'D':
#     print('slowly~')
# else : print('what?')
##############################################
# 6070
# 월이 입력될 때 계절 이름이 출력되도록 해보자.
# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
# #   9, 10, 11 : fall
# s = int(input())
# if s // 3 == 1 and s // 6 != 1:
#     print('spring')
# elif s // 6 == 1 and s // 9 != 1:
#     print('summer')
# elif s // 9 == 1 and s // 12 != 1 :
#     print('fall')
# else : print('winter')
##############################################
# 6071

##############################################


##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################