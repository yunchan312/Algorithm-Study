#수 이어가기
'''
두번째 수는 양의 정수 중에서 하나를 선택한다.
세번째 이후에 나오는 모든 수는 앞의 앞의 수에서 앞의 수를 빼서 만든다.
음의 정수가 만들어지면 이 음의 정수를 버리고 더 이상 수를 만들지 않는다.
'''

n = int(input())
ans = []
for i in range(n+1):
    anslist =[]
    anslist.append(n)
    anslist.append(i)
    while(True):
        tempInd = len(anslist)-1
        appendnum = anslist[tempInd-1]-anslist[tempInd]
        if appendnum < 0:
            break
        else:
            anslist.append(appendnum)
    
    if len(ans) < len(anslist):
        ans = anslist
    
print(len(ans))
ansString=""
for k in range(len(ans)):
    ansString += (str(ans[k]) + " ")
print(ansString)