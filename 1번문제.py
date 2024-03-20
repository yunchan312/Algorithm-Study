arrow = list(input())
stack = []
ans = []
status = 0
cnt = 0

for i in range(len(arrow)):
    if arrow[i] == '-':
        stack.append(arrow[i])
        continue
    else:
        if len(stack) < 1:
            stack.append(arrow[i])
            continue
        else:
            if stack[0] == '<':
                if arrow[i] == '<':
                    ans.append([-1, len(stack)-1])
                    stack.clear()
                    stack.append(arrow[i])
                elif arrow[i] == '>':
                    ans.append([0, len(stack)-1])
                    stack.clear()
            else:
                if arrow[i] == '>':
                    ans.append([1, len(stack)-1])
                    stack.clear()
            continue

while(len(stack) >= 1):
    if stack[0] == '<':
        if stack[-1] == '>':
            ans.append([0, len(stack)-2])
        elif stack[-1] == '-':
            ans.append([-1,len(stack)-1])
    
print(ans)