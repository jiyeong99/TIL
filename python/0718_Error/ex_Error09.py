# 아래 코드는 과일의 개수를 구하는 논리적 오류가 있는 코드의 일부분 입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        # 이렇게 되면 key-value쌍을 추가하는게 아니라 요소값이 하나뿐인 딕셔너리 한개를 계속 만들게 됩니다.
        # 그래서 결과값이 마지막 요소인 Salal berry가 되었습니다.
        # furit_count에 fruit가 없을 때, fruit key : 1이 추가되도록 문장을 고쳐줍니다.
        # fruit_count = {fruit: 1}
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)
