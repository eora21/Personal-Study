N = int(input())

for i in range(1, N + 1):
    cnt = 0
    for t in str(i):
        if t=="3" or t=="6" or t=="9":
            cnt+=1
    if cnt>0:
        print("-"*cnt,end=" ")
    else:
        print(i, end=" ")