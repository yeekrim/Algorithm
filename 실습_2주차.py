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
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
m,d = map(int, input().split('/'))

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

#5 찌발

#6

#7
#8