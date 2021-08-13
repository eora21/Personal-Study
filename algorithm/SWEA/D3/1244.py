T = int(input())

"""
우선순위
큼, 뒤쪽 <-> 작음, 앞쪽
동일한 큰, 작은 숫자
횟수에 따라
미리 핑을 찍고 교체!
1== 제일 뒤부터의 max, max가 아닌 맨 앞 숫자 핑
1 < max를 제외한 다음 max, 이번 max가 아닌 맨 앞 숫자 핑
"""

for case in range(T):
    num, change = input().split()

    num = list(map(int, num))
    reverse_num = list(reversed(num))

    print(num)
    print(reverse_num)

    # max_li = []
    # for c in range(int(change)):
    #     max_num = max(num)
    #     max_li.append(max_num)
