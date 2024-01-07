'''
	N = 별똥별이 떨어지는 구역의 가로길이
	M = 세로길이
	L = 트렘펄린의 한 변의 길이
    K = 개수
'''

n,m,l,k = map(int, input().split())

xInd = []
yInd = []
for i in range(k):
    x, y = map(int, input().split())
    xInd.append(x)
    yInd.append(y)

print(xInd)
print(yInd)