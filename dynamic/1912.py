'''연속합'''
N = int(input())
l = list(map(int, input().split()))
dp =[0 for _ in range(N)]
dp[0] = l[0]

for i in range(1,N):
    dp[i] = max(l[i], dp[i-1]+l[i])

print(max(dp))