#black jack
'''
n개의 카드 중 M을 넘지 않으면서 최대한 M에 가깝게 3장 뽑기
'''
n,m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if cards[i]+cards[j]+cards[k] <= m:
                result = max(cards[i]+cards[j]+cards[k], result)

print(result)