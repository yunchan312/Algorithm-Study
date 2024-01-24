'''아기상어'''

from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

ans = []
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            ans.append(i)
            ans.append(j)

cnt = 0

def bfs(x, y):
    visited = [[0]*N for _ in range(N)]
    q = deque([[x,y]])
    cand = []

    visited[x][y] = 1

    while q:
        temp, cnt = q.popleft()

        for i in range(4):
            nx, ny = temp + dx[i] , cnt + dy[i]

            if 0 <= nx and nx < N and 0 <= ny and ny < N and visited[nx][ny] == 0:
                if space[x][y] > space[nx][ny] and space[nx][ny] != 0:
                    visited[nx][ny] =  visited[temp][cnt] + 1
                    cand.append((visited[nx][ny] - 1, nx, ny))
                elif space[x][y] == space[nx][ny]:
                    visited[nx][ny] =  visited[temp][cnt] + 1
                    q.append([nx,ny])
                elif space[nx][ny] == 0:
                    visited[nx][ny] =  visited[temp][cnt] + 1
                    q.append([nx,ny])
                    
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))


i, j = ans
size = [2, 0]
while True:
    space[i][j] = size[0]
    cand = deque(bfs(i,j))
    
    if not cand:
        break
        
    step, xx, yy = cand.popleft()
    cnt += step
    size[1] += 1
    
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    space[i][j] = 0
    i, j = xx, yy
        
print(cnt)