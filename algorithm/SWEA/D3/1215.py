def check_palindrome(args, L):

    cnt = 0
    for i in range(8 - L + 1):
        arr = args[i: i + L]

        while len(arr) > 1:
            if arr[0] == arr[-1]:
                arr = arr[1:-1]
            else:
                break
        else:
            cnt += 1

    return cnt

for case in range(10):
    array = [[0]] * 8
    total = 0

    L = int(input())
    
    for i in range(8):
        array[i] = input()
        total += check_palindrome(array[i], L)
    
    for col in range(8):
        li = []
        for row in range(8):
            li.append(array[row][col])
        total += check_palindrome(li, L)

    print(f"#{case + 1} {total}")