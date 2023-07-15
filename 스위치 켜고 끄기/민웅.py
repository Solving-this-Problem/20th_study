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
