#2주차 9번
n = int(input())
res = n

for i in range(n) :
    string = input()
    for j in range(len(string)-1) :
        if string[j] == string[j+1] :
            continue
        elif string[j] in string[j+1:] :
            res -= 1
            break

print(res)

#3주차 5번
n, k = map(int, input().split())
num = [i for i in range(1,n+1)]
res = []

index = -1
for _ in range(n) :
    index += k
    if index > len(num) :
        while index >= len(num) :
            index -= len(num)
    res.append(num[index])
    num.pop(index)
    index -= 1

print(res)

#4주차 5번
n = int(input())
length = []

for i in range(n) :
    string = str(input())
    if [len(string),string] in length :
        pass
    else :
        length.append([len(string), string])

length = sorted(length)

for i in range(len(length)) :
    print(length[i][1])