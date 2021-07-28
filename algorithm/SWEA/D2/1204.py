T = int(input())

for case in range(T):
    dic = {}
    
    N = int(input())
    for rep in range(N):
    
        li = list(map(int, input().split()))
        
        for i in li:
            try:
                dic[i] += 1
            except:
                dic[i] = 1
        
        key_total = 0
        value_total = 0
        for key, value in dic.items():
            if value_total < value:
                value_total = value
                key_total = key
            elif value_total ==value:
                if key_total <key:
                    key_total = key

        print(f"#{case + 1} {key_total}")