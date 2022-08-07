import sys
from pprint import pprint
sys.stdin = open("77_input.txt")
T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split()) # 행,열
    grid = []
    for _ in range(n):
        temp = map(int,input().split())
        temp = list(temp)
        grid.append(temp)
    move = 0
    for x in range(m):  # 행순회, 아래서 부터
        for y in list(range(n))[::-1]:
            # print(x,y)
            if grid[y][x] == 1:
                while y+1 != n and grid[y+1][x] != 1: # 조건은 문제 없고..
                    grid[y][x] = 0
                    grid[y+1][x] = 1 
                    y+=1
                    # y순회를 한번 더 해야하는데 안돌아ㅠㅠㅠㅠ
                    # 전체적으로 y축 순회를 한번 더 안하고 있는데.
                    # 범위 문제인거같은데
                    # 아 강사님 코드에 y+= 1이 빠졌구나..
                    # 근데 저건 왜 들어가는걸까..코드리뷰 영상 한번 더 봐야겠습니다.
                    move += 1
    print(move)
    # print(move)
        
    # print(f'#{test_case} ')