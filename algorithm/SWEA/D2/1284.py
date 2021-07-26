T = int(input())

for i in range(T):
    PQRSW = input().split(" ")
    P = int(PQRSW[0]) #A사 1L당 요금
    Q = int(PQRSW[1]) #B사 기본 요금
    R = int(PQRSW[2]) #B사 초과 기준
    S = int(PQRSW[3]) #B사 1L당 초과 요금
    W = int(PQRSW[4]) #종민이가 사용한 양

    A = W * P
    if W > R:
        B = Q + (W - R) * S
    else:
        B = Q

    print(f"#{i + 1} {A if A <= B else B}")