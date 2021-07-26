T = int(input())

for case in range(T):
    N = int(input())
    m_total = a_total = 0
    for C in range(N):
        mode = input()
        if mode == "0":
            pass
        else:
            m, a = map(int, mode.split())
            if m == 1:
                a_total += a
            else:
                a_total -= a
            if a_total < 0:
                a_total = 0
        m_total += a_total

    print(f"#{case + 1} {m_total}")