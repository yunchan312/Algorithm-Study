'''거북이'''

'''
F: 한눈금 앞으로
B: 한눈금 뒤로
L: 왼쪽으로 90도 회전
R: 오른쪽으로 90도 회전
'''
t = int(input())
for _ in range(t):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    X=[0]
    Y=[0]
    dir = 0
    def Fcom():
        X.append(X[-1]+dx[dir])
        Y.append(Y[-1]+dy[dir])
    def Bcom():
        X.append(X[-1]-dx[dir])
        Y.append(Y[-1]-dy[dir])
    def Lcom():
        global dir
        dir +=1
        if dir >= 4:
            dir = 0
    def Rcom():
        global dir
        dir -=1
        if dir<0:
            dir = 3


    commands = input()
    for command in commands:
        if command == 'F':
            Fcom()
        elif command == 'B':
            Bcom()
        elif command =='L':
            Lcom()
        elif command == 'R':
            Rcom()
            
    w = max(X) - min(X)
    h = max(Y) - min(Y)
    print(h*w)