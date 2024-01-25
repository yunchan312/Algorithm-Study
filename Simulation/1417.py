'''국회의원 선거'''

'''
N => 국회의원 숫자
M => 마을주민 숫자

매수해야 하는 사람의 최솟값을 출력하는 프로그램
즉, 기호 1번의 표가 제일 많게하는 매수 인간의 최솟값
'''
import sys
input = sys.stdin.readline

N = int(input())
cand = [0 for _ in range(N-1)]
dasom = int(input())
for i in range(N-1):
    cand[i] = int(input())

def isDasomMax(cand):
    global dasom
    if dasom > max(cand):
        return True
    return False

beforeDasom = dasom

if N == 1:
    print(0)
else:
    while(True):
        if isDasomMax(cand):
            break
        dasom +=1
        cand[cand.index(max(cand))] -=1


    print(dasom-beforeDasom)