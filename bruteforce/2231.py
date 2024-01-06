'''분해합
어떤 자연수 M의 분해합이 N인 경우, N의 생성자 M
즉 분해합을 N이 어떤 수의 분해합이라면 그 수의 생성자이다.

N이 주어졌을 때 N의 가장 작은 생성자는?
즉 분해합이 N인 숫자 중 최소값은?
'''

N = int(input())
def intSum(n): #자릿수들의 합을 구해주는 함수
    temp = n
    sum = 0
    while(temp >= 10):
        sum += temp %10
        temp = temp//10
    sum += temp
    return sum

for i in range(N+1):
    if intSum(i)+i == N:
        print(i)
        break
    if i==N:
        print(0)