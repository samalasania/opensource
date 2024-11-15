t = int(input())
for i in range(t):
    x,n = map(int,input().split())
    score = x//10
    ajay_score = score * n
    print(ajay_score)
