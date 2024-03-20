from collections import defaultdict
from collections import deque
import itertools as iter

def getCloseChicken(chickens, house):
  cur_min = 1000000000
  theChicken = (0,0)
  for chi_row, chi_col in chickens:
    if cur_min > abs(chi_row-house[0]) + abs(chi_col-house[1]):
      cur_min = abs(chi_row-house[0]) + abs(chi_col-house[1])
      theChicken = (chi_row, chi_col)
  return theChicken

def getChickenDist(chicken, house):
  return abs(chicken[0]-house[0])+abs(chicken[1]-house[1])


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
#print(list(MChickens[0]))
for i in MChickens:
    print(getChickenDist(list(MChickens[i]), houses))

def getCityChickenDist(chickens, houses):
  combi = defaultdict(deque)
  for house in houses:
    combi[getCloseChicken(chickens, house)].append(house)

  cityChickenDist = 0

  for chi_row, chi_col in combi:
    for homes in combi[(chi_row, chi_col)]:
      cityChickenDist += getChickenDist((chi_row, chi_col), homes)
  return cityChickenDist