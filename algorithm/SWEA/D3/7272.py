for case in range(int(input())):
    st = list(map(list, input().split()))

    for s in st:
        for i in range(len(s)):
            if s[i] == "B":
                s[i] = "2"
            elif s[i] in "ADOPQR":
                s[i] = "1"
            else:
                s[i] = "0"
    
    print("#{} {}".format(case + 1, "SAME" if st[0] == st[1] else "DIFF" ))

    # 정답 제출에 파이썬이 없어 채점불가