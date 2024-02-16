'''볼 모으기'''
'''진심으로 왜 15점인지 모르겠음'''

l = int(input())
balls = input()

std = balls[-1]
first = False
thel = 0
cnt = 0
for i in range(l-2,-1,-1):
    if balls[i] != std:
        if first == False:
            first = True
            thel = i+1
        cnt +=1

print(min(cnt, thel-cnt))
