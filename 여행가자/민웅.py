# 1976_여행가자_Lets trip
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

adjL = [[] for _ in range(N+1)]

visited = [0]*(N+1)
check = 0

for i in range(1, N+1):
    roads = list(map(int, input().split()))

    for j in range(1, N+1):
        if roads[j-1]:
            adjL[i].append(j)

plan = list(map(int, input().split()))

stack = [plan[0]]

while stack:
    city = stack.pop()
    visited[city] = 1

    for node in adjL[city]:
        if not visited[node]:
            stack.append(node)

ans = 'YES'
for v in plan:
    if not visited[v]:
        ans = 'NO'
        break


print(ans)
