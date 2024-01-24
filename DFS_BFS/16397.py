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
n,g,t = map(int, input().split())
visited = set()

dq.append((n, 0))
visited.add(n)

def A(x):
    return x+1
def B(x):
    temp=x*2
    t=0
    while(temp//10 != 0):
        t+=1
        temp//=10
    return (x*2) - (10**t)
didItWork = False

while dq:
    temp, cnt = dq.popleft()
    if cnt > t:
        break
    if temp == g:
        didItWork = True
        break

    if A(temp) not in visited and A(temp) < 100000:
        dq.append((A(temp), cnt+1))
        visited.add(A(temp))
    
    if B(temp) not in visited and B(temp) < 100000:
        dq.append((B(temp), cnt+1))
        visited.add(B(temp))
    
if didItWork:
    print(cnt)
else:
    print('ANG')

    