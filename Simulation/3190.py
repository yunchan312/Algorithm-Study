'''뱀

사과를 먹으면 뱀 길이가 늘어난다.
뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

NxN 정사각 보드위에서 진행
몇몇 칸에는 사과가 있다.

매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
    먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = []
body=deque()
commands=deque()

dir = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

hx, hy, tx, ty = 1, 1, 1, 1

for _ in range(K):
    ar, ac = map(int, input().split())
    apples.append((ar, ac))
L = int(input())
for _ in range(L):
    sec, com = map(str, input().split())
    commands.append((int(sec), com))

def Dcom():
    global dir
    dir +=1
    if dir >= 4:
        dir = 0
def Lcom():
    global dir
    dir -=1
    if dir <0:
        dir = 3
def didHeadHitWall(hx, hy):
    if hx <= 0 or hy <= 0 or hx >N or hy > N:
        return True
    return False
def didHeadHitBody(hx, hy, body):
    for by, bx in body:
        if by == hy and bx == hx:
            return True
    return False
def didHeadEatApp(hx, hy, apples):
    for index, A in enumerate(apples):
        ay, ax = A
        if ax == hx and ay == hy:
            apples.pop(index)
            return True
def changeDir(timeCnt, commands):
    if len(commands) == 0:
        return
    else:
        comTime, comType = commands[0]
        if timeCnt == comTime:
            return comType
        return



timeCnt = 0
while(True):
    timeCnt +=1
    #머리 먼저 움직이기
    hx += dx[dir]
    hy += dy[dir]
    
    #게임 오버인지 검사
    if didHeadHitBody(hx, hy, body) or didHeadHitWall(hx, hy):
        print(timeCnt)
        break
    #사과를 먹었는지 검사
    if didHeadEatApp(hx, hy, apples):
        #사과를 먹었다면, head의 이 전위치를 body에 포함
        body.appendleft((hy-dy[dir],hx-dx[dir]))
    else:
        #사과를 먹지 않았다면, body 이동
        body.appendleft((hy-dy[dir],hx-dx[dir]))
        body.pop()
    #뱀의 행동을 마치고, 방향을 바꾸는지 여부 검사 및 방향 바꿈
        
    if changeDir(timeCnt, commands) == 'D':
        commands.popleft()
        Dcom()
    elif changeDir(timeCnt, commands) == 'L':
        commands.popleft()
        Lcom()

        

