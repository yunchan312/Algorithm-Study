'''바이러스'''

n = int(input())
t = int(input())
visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for i in range(t):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def DFS(x):
    visited[x] = 1
    for i in graph[x]:
        if visited[i] == 0:
            DFS(i)

DFS(1)
print(sum(visited)-1)