T = int(input())

for i in range(T):
    N = int(input())
    nums=set()
    cnt = 0
    while len(nums) < 10:
        cnt += 1
        st = str(N * cnt)
        for ch in st:
            nums.add(ch)
        
    print(f"#{i + 1} {N * cnt}")