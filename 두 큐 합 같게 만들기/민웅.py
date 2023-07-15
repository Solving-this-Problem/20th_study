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