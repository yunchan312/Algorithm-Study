'''
    특정거리의도시찾기
    N => 도시의 개수
    M => 도로의 개수
    K => 거리정보
    X => 출발 도시의 번호
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int, input().split())
cities = [[] for _ in range(n)]
d = deque()

for i in range(m):
    a, b = map(int, input().split())
    cities[a-1].append(b-1)


visited = [False for _ in range(n)]
d.append(x-1)
visited[x-1] = True
dis = [0 for _ in range(n)]
ans = []
while(d):
    temp = d.popleft()
    for num in cities[temp]:
        if not visited[num]:
            d.append(num)
            visited[num] =True
            dis[num] = dis[temp]+1
            if dis[num] == k:
                ans.append(num)
if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i+1, end='\n')

