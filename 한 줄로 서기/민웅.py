# 1138_한 줄로 서기
import sys
input = sys.stdin.readline

N = int(input())

n_li = list(map(int, input().split()))
line = [-1]*N
for i in range(1, N+1):
    n = n_li[i-1]
    for j in range(N):
        if not n and line[j] == -1:
            line[j] = i
            break
        elif line[j] == -1:
            n -= 1

print(*line)