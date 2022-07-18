# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요

# words = list(map(int, input().split()))
words = list(input().split())
print(words)

# ValueError: invalid literal for int() with base 10: 'im'
# int로 mapping해놓고 문자열을 입력해서 생긴 오류.
# 문자열을 입력받으려면 int로 mapping하면 안됩니다.
# input()은 기본적으로 문자열을 입력받으니 그냥 input만 씁니다.
