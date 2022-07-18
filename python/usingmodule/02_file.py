# 파일명, 어떤 모드로 열지,
# 인코딩을 설정
cnt = 0
with open('student.txt','r', encoding='utf-8') as f :
    # text = string type
    text = f.read()
    print(text)
    # string.split() => list type
    names = text.split()
    for name in names :
        # if name.startswith('김')
        # name : 첫번째 시행 - 김세환
        if name[0] == '김':
            cnt += 1
    print(cnt)
        
