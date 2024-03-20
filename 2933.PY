import sys
input = sys.stdin.readline

R,C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
throw = int(input())
height = list(map(int, input().split()))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cluster = set()
visited = []

def Throw(i, h):
    if i%2 == 0:
        for k in range(C):
            if cave[R-h][k] == 'x':
                cave[R-h][k] = '.'
                visited = [[False for _ in range(C)] for _ in range(R)]
                getMineralLocation(R-h-1, k, visited)
                break
    elif i%2 == 1:
        for k in range(C,-1,-1):
            if cave[R-h][k] == 'x':
                cave[R-h][k] = '.'
                visited = [[False for _ in range(C)] for _ in range(R)]
                getMineralLocation(R-h-1, k, visited)
                break

def getMineralLocation(h,k, visited):
    #h~R까지 탐색
    if cave[h][k] == 'x' and not visited[h][k]:
        visited[h][k] = True
        cluster.add((h, k))
        for d in range(4):
            x = k+dx[d]
            y = h+dy[d]
            if y < R and y >= h and x>=0 and x<C:
                getMineralLocation(y, x, visited)
    return

Throw(1,4)
print(cluster)