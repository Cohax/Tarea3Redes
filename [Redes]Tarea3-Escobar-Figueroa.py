import pdb

def initialize(graph, source):
    d = {} 
    p = {} 
    for node in graph:
        d[node] = float('Inf') 
        p[node] = None
    d[source] = 0
    return d, p
 
def relax(node, neighbour, graph, d, p):
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node
 
def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): 
        for u in graph:
            for v in graph[u]: 
                relax(u, v, graph, d, p) 
 
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]
 
    return d, p
 
 
def test():

    final1 = [[None] * 11 for i in range(11)]

    final2 = [[None] * 11 for i in range(11)]

    matriz = []
    matriz = ['pc', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'se']
    
    preg2 = {
        'pc': {'a': 3},
        'a': {'pc': 3, 'b': 1, 'g': 4, 'i': 10},
        'b': {'a': 1, 'c': 9, 'e': 8},
        'c': {'b': 9, 'd': 2},
        'd': {'c': 2, 'e': 9, 'f': 4, 'i': 2},
	'e': {'b': 8, 'd': 9, 'f': 2, 'i': 1},
        'f': {'d': 4, 'e': 2, 'h': 6},
        'g': {'a': 4, 'h': 7},
        'h': {'f': 6, 'g': 7, 'i': 3},
        'i': {'a': 10, 'd': 2, 'e': 1, 'h': 3, 'se': 1},
	'se': {'i': 1}
        }

    preg3 = {
        'pc': {'a': 3},
        'a': {'pc': 3, 'b': 1, 'g': 4, 'i': 10},
        'b': {'a': 1, 'c': 9, 'e': 8},
        'c': {'b': 9, 'd': 2},
        'd': {'c': 2, 'e': 9, 'f': 4, 'i': 2},
	'e': {'b': 8, 'd': 9, 'f': 2, 'i': 1},
        'f': {'d': 4, 'e': 2, 'h': 6},
        'g': {'a': 4, 'h': 7},
        'h': {'f': 6, 'g': 7},
        'i': {'a': 10, 'd': 2, 'e': 1, 'se': 1},
	'se': {'i': 1}
        }
		
     
    for b in matriz:
        d, p = bellman_ford(preg2, b)
        preg2[b]=d
        

    for c in matriz:
        d, p = bellman_ford(preg3, c)
        preg3[c]=d

    a=0
    for flag1 in matriz:
        b=0
        for flag2 in matriz:
            
            
            final1[a][b]= preg2[flag1][flag2]
            b+=1
        a+=1


    a=0
    for flag1 in matriz:
        b=0
        for flag2 in matriz:
            
            
            final2[a][b]= preg3[flag1][flag2]
            b+=1
        a+=1


    print "-----------PREG 2------------"
    print final1[0]
    print final1[1]
    print final1[2]
    print final1[3]
    print final1[4]
    print final1[5]
    print final1[6]
    print final1[7]
    print final1[8]
    print final1[9]
    print final1[10]

    print "-----------PREG 3------------"
    print final2[0]
    print final2[1]
    print final2[2]
    print final2[3]
    print final2[4]
    print final2[5]
    print final2[6]
    print final2[7]
    print final2[8]
    print final2[9]
    print final2[10]

if __name__ == '__main__': test()
