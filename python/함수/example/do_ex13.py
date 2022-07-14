# 주어진 문자열 word가 주어질 때, 
# 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
word = 'apple'

# 2.pythonic
# print(word[::-1])
# print(''.join(reversed(word)))

# 3. ndex
for i in range(len(word)):
    print(i)
    print(word[len(word)-i-1],end='')
