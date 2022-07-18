# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
N = 10
answer = ()
for number in range(N + 1):
    l_answer = list(answer)
    l_answer.append(number * 2)
    answer = tuple(l_answer)
print(answer)

# AttributeError: 'tuple' object has no attribute 'append'
# tuple은 append메소드를 사용하지 않습니다.
# 튜플의 요소값은 변경이 불가하므로 list로 변환해서 변경해준 후 다시 tuple로 선언해줍니다.