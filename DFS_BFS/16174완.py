'''점프왕 젤리'''

n = int(input())

plate = [0 for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    plate[i] = list(map(int, input().split()))

#런타임에러, visited 추가하니까 통과함
y,x=0,0
def jelly(plate, y, x):
    temp = plate[y][x]
    visited[y][x] = True
    if temp == -1:
        return True
    if(y+temp < n and not visited[y+temp][x]):
        if jelly(plate, y+temp,x) == True:
            return True
    if(x+temp < n and not visited[y][x+temp]):
        if jelly(plate, y, x+temp) == True:
            return True
    return False

if jelly(plate, y, x) == True:
    print("HaruHaru")
else:
    print("Hing")
