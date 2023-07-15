N = int(input())
people = list(map(int, input().split()))

line = [0] * N
for i in range(N):
    empty_cnt = 0
    j = 0
    while True:
        if empty_cnt == people[i] and line[j] == 0:
            line[j] = i + 1
            break
        if line[j] == 0:
            empty_cnt += 1
        j += 1

print(*line)
