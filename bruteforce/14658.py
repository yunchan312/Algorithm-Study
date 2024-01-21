'''
	N = 가로길이
	M = 세로길이
	L = 트렘펄린의 한 변의 길이
    K = 개수
'''
import sys

N,M,l,k = map(int, sys.stdin.readline().split())

ans = 0

xInd = [0 for _ in range(k)]
yInd = [0 for _ in range(k)]

for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    xInd[i] = x
    yInd[i] = y

#두 점을 선택하여, 두 점이 걸쳐지는 점을 왼쪽 아래 곡짓점으로 하여 가장 많은 별들을 튕겨낼 수 있는 배치를 찾는다.
for x in xInd:
    for y in yInd:
        cnt = 0
        for j in range(k):
            if x <= xInd[j] <= x+l and y <= yInd[j] <= y+l:
                cnt += 1
            ans = max(ans, cnt)
        
print(k-ans)#지구에 부딪히는 이었다.........



# 무식하게 모든 좌표 가보기(시간초과 뜸)
'''
for m in range(M-1, l-2, -1):
    for n in range(N-1, l-2, -1):
        cnt=0
        temp =[]
        for q in range(k):
            if xInd[q] >= (n-l) and yInd[q]<=(m-l):
                cnt += 1
            temp.append(cnt)
        ans = max(ans, cnt)

print(ans)'''

#거리로 조지기(실패)
'''
def getDist(x,y,n,m):
    return ((x-n)**2+(y-m)**2)**1/2


maxDist = (l**2+l**2)**1/2
for m in range(M-1, l-2, -1):
    for n in range(N-1, l-2, -1):
        cnt = 0
        for q in range(k):
            if getDist(xInd[q],yInd[q],n,m) <= maxDist and xInd[q] >= (n-l) and yInd[q] <= (m-l):
                cnt += 1
        ans = max(ans, cnt)

print(ans)
'''
#점 하나씩 검사해보기(4중 for문 인 것 같은데 이게 맞냐?)


