#1
a =input()
c =a.upper()
d =list(set(c))
cnt = []

for i in d:
   cnt.append(c.count(i))


if cnt.count(max(cnt)) >=2:
   print("?")
else:
   print(d[cnt.index(max(cnt))])

#2
a, b =map(int, input().split())
numarr = []

for i in range(b) :
    for j in range(i) :
        numarr.append(i)

print(sum(numarr[a-1:b]))

#3
length = 0
cnt = 1
arr = []

for i in range(5):
  word = input()
  arr.append(word)
  length = max(len(word), length)

for i in range(length):
  for j in range(5):
    if i <= len(arr[j]) - 1:
      print(arr[j][i], end = "")
    else:
      continue

#4
for i in range(5,0,-1) :
    cnt = (2*i)-1
    print(("*"*cnt).center(9))
for i in range(2,6) :
    cnt = (2*i)-1
    print(("*"*cnt).center(9))

#5
num = int(input("number : "))
n = int(input("n : "))
m = int(input("m : "))

if num % n == 0 & num % m ==0 :
    print("1")
else :
    print("0")

#6 
number_en = ['zero','one','two','three','four','five','six','seven','eight','nine']
numlist = dict(enumerate(number_en, 0))

string = input()

for num, letter in numlist.items() :
    string=string.replace(letter,str(num))

print(string)

#7
a,b = input().split()
a = list(a)
b = list(b)

for i in range(2,0,-1) :
    if a[i] > b[i] :
        print(a[2], end ='')
        print(a[1], end ='')
        print(a[0], end ='')
        break
    elif a[i] == b[i] :
        continue
    else :
        print(b[2], end ='')
        print(b[1], end ='')
        print(b[0], end ='')
        break

#8
num = int(input())
record = []
entered = []

for i in range(num) : 
    a = input().split()
    record.append(list(a))

for j in range(len(record)) :
    if record[j][1] == 'enter' :
        entered.append(record[j][0])
    elif record[j][0] in entered and record[j][1] == 'leave' :
        entered.remove(record[j][0])
    else :
        pass

for k in range(len(entered)) :
    print(entered[k])

#9
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

#10
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