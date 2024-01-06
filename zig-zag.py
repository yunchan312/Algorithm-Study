A = [1,-1,3,-4,5,-4,6,-2]
#미완성
def zigZag(A): 
    high = [0]*(len(A)+1)
    high[0] = 1
    low = [0]*(len(A)+1)
    low[0] = 1
    t = len(A)
    for i in range(t):
        for j in range(t):
            if i > j and A[j] > A[i]:
                temp = high[:j+1]
                low[i] = max(temp+1)
            elif i>j and A[j] < A[i]:
                temp = low[:j+1]
                high[i] = max(high+1)
    return max(max(high), max(low))



