X="ABCBDAB"
Y="BDCABA"

def LCS(X, Y):
    n,m = len(X), len(Y) #n=7 m=6
    lcs = [[0 for _ in range(m+1)] for _ in range(n+1)]# 8*7 dp table 생성
    for i in range(1, n+1): # i = 1 2 3 4 5 6 7
        for j in range (1, m+1): # j = 1 2 3 4 5 6
            if X[i-1] == Y[j-1]:
                lcs[i][j] = lcs[i-1][j-1]+1
            else:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
    return lcs[n][m]


result = LCS(X, Y)
print(result)
