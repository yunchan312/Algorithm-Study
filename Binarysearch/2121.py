'''넷이놀기'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A,B = map(int, input().split())
dots = set(tuple(map(int, input().split())) for _ in range(N))
cnt = 0

for x,y in dots:
    if (x+A,y) in dots and (x,y+B) in dots and (x+A,y+B) in dots:
        cnt +=1
print(cnt)

'''def isRect(tx,ty,start, end):
    if start >= end:
        return False
    pivot = (start+end)//2
    x,y = dots[pivot]
    if tx > x:
        isRect(x,y,pivot,end)
    elif tx < x:
        isRect(x,y,start,pivot)
    else:
        if ty > y:
            isRect(x,y,pivot,end)
        elif ty < y:
            isRect(x,y,start,pivot)
        else:
            return True


for i in range(N):
    x,y = dots[i]
    for k in range(i+1, N):
        jx, jy = dots[k]
        if jx > x:
            break
        if jy-y == B:
            print(x,y)
            print(jx,jy)
            if isRect(x+A,y,i,len(dots)-1) and isRect(jx+A,jy,k,len(dots)-1):
                cnt +=1
print(cnt)
'''
