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

#6 오름차순으로 나오는 문제만 해결하면 됨
string = input()

for num, letter in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine','ten']) :
    if letter in string :
        print(num, end='')

#7
a,b = input().split()
a = list(a)
b = list(b)

a[0],a[2] = a[2],a[0]
b[0],b[2] = b[2],b[0]

for i in range(3) :
    if a[i] > b[i] :
        print(a[0],a[1],a[2])
        break
    elif a[i] == b[i] :
        continue
    else :
        print(b[0],b[1],b[2])

#8

#9
#10