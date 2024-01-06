'''
A가 B의 2-친구가 되기 위해서,
    1. 두 사람이 친구
    2. A와 친구이고 B와 친구인 C
'''
person = int(input())
g=[]
for _ in range(person):
    g.append(input())

graph = [[] for _ in range(person)]
for y in range(person):
    for x in range(person):
        if g[y][x] == 'Y':
            graph[y].append(x)

twoFriend = [0 for _ in range(person)]

for i in range(person):
    friend = set()
    for j in graph[i]:
        friend.add(j)
        for k in graph[j]:
            friend.add(k)
    if len(friend) == 0:
        twoFriend[i] = 0
    else:
        twoFriend[i] = len(friend)-1

print(max(twoFriend))

'''
#길이 2 탐색
for i in range(person):
    twoFriend[i] += len(graph[i])
    for j in range(len(graph[i])):
        temp = graph[i][j]
        tempArr = graph(temp)
        for k in range(len(tempArr)):
            if isNotFriend(tempArr[k],graph[i]) and tempArr[k] != i:
                twoFriend += 1'''




