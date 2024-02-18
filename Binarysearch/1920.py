'''수찾기'''
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

def binarySearch(b, start, end):
    if start > end:
        return 0
    p = (start + end)//2
    if A[p] == b:
        return 1
    elif A[p] > b:
        end = p-1
    else:
        start = p+1
    return binarySearch(b,start,end)

A.sort()
for b in B:
    print(binarySearch(b,0,len(A)-1))