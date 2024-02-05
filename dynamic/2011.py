'''암호코드'''
import sys
input = sys.stdin.readline


code = (input())
print(int(code[1]+code[0]))
if int(code) <= 0:
    print(0)
else:
    dp = [0 for _ in range(len(code)-1)]
    dp[0] = 1
    if len(code) == 1:
        print(dp[0])

    if len(code) >= 2:
        if int(code[0]+code[1]) <= 26 and int(code[0]+code[1]) >= 10:
            dp[1] = 2
        else:
            dp[1] = 1
        for i in range(2,len(code)-1):
            if int(code[i-1]+code[i-2])<=26 and int(code[i-1]+code[i-2]) >= 10:
                dp[i] += dp[i-2]
            if int(code[i]) > 0:
                dp[i] += dp[i-1]
        print(dp[-1]%1000000)

