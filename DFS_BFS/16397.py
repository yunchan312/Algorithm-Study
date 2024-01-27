'''
탈출
N을 G로 만들어라 횟수: T

A: N+1
B: N*2, (가장 큰 자리수-1)
'''
import sys
from collections import deque
input = sys.stdin.readline

dq = deque()
n,t,g = map(int, input().split())
visited = set()

dq.append((n, 0))
visited.add(n)

def A(x):
    return x+1
def B(x):
    temp=x*2
    t=0
    while(temp//10 > 0):
        t+=1
        temp//=10
    return (x*2) - (10**t)
didItWork = False

while(dq):
    temp, curTime = dq.popleft()
    if curTime > t:
        break
    if temp == g:
        didItWork=True
        print(curTime)
        break

    if A(temp)<=99999 and A(temp) not in visited:
        dq.append((A(temp), curTime+1))
        visited.add(A(temp))

    if temp>0 and temp*2 <= 99999:
        if B(temp) not in visited:
            dq.append((B(temp), curTime+1))
            visited.add(B(temp))

if not didItWork:
    print('ANG')
