# 1
# 새로운불면증 치료법
# 민석이가 양을 세려는데
# 1번부터 세기 재미없을거같아서 N의 배수번호 양을 센다.
# 임의의 숫자 N을 1부터 시작하여 곱해서 나온 수가 
# 0부터 9까지 다 나와야한다?
# 임의의 숫자 N에 1부터 곱한 숫자열을
# 0부터 9를 갖고있는 리스트에서 겹치는 숫자를 제거하면서
# 리스트가 비면 반복문을 멈춰볼까
import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    # 자, 야옹씨. 빈 집합 numbers를 만들고 어떤 수를 자릿수로 쪼개서 원소로 집어 넣을거에요.
    # 그럼 집합은 중복이 불가능 하니까. 0부터 9까지 10개밖에 안들어가겠죠?
    numbers = set()
    # N에 수를 곱해 나가야 하니까 N은 int값이어야 연산을 할 수 있겠죠.
    N = int(input())
    # 그래서 number의 원소 갯수가 10개 이하일때, 반복문을 돌리면 무한루프가 돌아가지...음
    # 원소 개수가 10이 되면 break를 걸자
    # 그리고, N은 N, 2N, 3N으로 증가하니까 반복문을 돌때마다 초기값 N에 고정값 N을 한번씩 더하는 정수형 변수 Nc를 선언할겁니다.
    # 그러면 result는 Nc겠죠?
    # 그리고 Nc의 초기값은 N일거에요. test_case마다 N과 초기값 Nc가 달라지니 라인 위치를 조심합시다.
    Nc = N
    while True:
        # 이렇게 하면? n으로 N을 읽어서 numbers에 집어넣을 수 있겠죠.
        # 문자형으로 변환한 숫자가 자릿수로 하나씩 나눠져서 number의 원소로 들어가요.
        for n in str(Nc):
            numbers.add(n)
            # 다 집어넣었으면 len(number)를 한번 봅시다.
        if len(numbers) == 10 : 
            break
        # len(numbers)가 10개가 차지 않았으니 N을 한번 더합시다.
        Nc += N
        # 10개가 다 차면 while문을 나가요
        # 그러면 마지막 Nc가...N이 더해지지않나? 안돌아가니까 안들어가나?
        # 안더해지네요! 왜냐면 break 이후에 있으니까! 34번줄은 안돌아갑니다.
    print(f'#{test_case} {Nc}')