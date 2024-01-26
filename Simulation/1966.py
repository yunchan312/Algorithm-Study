'''
프린터 큐
N => 문서의 개수 
M => 몇번째로 인쇄되는지 궁금한 문서가 현재 QUEUE에서 몇번째에 놓여있는지를 나타내는 정수

뭐지 ㅅㅂ
'''
import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    N, target = map(int, input().split())
    docu = deque(map(int, input().split()))
    curPrt = 1
    ind = deque(i for i in range(N))

    '''프린트 할 때 해당 ind가 target과 같은지 검사하는 함수'''
    def isTarget(ind):
        if ind[0] == target:
            return True
        return False

    '''현재 우선순위에 맞는건지 확인하는 함수'''
    def tryPrint(docu):
        if max(docu) == docu[0]:
            return True
        return False

    while(ind):
        if not tryPrint(docu):
            indTemp = ind.popleft()
            ind.append(indTemp)
            docuTemp = docu.popleft()
            docu.append(docuTemp)
        else:
            if isTarget(ind):
                print(curPrt)
                break
            else:
                curPrt +=1
                ind.popleft()
                docu.popleft()