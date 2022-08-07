# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 
# 최종 누적된 값을 구해보자.
n = int(input())
r = 0
for i in range(1,n+1):
    if i % 2 == 0:
        r = r - i
    else : r = r + i
print(r)