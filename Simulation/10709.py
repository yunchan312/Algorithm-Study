'''기상캐스터'''

import sys
input = sys.stdin.readline

h,w = map(int, input().split())
sky = []
isCloud = [[False for _ in range(w)] for _ in range(h)]
ans = [[-1 for _ in range(w)] for _ in range(h)]

for _ in range(h):
    sky.append(input())

for i in range(h):
    for j in range(w-1,-1,-1):
        if sky[i][j] == 'c' and not isCloud[i][j]:
            cnt = 1
            for k in range(j, w):
                if not isCloud[i][k]:
                    ans[i][k] += cnt
                    cnt +=1
                isCloud[i][k] = True

for a in range(h):
    temp =  ''
    for b in range(w):
        temp = temp + str(ans[a][b])+ ' '
    print(temp)

