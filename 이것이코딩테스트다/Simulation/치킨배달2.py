from collections import deque
import itertools as iter

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chickens, houses = deque(),deque()
for r in range(N):
  for c in range(N):
    if city[r][c] == 1:
      houses.append((r,c))
    elif city[r][c] == 2:
      chickens.append((r,c))

MChickens = deque(iter.combinations(chickens, M))

# chickens = [(1,0), (1,3)]
def getCityChickenDist(chickens, houses):
  cityChickenDist = 0
  for h_row, h_col in houses:
    cur_min=10000000
    for c_row, c_col in chickens:
      if cur_min > abs(h_row-c_row)+abs(h_col-c_col):
        cur_min = abs(h_row-c_row)+abs(h_col-c_col)
    cityChickenDist += cur_min
  return cityChickenDist

answer = 100000000000
for chickens in MChickens:
  answer = min(answer, getCityChickenDist(list(chickens), houses))
print(answer)

