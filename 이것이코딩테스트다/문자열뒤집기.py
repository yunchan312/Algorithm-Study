from collections import deque

S = input().strip()
zero, one = 0, 0
temp = deque()
temp.append(S[0])
for i in range(1,len(S)):
    if temp[0] == S[i]:
        temp.append(S[i])
    else:
        if temp.pop() == '0':
            zero += 1
        else:
            one +=1
        temp.clear()
        temp.append(S[i])
if len(temp)>0 and temp.pop() == '0':
    zero += 1
elif len(temp)>0 and temp.pop() == '1':
    one +=1

print(min(one, zero))