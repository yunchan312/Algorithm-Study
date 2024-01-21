'''
    특정거리의도시찾기
    N => 도시의 개수
    M => 도로의 개수
    K => 거리정보
    X => 출발 도시의 번호
'''
n,m,k,x = map(int, input().split())
cities = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    cities[a-1].append(b-1)

visited = [False for _ in range(n)]
    