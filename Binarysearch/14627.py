'''파닭파닭'''
import sys
input = sys.stdin.readline
S,C = map(int, input().split())
P = [int(input()) for _ in range(S)]
start = 1
end = max(P)
ans = 0
while start <= end:
    mid = (start+end)//2
    cnt = sum(p//mid for p in P)
    if cnt >= C:
        ans = max(ans, mid)
        start = mid+1
    else:
        end = mid-1

print(sum(P)-(C*ans))
