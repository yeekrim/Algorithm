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
#4
for i in range(5,0,-1) :
cnt = (2*i)-1
print(("*"*cnt).center(9))
for i in range(2,6) :
cnt = (2*i)-1
print(("*"*cnt).center(9))