'''수리공 항승'''
from collections import deque

N, L = map(int, input().split())
h = deque(map(int, input().split()))

def quicksort(A):
    if len(A) <= 1: return A
    pivot = A[0]
    s,m,l = [],[],[]
    for x in A:
        if x < pivot: s.append(x)
        elif x > pivot: l.append(x)
        else: m.append(x)
    return quicksort(s) + m + quicksort(l)

holes = quicksort(h)
cnt = 1
tempStd = holes[0]-0.5+L
for i in range(N):
    if holes[i] < tempStd:
        continue
    else:
        tempStd = holes[i]-0.5+L
        cnt +=1

print(cnt)

    