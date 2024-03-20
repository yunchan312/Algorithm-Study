n = int(input())
h = list(map(int, input().split()))

cnt = 0
if sum(h)%3 != 0:
    print("NO")
else:
    for i in h:
        cnt += i // 2 #2번 물뿌리개를 사용한 횟수
    if cnt < (sum(h) / 3):
        print("NO")
    else:
        print("YES")