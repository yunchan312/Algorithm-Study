'''영화감독 숌'''

def howLong(X):
	length = 0
	while(X>0):
		X //= 10
		length += 1
	return length

def isDevilNum(X):
    for i in range(howLong(X)):
        if (X//(10**i))%10 == 6 and (X//(10**(i+1)))%10 == 6 and (X//(10**(i+2)))%10 ==6:
            return True
    return False

n = int(input())
cnt = 1
temp = 666
while(n != cnt):
    temp += 1
    if isDevilNum(temp) == True:
        cnt += 1

print(temp)