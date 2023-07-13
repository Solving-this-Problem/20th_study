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
```
## [서희](./두%20큐%20합%20같게%20만들기/서희.py)
```py
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
```
## [민웅](./스위치%20켜고%20끄기/민웅.py)
```py
```
## [서희](./스위치%20켜고%20끄기/서희.py)
```py
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
```
## [민웅](./한%20줄로%20서기/민웅.py)
```py
```
## [서희](./한%20줄로%20서기/서희.py)
```py
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
```
## [서희](./여행가자/서희.py)
```py
```
## [성구](./여행가자/성구.py)
```py
```
## [혜진](./여행가자/혜진.py)
```py
```

</div>
</details>