N = int(input())
switch = list(map(int, input().split()))
S = int(input())
students = []
for _ in range(S):
    students.append(list(map(int, input().split())))



for student in students:
    if student[0] == 1:
        rule1 = N//int(student[1]) + 1
        for i in range(1, rule1):
            if switch[int(student[1])*i -1] == 1:
                switch[int(student[1])*i -1] = 0
            else:
                switch[int(student[1])*i-1] = 1
    else:
        for i in range(N):
            if int(student[1])-i >= 1 and int(student[1])+i <= N:
                if switch[int(student[1])-i-1] == switch[int(student[1])+i-1]:
                    if switch[int(student[1])-i-1] == 1:
                        switch[int(student[1])-i-1] = 0
                        switch[int(student[1])+i-1] = 0
                    else:
                        switch[int(student[1])-i-1] = 1
                        switch[int(student[1])+i-1] = 1
                else:
                    break

D = N//20 + 1
for d in range(D):
    s = switch[0+20*d:20+20*d]
    print(*s)
