# 문자열 word가 주어질 때, Dictionary를 활용해서 
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.

# word = input()
# lst_word = []
# dic_word = {}

# for i in word :
#     lst_word.append(i)
# # print(lst_word)

# for i in word :
#     dic_word[i] = 0
# # print(dic_word)

# lst_dic_word = list(dic_word.keys())
# # print(lst_dic_word)

# for i in lst_word :
#     for t in lst_dic_word :
#         if i == t:
#             dic_word[t] = dic_word[t]+1

# print(dic_word)

word = 'banana'
result = {}
for char in word:
    result[char] = result.get(char, 0) + 1
print(result)

for key in result:
    print(key, result[key])

#     if char in result :
#         result[char] = 1
#     else : result[char] = result[char] + 1

# print(result)