'''from scipy.stats import norm
import math

# Z-스코어 값에 따른 누적 분포 함수 값 계산
cdf_value1 = norm.cdf((math.log(6, math.e)-2.3)/(0.2))
cdf_value2 = norm.cdf(0.3*(10**0.5))
cdf_value3 = norm.cdf((145.5-(1000/6))/((5000/36)**0.5))
#ppf = critical point(임계치)
ppf_value = norm.ppf(0.5)

result = cdf_value2 - cdf_value3
print(cdf_value2*2 - 1)

'''
'''
def getMaxArea(buildings):#최대 넓이를 구하는 함수
	stack = []#현재의 buildings 높이의 인덱스를 저장하는 stack
	maxArea = 0

	for i in range(len(buildings)):
		while stack and buildings[i] < buildings[stack[-1]]:#stack이 비어있지 않으면, building[i] < building[stack[-1]]
			height = buildings[stack.pop()] #높이 = stack에 저장해둔 높이
			width = i if not stack else i - stack[-1] - 1 #stack이 비어있으면 width = i stack이 차있으면 i 부터 stack[-1]까지의 길이
			maxArea = max(maxArea, height * width) #maxArea를 구함
		stack.append(i)

	while stack: #stack이 비어있지 않다면 stack이 빌 때까지 위 과정을 반복함
		height = buildings[stack.pop()]
		width = len(buildings) if not stack else len(buildings) - stack[-1] - 1
		maxArea = max(maxArea, height * width)

	return maxArea

n = int(input())
buildings = list(map(int, input().split()))
result = getMaxArea(buildings)
print(result)
'''

'''
	수행시간 간략히 분석하고 Big-O로 표기
	
	첫번째 ㄹ
	
'''
'''a = [1,2,3,4]
if 5 in a:
    print('yes')'''

'''apples=[(1,2),(3,4),(5,6)]
for ind, A in enumerate(apples):
    ay, ax = A
    print(ind, ay, ax)'''
'''from collections import deque

apples=deque([1,2,3])
apples.append(4)
print(apples)
apples.pop()
print(apples)
if 10 not in apples:
    print(1)'''

'''dp = [(10,3), (11,2), (12,1), (0,13)]
print(max(dp))'''

for i in range(10):
    if i == 3:
        print(3)
        break
    print(4)