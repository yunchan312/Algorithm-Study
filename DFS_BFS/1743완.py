'''음식물 피하기'''
#N: 세로길이
#M: 가로길이

#sys추가하니까 됐음

import sys
sys.setrecursionlimit(10**5)

N,M,K = map(int, sys.stdin.readline().split())
hall = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
food = []
f = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(K):
    ty,tx = map(int, sys.stdin.readline().split())
    hall[ty-1][tx-1] = 1

def foods(y,x):
    global f
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<M and 0<=ny<N:
            if hall[ny][nx]==1 and not visited[ny][nx]:
                visited[ny][nx] = True
                f +=1
                foods(ny,nx)

res = 0
for i in range(N):
    for j in range(M):
        if hall[i][j] == 1 and not visited[i][j]:
            f=0
            foods(i, j)
            res = max(res, f)

print(res)

