grade = [
    "A+",
    "A0",
    "A-",
    "B+",
    "B0",
    "B-",
    "C+",
    "C0",
    "C-",
    "D0",
    ]

T = int(input())

for case in range(T):
    
    students, pick = map(int, input().split())
    dic = {}
    for s in range(students):
        # dict로 몇 번째 학생인지
        # 정렬
        # value = 점수
        # 학생 찾아서 출력
        middle, final, homework = map(int, input().split())
        dic[s] = middle * 0.35 + final * 0.45 + homework * 0.2
    
    dic_sorted = list(map(list, sorted(dic.items(), key=lambda x: x[1], reverse=True)))
    cnt = 0
    for i in range(students):
        dic_sorted[i][1] = grade[int(i // (students / 10))]
    pick_grade = ""
    for j in range(students):
        if dic_sorted[j][0] == pick - 1:
            pick_grade = dic_sorted[j][1]
            break

    print(f"#{case + 1} {pick_grade}")