# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
# print(chr(ord('a')-32))
word = 'banana'
WORD = []
for i in word :
    WORD.append(chr(ord(i)-32))
print(''.join(map(str,WORD)))