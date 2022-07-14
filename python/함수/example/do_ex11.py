# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

def mult(n):
    
    print("\n%d 단"%n)
    i = 1
    for i in range(1,9): 
        k = n*i
        i+=1
        print("%d x %d = %d"%( n,i,k))
   

for n in range(1,10):
    mult(n)
    