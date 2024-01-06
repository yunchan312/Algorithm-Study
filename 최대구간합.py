A = [1,-1,3,-4,5,-4,6,-2]
'''
DP를 활용해서 구하기
dp[j] = A[j]로 끝나는 구간 중 최대합.
'''
dp = [A[0]]

for i in range(1, len(A)):
    dp.append(max(dp[i-1] + A[i], A[i]))

print(max(dp))