'''스티커'''
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    dp = [[0 for _ in range(N)] for _ in range(2)]
    sticker = [list(map(int, input().split())) for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if N == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    dp[0][1] = sticker[0][1]+sticker[1][0]
    dp[1][1] = sticker[1][1]+sticker[0][0]
    if N == 2:
        print(max(dp[0][1], dp[1][1]))
        continue



    for x in range(2, N):
        dp[0][x] = sticker[0][x] + max(dp[1][x-1], dp[1][x-2])
        dp[1][x] = sticker[1][x] +  max(dp[0][x-1], dp[0][x-2])
    print(max(dp[0][-1],dp[1][-1]))

