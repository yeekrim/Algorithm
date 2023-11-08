#1
class disjointSets :
    def __init__(self,n) :
        self.parent = [-1]*n
        self.set_size = n
    def find(self, id) :
        while (self.parent[id] >= 0) :
            id = self.parent[id]
        return id
    def union(self,s1,s2) :
        self.parent[s1] = s2
        self.set_size = self.set_size -1

INF = 9999
def getMinVertex(dist, selected) :
    minv = -1
    mindist = INF
    for v in range(len(dist)) :
        if not selected[v] and dist[v]<mindist :
            mindist = dist[v]
            minv = v


def MSTKruskal(V, adj) :
    n = len(V)
    dsets = disjointSets(n)
    E = []
    for i in range(n-1) :
        for j in range(i+1, n) :
            if adj[i][j] != None :
                E.append((i,j,adj[i][j]))
    
    E.sort(key=lambda e : e[2])
    ecount = 0
    for i in range(len(E)) :
        e = E[i]
        uset = dsets.find(e[0])
        vset = dsets.find(e[1])

        if uset != vset :
            dsets.union(uset,vset)
            print("간선 추가")
            ecount += 1
            if ecount == n-1 :
                break

def MSTdijkstra(vtx, adj, start) :
    vsize = len(vtx)
    dist = list(adj[start])
    dist[start] = 0
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True

    for i in range(vsize) :
        print("Step%2d : " % (i+1),dist)
        u = getMinVertex(dist, found)
        found[u] = True

        for w in range(vsize) :
            if not found[w] :
                if dist[u] + adj[u][w] < dist[w] :
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u
    
    return path

#2
works = [93,30,55]
speeds = [1,30,5]

works2 = [95,90,99,99,80,99]
speeds2 = [1,1,1,1,1,1]

res = []

while len(works) != 0 :
    cnt = 0

    while works[0] >= 100 :
        del works[0]
        cnt += 1
        if len(works) == 0 :
            break
    if cnt != 0 :
        res.append(cnt)
        cnt = 0
    
    for work, speed in zip(works, speeds) :
        works[cnt] += speed
        cnt += 1

print(res)

#3
n = int(input())
lst = []
for _ in range(n) :
    num = int(input())
    lst.append(num)

stack = []
max_v = 0
for i in range(n) :
    idx = i
    while stack and stack[-1][1] > lst[i] :
        idx, height = stack.pop()
        res = (i-idx) * height
        max_v = max(max_v, res)
    stack.append([idx, lst[i]])

while stack :
    idx, height = stack.pop()
    res = (n-idx) * height
    max_v = max(max_v, res)

print(max_v)

#4
V = int(input())
E = int(input())
edges = [] 

for _ in range(E):
    edges.append(list(map(int, input().split()))) 

root = dict()
for i in range(1, V+1):    
    root[i] = i 
    
def find(x):    
    if root[x] == x:        
        return x    
    else:        
        root[x] = find(root[x])        
        return root[x] 
        
def union(x, y):   
    x = find(x)    
    y = find(y)
    root[y] = x

edges = sorted(edges, key=lambda x: x[2])
total_cost = 0
for edge in edges:
    if find(edge[0]) == find(edge[1]):        
        continue    
    else:        
        total_cost += edge[2]        
        union(edge[0], edge[1]) 

print(total_cost)

