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
