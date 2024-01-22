'''촌수계산'''
from collections import deque

n = int(input())

a,b = map(int, input().split())
t = int(input())

q = deque()
q.append(a)

family = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited[0] = True

for i in range(t):
    x,y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

dis = [0 for _ in range(n+1)]
while(q):
    temp = q.popleft()
    for mem in family[temp]:
        if not visited[mem]:
            q.append(mem)
            visited[mem] = True
            dis[mem] = dis[temp]+1

if dis[b] == 0:
    print(-1)
else:
    print(dis[b])


    


