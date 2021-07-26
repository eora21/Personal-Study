calendar = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

T = int(input())

for case in range(T):
    Mth_Day = input().split(" ")

    A_Mth = int(Mth_Day[0])
    A_Day = int(Mth_Day[1])
    B_Mth = int(Mth_Day[2])
    B_Day = int(Mth_Day[3])

    result = 0

    while(A_Mth < B_Mth):
        result += calendar[A_Mth] - A_Day + 1
        A_Mth += 1
        A_Day = 1
    
    result += B_Day - A_Day + 1

    print(f"#{case + 1} {result}")