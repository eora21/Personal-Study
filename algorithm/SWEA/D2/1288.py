T = int(input())

for i in range(T):
    N = int(input())
    nums=set()
    cnt = 1
    while len(nums) < 10:
        st = str(N * cnt)
        for ch in st:
            nums.add(ch)
        cnt += 1

    print(f"#{i + 1} {N * cnt}")