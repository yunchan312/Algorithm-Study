'''블랙프라이데이'''
import sys
input = sys.stdin.readline

N,C = map(int, input().split())
weight = list(map(int, input().split()))

def binarySearch(target, start, end):
    if start >= end:
        return False
    pivot = (start+end)//2
    if weight[pivot] == target:
        return True
    elif weight[pivot] > target:
        end = pivot-1
    else:
        start = pivot+1
    return binarySearch(target, start, end)
ans = 0
temp = set()
weight.sort()


def event(weight,N,C):
    #하나를 고를 때
    if binarySearch(C, 0, N-1):
        return True
    #두개를 고를 때
    for i in range(N):
        if binarySearch(C-weight[i],i,N-1):
            return True
    #세개를 고를 경우
        else:
            for j in range(i+1, N):
                wSum = weight[i]+weight[j]
                if wSum < C:
                    tempTarget = C - wSum
                    if binarySearch(tempTarget, j, N-1):
                        return True
    return False



if event(weight, N,C):
    print(1)
else:
    print(0)

