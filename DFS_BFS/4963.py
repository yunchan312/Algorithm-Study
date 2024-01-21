'''
    섬의 개수
    첫째줄 : 지도의 너비w와 높이h
    둘째줄 : h개의 줄에는 지도가 주어진다. 1은땅, 0은 바다
    입력의 마지막 줄에는 0 0이 주어진다
'''
cnt = 0
w,h = map(int, input().split())
plate = []
visited=[[False for _ in range(w)] for _ in range(h)]
for i in range(h):
    plate.append(list(map(int, input().split())))
dx = [-1, 0, 1, -1, 1, -1,0,1]
dy = [-1, -1, -1, 0, 0, 1,1,1]
cnt = 0


def findLand(y,x):
    if plate[y][x] == 1:
        plate[y][x] = 0
        for i in range(8):
            if y+dy[i] < 0 and y+dy[i] >= h and x+dx[i] < 0 and x+dx[i] >= w:
                if plate[y+dy[i]][x+dx[i]] == 1:
                    findLand(y+dy[i], x+dx[i])


for y in range(h):
    for x in range(w):
        findLand(y,x)
        cnt += 1
print(cnt)