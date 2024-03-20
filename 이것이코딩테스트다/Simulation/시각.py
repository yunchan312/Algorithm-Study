def is3Contain(clock):
  if '3' in clock:
    return True
  return False
cnt =0
N = int(input())
for h in range(N+1):
  for m in range(60):
    for s in range(60):
      temp = str(h) + ':' + str(m) + ':' + str(s)
      if is3Contain(temp):
        cnt+=1
print(cnt)