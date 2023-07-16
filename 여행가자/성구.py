# 1976 여행가자
import sys
from collections import deque
input = sys.stdin.readline

# Input
N = int(input())
M = int(input())
linked = [ [] for _ in range(N+1)]
# setting
for country in range(1, N+1):
    route = list(map(int, input().split()))
    for b in range(N):
        if route[b]:
            linked[country].append(b+1)
plan = list(map(int, input().split()))

# BFS
que = deque([plan[0]])
visited = [0] * (N+1)
visited[plan[0]] = 1
while que:
    spot = que.popleft()
    for i in range(1, N+1):
        for element in linked[spot]:
            if not visited[element]:
                que.append(element)
                visited[element] = 1
for i in plan:
    if not visited[i]:
        print("NO")
        break
else:
    print("YES")



'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

linked = [ [] for _ in range(N+1)]

for country in range(1,N+1):
    route = list(map(int, input().split()))
    for b in range(N):
        if route[b]:
            linked[country].append(b+1)

travel = list(map(int,input().split()))

check = set([travel[0]])
for i in range(1,N+1):
    for j in range(M):
        if travel[j] in linked[i]:
            check.add(travel[j])

for element in set(travel):
    if element not in check:
        print("NO")
        break
else:
    print("YES")

'''