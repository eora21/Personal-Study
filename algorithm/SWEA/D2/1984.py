T = int(input())

for case in range(T):
    li = list(map(int, input().split()))
    li.sort()
    # print(f"{li[0]}, {li[-1]}")
    li = li[1:-1]
    print(f"#{case + 1} {round(sum(li) / len(li))}")