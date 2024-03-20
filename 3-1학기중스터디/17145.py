#낚시왕
from collections import deque
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
# (r,c) 속력, 이동방향, 크기
sharks = deque(deque(map(int, input().split())) for _ in range(M))
dx = [0,0,1,-1]
dy = [-1,1,0,0]

#상어가 움직이는 범위: (1~R, 1~C)
#낚시왕이 움직이는 범위: (0, 1~C) 낚시왕의 위치가 (0,C+1)이 되면 이동을 멈춘다.
'''
*** 1초동안 있는 일 ***
1. 낚시왕이 한칸 이동한다.
2. 낚시왕이 있는 열의 상어 중 땅과 가장 가까운 상어를 잡는다.
3. 상어가 이동한다.
''' 

def moveShark(shark): #return deque
    s_row = shark[0]
    s_col = shark[1]
    s_direction = (shark[3]-1)
    s_speed = shark[2]
    s_size = shark[4]
    for _ in range(s_speed):
        if s_row+dy[s_direction]>=1 and s_row+dy[s_direction]<=R and s_col+dx[s_direction]>=1 and s_col+dx[s_direction]<=C:
            s_row += dy[s_direction]
            s_col += dx[s_direction]
        else:
            if s_direction == 0:
                s_direction = 1
            elif s_direction == 1:
                s_direction = 0
            elif s_direction == 2:
                s_direction = 3
            elif s_direction == 3:
                s_direction = 2
            s_row += dy[s_direction]
            s_col += dx[s_direction]
    return deque([s_row, s_col, s_speed, s_direction+1, s_size])

def getFish(sharks, king_col): #return sharks, size O(M)
    close_shark_row = R+1
    target = deque()
    size = 0
    for i,shark in enumerate(sharks):
        if shark[1] == king_col:
            if close_shark_row > shark[0]:
                close_shark_row = shark[0]
                target = sharks[i]
    if target in sharks:
        size = target[4]
        sharks.remove(target)
    return sharks, size

def eatShark(sharks): #return sharks
    eatens = deque()
    for i in range(len(sharks)-1):
        for j in range(i+1,len(sharks)):
            if sharks[i][0] == sharks[j][0] and sharks[i][1] == sharks[j][1]:
                if sharks[i][4] > sharks[j][4]:
                    eatens.append(sharks[j])
                else:
                    eatens.append(sharks[i])
                break

    for eaten in eatens:
        sharks.remove(eaten)
    return sharks

size = 0
for king_col in range(1, C+1):
    sharks, tmp_size = getFish(sharks, king_col) #O(M)
    size += tmp_size

    for i, shark in enumerate(sharks):  #O(speed * M)
        sharks[i] = moveShark(shark)
    
    sharks = eatShark(sharks) # O(M ** 2)
print(size)