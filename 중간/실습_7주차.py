#1
N,M,V = map(int,input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0]*(N+1)
visited2 = visited1.copy()

def dfs(V):
    visited1[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(V):
    queue = [V]
    visited2[V] = 1
    while queue:
        V = queue.pop(0) 
        print(V, end = ' ')
        for i in range(1, N+1):
            if(visited2[i] == 0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1

dfs(V)
print()
bfs(V)

#2
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

n = int(input())
tree = {}
    
for _ in range(n):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')

#3
import heapq

k=int(input())
s=list(map(int,input().split(',')))
heapq.heapify(s)
h=[]

cnt=0
while 1:
  cnt += 1
  i = s[0]
  heapq.heappop(s)
  heapq.heapify(s)
  j = s[0]

  if i+j*2 < k :
    heapq.heappush(h,i+j*2)
  else:
    heapq.heappush(h,i+j*2)
    break

print(cnt)

#4
ans = ""
tag = False
stack = ""
for i in input():
    if i == "<":
        tag = True
        ans += stack[::-1]
        stack = ""
        ans += i
        continue
    elif i == ">":
        tag = False
        ans += i
        continue
    elif i == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue
        
    if tag:
        ans += i
    else:
        stack += i
print(ans+stack[::-1])

#5
N, W, L = map(int, input().split())
truck_list = list(map(int, input().split()))


time = 0
index = 0

while(index < len(truck_list)):
    truck_queue = []
    for i in range(index, len(truck_list)):
        if sum(truck_queue) + truck_list[i] <= L:
            truck_queue.append(truck_list[i])
            index += 1
        else:
            break

    print(truck_queue)
    time += (W + len(truck_queue)-1)

time += 1

print()
print(time)