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
student_list = [list(map(int, input().split())) for _ in range(student_N)]


for student in student_list:
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
