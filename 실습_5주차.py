#1
#2
array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]
res = []

def oneres(array, cmd) :
    i = cmd[0]; j = cmd[1]; k = cmd[2]
    resary = array[i-1:j]
    sortedary = quick_sort(resary)
    return sortedary[k-1]

for i in range(len(commands)) :
    cmd = commands[i]
    res.append(oneres(array, cmd))

print(res)

#3
#4
#5
#6
#7