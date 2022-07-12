dustlv = int(input())
if dustlv > 150 :
    if dustlv > 300 :
        print("실외활동을 자제하세요")
    else :
        print("매우나쁨")
elif dustlv > 80 :
    print("나쁨")
elif dustlv > 30 : 
    print("보통")
else :
    if dustlv <0 :
        print("음수값입니다")
    else :
        print("좋음")