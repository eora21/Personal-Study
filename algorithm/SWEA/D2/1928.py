li = [2, 3, 5, 7, 11]

T = int(input())

for i in range(T):
    string = input()
    li=[]
    #변환
    for num in range(len(string)):
        ch = ord(string[num])
        if ch >= 97:
            ch -= 71
        elif ch >= 65:
            ch -= 65
        elif ch >= 48:
            ch += 4
        elif ch == 43:
            ch = 62
        else:
            ch = 63

        for StoZ in range(5, -1, -1):
            li.append(ch // 2**StoZ)
            if ch // 2**StoZ:
                ch -= 2**StoZ

    #8개씩
    ans =[]
    for cnt in range(len(li) // 8):
        st = li[cnt * 8:cnt * 8 + 8]
        total = 0
        for ch in range(len(st)):
            if int(st[7 - ch]):
                total += 2**ch
        ans.append(chr(total))

    print(f"#{i + 1} {''.join(ans)}")