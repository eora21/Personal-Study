T = int(input())

for case in range(T):
    a = input()
    nums = list(map(int, input().split()))
    nums.sort()
    
    st = " ".join(list(map(str, nums)))

    print(f"#{case + 1} {st}")