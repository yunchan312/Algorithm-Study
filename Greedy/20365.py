'''블로그2'''

l = int(input())
string = input()
R_time, B_time = 1,1

if string[0] == 'B':
    B_time +=1
if string[0] == 'R':
    R_time +=1

for i in range(1, l):
    if string[i] == string[i-1]:
        continue
    elif string[i] == 'R' and string[i] != string[i-1]:
        R_time +=1
    elif string[i] == 'B' and string[i] != string[i-1]:
        B_time +=1
print(min(R_time, B_time))
