'''평범한 배낭'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
W = [0 for _ in range(N)]
V = [0 for _ in range(N)]
maxValue = 0
for i in range(N):
    W[i],V[i] = map(int, input().split())

def backpack(weight, value, i):
    global maxValue
    if i >= N:
        return
    if weight+W[i]<=K:
        maxValue = max(value+V[i], maxValue)
        backpack(weight+W[i],value+V[i], i+1)
    backpack(weight, value, i+1)

backpack(0,0,0)
print(maxValue)