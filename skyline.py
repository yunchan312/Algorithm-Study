'''
    가장 낮은 층부터 시작,
    각각의 층에서 최대 너비를 구한다.
    그 너비 * 층수  = currentMaxArea
    maxArea = max(currentMaxArea, maxArea)
'''
def getMaxArea(building):
    maxArea = 0
    for k in range(min(building), max(building)+1):
        maxArea = max(maxArea, currentMaxArea(building, k))
    return maxArea

def currentMaxArea(building, k):
    w = []
    if building[0] >= k:
        w.append(1)
    else:
        w.append(0)
    for i in range(1, len(building)):
        if building[i] < k:
            w.append(0)
        else:
            w.append(w[i-1] + 1)
    return max(w)*k

n = int(input())
building = int(input().split())
print(building)

'''
big-o 계산
getMaxArea함수에서 (빌딩의 최대높이 - 빌딩의 최소높이) = K 만큼
currentMaxArea함수를 반복
currentMaxArea함수는 building리스트의 길이 n만큼 반복한다.
따라서 수행시간은 O(K*n)로, pseudo polynomial 수행시간을 갖는다.

'''