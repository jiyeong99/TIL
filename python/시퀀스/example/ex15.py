# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지

word = input()
k = 0
# if 'a' in word:
#     for i in word :
#         if i == 'a':
#             print('word[%d]'%k)
#             break
#         k += 1 
# else : print('-1')

for idx in range(len(word)):
    print(idx, word[idx])
    if word[idx] == 'a':
        print(idx)
        break
    # for문을 다 돌았다ㅡㄴㄴ ㅡㄸㅅ은
    # 한번도 break에 안걸렸다
    # 즉, a는 없었다.
    else : print(-1)
