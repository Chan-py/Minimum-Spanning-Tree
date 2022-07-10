import sys
input = sys.stdin.readline

def find(x):
    if par[x] == -1:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def merge(a, b):
    a = find(a)
    b = find(b)
    if par[a] > par[b]:
        a, b = b, a
    
    if a != b:
        par[b] = a
        return True
    else:
        return False

V, E = map(int, input().split())
par = [-1 for _ in range(V+1)]
graph = []
for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append((C, A, B))
graph.sort()
sum = 0
for x, a, b in graph:
    if merge(a, b):
        sum += x
print(sum)