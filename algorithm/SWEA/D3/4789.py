for case in range(int(input())):
    people = list(map(int, input()))

    now = 0
    hire = 0

    for i in range(len(people)):
        if people[i] and now < i:
            hire += i - now
            now += i - now
        now += people[i]
    
    print("#{} {}".format(case + 1, hire))