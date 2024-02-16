'''ATM'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
ans = 0
times.sort()
for x in range(1,N+1):
    ans += sum(times[:x])
print(ans)