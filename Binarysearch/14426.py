'''접두사 찾기'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
strings = [input().strip() for _ in range(N)]
texts = [input().strip() for _ in range(M)]
cnt = 0

for text in texts:
    for string in strings:
        if string[0] == text[0]:
            if string[:len(text)] == text:
                cnt +=1
                break
print(cnt)