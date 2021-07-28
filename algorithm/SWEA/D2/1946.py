T = int(input())

for case in range(T):
    N = int(input())
    li = []
    for repeat in range(N):
        ch, n = input().split()
        li.append(ch * int(n))
    li = "".join(li)
    cnt = 0
    print(f"#{case + 1}")
    while(cnt <= len(li)):
        print(li[cnt : cnt + 10])
        cnt += 10
