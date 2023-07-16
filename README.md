# 20th_study
[20주차] 코딩테스트 준비 8주차
<br/>

[프로그래머스 sql 문제 바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/164670)

[프로그래머스 python 문제 바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/118667)

[백준 문제집 바로가기](https://www.acmicpc.net/workbook/view/16092)

<br/><br/>

# [SQL] 조건에 맞는 사용자 정보 조회하기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./조건에%20맞는%20사용자%20정보%20조회하기/동우.sql)
```sql
```
## [민웅](./조건에%20맞는%20사용자%20정보%20조회하기/민웅.sql)
```sql
```
## [서희](./조건에%20맞는%20사용자%20정보%20조회하기/서희.sql)
```sql
SELECT USER_ID, NICKNAME, CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) AS '전체주소',
    CONCAT(SUBSTR(TLNO,1,3),'-',SUBSTR(TLNO,4,4),'-',SUBSTR(TLNO,8,4)) AS '전화번호'
FROM USED_GOODS_USER
WHERE USER_ID IN (
    SELECT WRITER_ID
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING count(*) >= 3
)

ORDER BY USER_ID DESC
```
## [성구](./조건에%20맞는%20사용자%20정보%20조회하기/성구.sql)
```sql
SELECT USER_ID, NICKNAME, CONCAT(CITY," ", STREET_ADDRESS1," ", STREET_ADDRESS2) AS "전체주소", 
CONCAT(LEFT(TLNO,3), "-",SUBSTRING(TLNO,4,4), "-", RIGHT(TLNO, 4)) "전화번호"
FROM USED_GOODS_USER AS U
LEFT JOIN (SELECT WRITER_ID, COUNT(BOARD_ID) AS NUMBER
            FROM USED_GOODS_BOARD 
            GROUP BY WRITER_ID
          ) AS C
ON U.USER_ID = C.WRITER_ID
WHERE C.NUMBER >=3
ORDER BY USER_ID DESC;
```
## [혜진](./조건에%20맞는%20사용자%20정보%20조회하기/혜진.sql)
```sql
```

</div>
</details>

<br/><br/><br/>

# [프로그래머스] 두 큐 합 같게 만들기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./두%20큐%20합%20같게%20만들기/동우.py)
```py
```
## [민웅](./두%20큐%20합%20같게%20만들기/민웅.py)
```py
# 테케 2개 틀린상태
from collections import deque


def solution(queue1, queue2):
    answer = -2
    check = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    s1 = sum(q1)
    s2 = sum(q2)
    max_sum = s1 + s2
    target_num = max_sum//2

    if max_sum%2 != 0:
        return -1

    if max(q1) > target_num or max(q2) > target_num:
        return -1

    at_least = False

    while True:
        if s1 == target_num and at_least:
            break

        if check >= 2*(len(q2)+len(q1)):
            return -1

        if s1 > target_num:
            temp = q1.popleft()
            q2.append(temp)
            check += 1
            s1 -= temp
            s2 += temp

        else:
            temp = q2.popleft()
            q1.append(temp)
            check += 1
            s1 += temp
            s2 -= temp
        at_least = True

    answer = check

    return answer
```
## [서희](./두%20큐%20합%20같게%20만들기/서희.py)
```py
from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    max_cnt = (len(queue1)) * 3
    s1 = sum(queue1)
    s2 = sum(queue2)
    S = s1 + s2

    if S % 2 != 0:
        return -1

    while True:
        if s1 > s2:
            target = q1.popleft()
            q2.append(target)
            s1 -= target
            s2 += target
            answer += 1
        elif s1 < s2:
            target = q2.popleft()
            q1.append(target)
            s1 += target
            s2 -= target
            answer += 1
        else:
            break
        if answer == max_cnt:
            answer = -1
            break
    return answer
```
## [성구](./두%20큐%20합%20같게%20만들기/성구.py)
```py
```
## [혜진](./두%20큐%20합%20같게%20만들기/혜진.py)
```py
```

</div>
</details>

<br/><br/><br/>

# [백준] 스위치 켜고 끄기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./스위치%20켜고%20끄기/동우.py)
```py
import sys
input = sys.stdin.readline

N = int(input())
switch = [0] + list(map(int, input().strip().split()))
students = int(input())

for _ in range(students):
    s, num = map(int, input().strip().split())

    if s == 1:
        for i in range(1, N + 1):
            if not i % num:
                if switch[i]:
                    switch[i] = 0
                else:
                    switch[i] = 1
    else:
        if switch[num]:
            switch[num] = 0
        elif switch[num] == 0:
            switch[num] = 1

        j = 1
        while True:

            if num - j < 1:
                break
            elif num + j > N:
                break

            elif switch[num - j] == switch[num + j]:
                if switch[num - j]:
                    switch[num - j], switch[num + j] = 0, 0
                    j += 1
                else:
                    switch[num - j], switch[num + j] = 1, 1
                    j += 1
            else:
                break

for i in range(1, N + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
```
## [민웅](./스위치%20켜고%20끄기/민웅.py)
```py
# 1244_스위치켜고끄기_OnOff
import sys
input = sys.stdin.readline

N = int(input())

switchs = list(map(int, input().split()))

n = int(input())

for _ in range(n):
    gender, number = map(int, input().split())

    if gender == 1:
        n = number
        while number-1 < N:
            if switchs[number-1]:
                switchs[number-1] = 0
            else:
                switchs[number-1] = 1
            number += n
    else:
        i, j = number-2, number
        if switchs[number-1]:
            switchs[number-1] = 0
        else:
            switchs[number-1] = 1

        while i >= 0 and j < N:
            if switchs[i] == switchs[j]:
                if switchs[i]:
                    switchs[i] = 0
                    switchs[j] = 0
                else:
                    switchs[i] = 1
                    switchs[j] = 1
            else:
                break
            i -= 1
            j += 1

for i in range(1, N+1):
    if i % 20:
        print(switchs[i-1], end=' ')
    else:
        print(switchs[i-1])

```
## [서희](./스위치%20켜고%20끄기/서희.py)
```py
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

```
## [성구](./스위치%20켜고%20끄기/성구.py)
```py
# 1244 스위치 켜고 끄기
'''
1 <= switch, 학생수 <= 100 정수
1: on, 0: off
남: 1, 여: 2
'''
import sys
input = sys.stdin.readline

# input
switch_N = int(input())
switch = list(map(int, input().split()))
student_N = int(input())

for student in [list(map(int, input().split())) for _ in range(student_N)]:
    # 남자
    if student[0] == 1:
        for number in range(student[1]-1, switch_N, student[1]):
            switch[number] = 0 if switch[number] else 1

    # 여자
    if student[0] == 2:
        left = right = student[1]-1
        switch[left] = 0 if switch[left] else 1
        while left>=0 and right < switch_N:
            if switch[right] != switch[left]:
                break
            switch[left] = 0 if switch[left] else 1
            switch[right] = 0 if switch[right] else 1
            left -= 1
            right += 1


# Output form

ans = "" 
for i in range(switch_N):
    ans += str(switch[i]) + " "
    if not((i+1) % 20):
        ans += "\n"
print(ans)

```
## [혜진](./스위치%20켜고%20끄기/혜진.py)
```py
```

</div>
</details>

<br/><br/><br/>


# [백준] 한 줄로 서기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./한%20줄로%20서기/동우.py)
```py
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip().split()))

tmp = [0] * N

for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == arr[i]:
            if tmp[j] == 0:
                tmp[j] = i + 1
                break
        elif tmp[j] == 0:
            cnt += 1

print(*tmp)

```
## [민웅](./한%20줄로%20서기/민웅.py)
```py
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
```
## [서희](./한%20줄로%20서기/서희.py)
```py
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

```
## [성구](./한%20줄로%20서기/성구.py)
```py
# 1138 한 줄로 서기
'''
1<= N <=10 자연수
(리스트 내부 수) <= N
'''

import sys
input = sys.stdin.readline

# Input
N = int(input())
arr = list(map(int,input().split()))

# Define
# 정답 만들기 용 리스트
line = [0] * N

# Setting Line Function
def Insert_Number(start:int, end:int, num:int):
    for i in range(start,end):
        if not line[i]:
            line[i] = num
            return 

# Main
def Main():               
    for i in range(N):
        cnt = 0
        for j in range(N):
            if cnt == arr[i]:   # 나보다 키가 큰 사람이 입력 받은 만큼 있으면
                Insert_Number(j, N, i+1) # 빈 곳에 서기
                break                       #  다음 사람의 순서로 가기위해 break
            elif not line[j] or line[j] >= (i+1):   # 아직 나보다 큰 사람들이 입력받은 만큼 없는 경우,
                cnt += 1                    # 키가 큰 사람이 있거나, 큰 사람이 설 가능성이 있는 경우 카운트
    print(*line)


Main()      
```
## [혜진](./두%20큐%20합%20같게%20만들기/혜진.py)
```py
```

</div>
</details>

<br/><br/><br/>


# [백준] 여행가자

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [동우](./여행가자/동우.py)
```py
```
## [민웅](./여행가자/민웅.py)
```py
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

```
## [서희](./여행가자/서희.py)
```py
```
## [성구](./여행가자/성구.py)
```py
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
```
## [혜진](./여행가자/혜진.py)
```py
```

</div>
</details>
