def fibo1(n): #recursion
    if n <= 1:
        return 1
    return fibo1(n-1) + fibo1(n-2)

def fibo(n): #Dynamic Programming
    dp = [0]*(n+1)
    dp[1] = 1
    for k in range(2, n+1):
        dp[k] = dp[k-1] + dp[k-2]
    return dp[n]

result = fibo(5)
print(result)