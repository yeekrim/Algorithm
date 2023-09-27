n, k = map(int, input().split())
num = [i for i in range(1,n+1)]
res = []

index = -1

while num != 0 :
    index += k
    if index > n-1 :
        index -= n-1
    res.append(num[index])
    num.remove(num[index])



print(res)