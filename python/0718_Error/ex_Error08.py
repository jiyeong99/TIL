# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

word = "HappyHacking"

count = 0

for char in word:
    # if char == "a" or "e" or "i" or "o" or "u":
    # >>> 12
    # 이렇게 되면 이 문장은 문자열하나를 조회할 때마다 cnt가 증가하게 됩니다.
    # 모음일 때만 cnt가 증가하도록 바꿉시다.
    # elif로 하나하나 조건을 만들어줘도 되지만 너무 길어지니 이렇게
    if char in "aeiou" :
        count += 1

print(count)