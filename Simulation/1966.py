'''
프린터 큐
N => 문서의 개수 
M => 몇번째로 인쇄되는지 궁금한 문서가 현재 QUEUE에서 몇번째에 놓여있는지를 나타내는 정수

뭐지 ㅅㅂ
'''
import sys
from collections import deque
input = sys.stdin.readline


N, target = map(int, input().split())
docu = list(map(int, input().split()))
dq = deque()
for n in range(N):
    dq.append(n)
ans =[]
for i in range(N):
    for j in range(i+1, N):
        if docu[dq[i]] < docu[dq[j]]:
            print('did')
            temp = dq.popleft()
            ans.append(temp)
        print(dq)


for d in dq:
    if d == target:
        print(ans)
    ans +=1