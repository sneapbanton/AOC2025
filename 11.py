from collections import defaultdict
from functools import cache

@cache
def bfs(src, goal):
    global adj
    if src == goal:
        return 1
    
    score = 0
    for neigh in adj[src]:
        res = bfs(neigh, goal) 
        score += res
    
    return score


@cache
def bfs2(src, goal, visited):
    global adj
    if src in ["fft", "dac"]:
        visited = list(visited)
        visited.append(src)
        visited = tuple(visited)
        
    if src == goal:
        if len(visited) != 2:
            return 0
        return 1
    
    score = 0
    for neigh in adj[src]:
        res = bfs2(neigh, goal, visited) 
        score += res
    
    return score

adj = defaultdict(lambda:[])
def p1():

    f = open("d11.txt")
    
    for line in f:
        src, dsts = line.split(":")
        dsts = [x if "\n" not in x else x[:-1] for x in dsts[1:].split(" ")]
        adj[src] = dsts

    print(bfs("you", "out"))

def p2():

    f = open("d11.txt")
    
    for line in f:
        src, dsts = line.split(":")
        dsts = [x if "\n" not in x else x[:-1] for x in dsts[1:].split(" ")]
        adj[src] = dsts

    print(bfs2("svr", "out", tuple([])))


p2()