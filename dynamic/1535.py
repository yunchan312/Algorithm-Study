'''안녕'''
from collections import deque

N = int(input())
life = deque(map(int, input().split()))
joy = deque(map(int, input().split()))

life.appendleft(100)
joy.appendleft(0)

ans = []

def search(j, l, depth):
    global ans
    if depth >= N:
        ans.append((j, l))
        return
    if l-life[depth+1] > 0:
        search(j+joy[depth+1], l-life[depth+1], depth+1)
    search(j, l, depth+1)


search(joy[0], life[0], 0)
j,l = max(ans)
print(j)

    
