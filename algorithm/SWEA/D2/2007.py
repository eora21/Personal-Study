T = int(input())

for i in range(T):
    string=input()
    for cnt in range(2, len(string)):
        start = cnt
        st=string[:cnt]
        end = cnt * 2
        flag=False
        # print(st == string[start:end])
        # print(st, string[start:end])
        while st == string[start:end]:
            start, end = end, end + cnt
            if end == len(string) or cnt > len(string[start:end]):
                flag=True
                break
        if(flag):
            break
    print(f"#{i + 1} {cnt}")