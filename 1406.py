'''editor'''
from collections import deque
import sys
input = sys.stdin.readline

A=deque(input().strip())
cursor = len(A)
M = int(input())

for i in range(M):
    command = list(input().split())
    if command[0] == 'P':
        ch = command[1]
        if cursor == len(A):
            A.append(ch)
        elif cursor == 0:
            A.appendleft(ch)
        else:
            A.insert(cursor, ch)
        cursor += 1
    elif command[0] == 'L':
        if cursor > 0:
            cursor -= 1
    elif command[0] == 'D':
        if cursor < len(A):
            cursor += 1
    elif command[0] == 'B':
        if cursor > 0:
            A.pop(cursor-1)
            cursor -=1