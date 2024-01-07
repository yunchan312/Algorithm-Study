#숫자 정사각형
n , m = map(int, input().split())


arr = [input() for _ in range(n)]
ans = set()
for i in range(n):
    for j in range(m):
        for k in range(min(n,m)):
            if j+k>=m:
                continue
            if i+k>=n:
                continue

            if arr[i][j] == arr[i+k][j] == arr[i][j+k] == arr[i+k][j+k]:
                ans.add(k)

print((max(ans)+1)**2)