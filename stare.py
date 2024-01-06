'''
계단 오르기 문제
<한번에 계단을 1칸 or 2칸을 오를 수 있다.>

f(n) = n번째 칸까지 갈 수 있는 경우의 수
f(6) = f(5) + f(4)

따라서 f(n) = f(n-1) + f(n-2)
'''
def goUpStare(n):
    stare = [0] * (n+1)

    stare[2] = 1
    stare[3] = 2

    for k in range(4, n+1):
        stare[k] = stare[k-1] + stare[k-2]
    return stare[n]

print(goUpStare(6))
