row, col = map(int, input().split())

plate = []

for i in range(row):
    plate.append(input())

'''
첫번째를 기준으로, 
y좌표가 짝수일 때, x좌표가 짝수면 첫번째와 같다.
y좌표가 홀수일 때, x좌표가 홀수면 첫번째와 같다.

총 경우는 2개, 첫번째가 W일 때, 첫번째가 B일 때
'''

def cntModi(x,y,plate):
    cnt_W = 0
    cnt_B = 0
    start = plate[y-7][x-7]
    for i in range(8):
        for j in range(8):
            if (i)%2 == (j)%2:
                if 'W' != plate[y-7+i][x-7+j]:
                    cnt_W += 1
                else:
                    cnt_B +=1
            else:
                if 'W' == plate[y-7+i][x-7+j]:
                    cnt_W += 1
                else:
                    cnt_B += 1
    return min(cnt_B, cnt_W)

minModi = 1000000
for y in range(row-1, 6,-1):
    for x in range(col-1, 6, -1):
        minModi = min(cntModi(x,y,plate), minModi)

print(minModi)

'''
def cntModi(x,y,plate):
    cnt = 0
    xs = x-7
    ys = y-7
    start = plate[ys][xs]
    for i in range(8):
        for j in range(8):
            if (i)%2 == 0: #짝수번째 줄
                if j%2 == 0 and plate[ys+i][xs+j]!=start:
                    cnt +=1
                elif j%2 !=0 and plate[ys+i][xs+j]==start:
                    cnt+=1
            else:
                if j%2 == 0 and plate[ys+i][xs+j]==start:
                    cnt +=1
                elif j%2 !=0 and plate[ys+i][xs+j]!=start:
                    cnt+=1

    return cnt
'''