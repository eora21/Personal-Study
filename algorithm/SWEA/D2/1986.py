T = int(input())

for i in range(T):
    end = int(input())
    total = 0
    for num in range(1, end + 1):
        total += num if num % 2 else -num

    print(f"#{i + 1} {total}")