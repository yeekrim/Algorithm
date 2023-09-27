#1
n = int(input())
ternary_reverse = ''
ternary = ''
res = ''

while n!=0 :
    save = str(n%3)
    ternary_reverse += save
    n = n//3

for i in range(len(ternary_reverse)-1,-1,-1) :
    ternary += ternary_reverse[i]

print(ternary)
print(ternary_reverse)
print(int(ternary_reverse, 3))

#2
def desc(num) :
    num = str(num)
    res = ''
    for i in range(len(num)-1,-1,-1) :
        res += num[i]
    return res

print(desc(12345678))

#3 ㅇㄴ 머임
day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
m,d = map(int, input().split('/'))
monthstart = [31,29,31,30,31,30,31,31,30,31,30,31]

sum = 0
for i in range(m-1) :
    sum += monthstart[i]
sum += d

res = sum % 7
print(day[res-1])

#4
n = int(input())
score = list(map(int, input().split()))

sum = 0
for i in score :
    sum += i
avg = sum/n

close_avg = 1
difference1 = 0
for j in range(len(score)) :
    difference2 = score[j]-avg
    if difference2 > difference1 :
        close_avg += 1
    elif difference2 < difference1 :
        pass

print(round(avg), end=' ')
print(close_avg)

#5 
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

#6
dic = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
credit_sum = 0
sum = 0

for i in range(5) :
    sub, credit, grade = input().split()
    if grade == 'P' :
        pass
    else :
        credit_sum += float(credit)
        sum += dic[grade] * float(credit)
    
print(sum/credit_sum)

#7
n = int(input())

bag = 0
while n >= 0 :
    if n % 5 == 0 :
        bag += (n // 5)
        print(bag)
        break
    n -= 3
    bag += 1 

else :
    print('-1')

#8
import random

num = int(input())
num2 = random.randrange(1,num+1)
reslist = [num, num2]

num3 = num - num2
reslist.append(num3)
while num3 >= 0 :
    num = num2
    num2 = num3
    num3 = num-num2
    if num3 < 0 :
        break
    else :
        reslist.append(num3)

print(reslist)