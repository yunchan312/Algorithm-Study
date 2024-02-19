'''접두사 찾기'''
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
strings = [input().strip() for _ in range(N)]
texts = deque()
for _ in range(M):
    texts.append(input().strip())


