for case in range(10):
    
    N = input()
    nums = list(map(int, input().split()))

    minus = 1

    while True:
        val = nums.pop(0) - minus
        if val <= 0:
            nums.append(0)
            break
        nums.append(val)
        minus += 1
        if minus == 6:
            minus = 1
    
    print(f"#{N}", *nums)