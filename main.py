def go():
    adj = {
        1: [2],
        2: [1, 8, 3],
        3: [2, 4],
        4: [3, 6],
        5: [7, 9],
        6: [4],
        7: [5],
        8: [2, 9],
        9: [5]
    }
    colors = {
        1: 'b',
        2: 'g',
        3: 'b',
        4: 'g',
        5: 'b',
        6: 'b',
        7: 'g',
        8: 'b',
        9: 'g'
    }
    level = {1: 0}
    parent = {1: None}
    frontier = [1]
    f = 1
    bipartite = False
    while frontier:
        next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = f
                    parent[v] = u
                    next.append(v)
                else:
                    if colors[v] == colors[u] and level[v]==level[u]:
                        bipartite = True
                        break
        if bipartite: break
        frontier = next
        f += 1
    print("the is bipartite: {}".format(bipartite))

if __name__ == '__main__':
    go()
