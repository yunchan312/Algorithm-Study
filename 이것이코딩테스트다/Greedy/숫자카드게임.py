N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

maxNum = -1
for card in cards:
    maxNum = max(maxNum, min(card))

print(maxNum)