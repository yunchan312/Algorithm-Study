'''설탕배달'''

n = int(input())

dp = [0 for _ in range(n+1)]
dp[0] = 1

i = 1
while(True):
    if i > n:
        break
    #둘 다 0이 아니면 더 작은 것을 고른다.
    if dp[i-5] != 0 and dp[i-3] != 0:
        dp[i] = min(dp[i-5], dp[i-3])
    #둘 다 0이거나 하나만 0이면 더 큰것을 고른다.
    else:
        dp[i] = max(dp[i-5], dp[i-3])

    if dp[i] != 0 and i >= 6:
        dp[i] += 1
    i += 1

if dp[-1] == 0:
    print(-1)
else:
    print(dp[-1])
