# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

word = input()
cnt = 0
lst =['a','e','i','o','u'] 
for i in word :
    for t in lst : 
        if i == t :
            cnt += 1
print(cnt)

# count = 0
# for char in word :
#     if char in 'aeiou': # ㅇㅁㅇ!!!!
#         count += 1
# print(count)