T = int(input())

for i in range(T):
    string=input()
    isitTrue = 1

    while(len(string)>=2):
        if string[0] == string[-1]:
            string = string[1:-1]
        else:
            isitTrue = 0
            break

    print(f"#{i + 1} {isitTrue}")