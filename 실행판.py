day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
m,d = map(int, input().split('/'))

res = int((16+(16/4)+(20/4)-2*20+(26*(m+1)//10)+d)%7)

print(res)