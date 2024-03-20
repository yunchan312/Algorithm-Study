n, m, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
num1 = l[0]
num2 = l[1]
split = num1*k+num2
t = m//(k+1)
count = split*t
rest = m%(k+1)
count += rest*num1

print(count)