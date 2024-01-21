'''촌수계산'''

n = int(input())

a,b = map(int, input().split())
t = int(input())

child = [[] for _ in range(n+1)]
parent= [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited[0] = True

for i in range(t):
    x,y = map(int, input().split())
    child[x].append(y)
    parent[y].append(x)

def cntChonSoo(a):
    visited[a] = True
    temp = len(child[a])
    


