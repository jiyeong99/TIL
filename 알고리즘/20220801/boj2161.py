# queue
from collections import deque
n = 7
card = [i for i in range(1,n+1)]
drop = []
for i in card:
    if i % 2 != 0:
        drop.append(card.popleft())
    else : card.insert(-1,card[i])