T = int(input())

for case in range(T):
    li = []
    Cash = 50000
    Money = int(input())
    mode = True
    while(Cash >= 10):
        li.append(int(Money // Cash))
        Money %= Cash
        Cash /= 5 if mode else 2
        mode = not mode
    
    print(f"#{case + 1}")
    print(" ".join(map(str, li)))