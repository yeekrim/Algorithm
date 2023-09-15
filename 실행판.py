a,b,n = map(int,input().split())
h = 0
res = 0

while True :
    h += a
    if h>=n :
        res += 1
        break
    h -= b
    res += 1
    if h>=n :
        break

print(res)