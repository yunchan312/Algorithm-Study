'''
악수
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
dp[0]=1
dp[1]=2
ind=2

while(ind < N):
    dp[ind]=(dp[ind-1]+dp[ind-2])%10
    ind+=1

print(dp[ind-1])