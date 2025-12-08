import math
from collections import defaultdict
from tqdm import tqdm

def dist(p1, p2):
    x1,y1,z1 = p1
    x2,y2,z2 = p2
    return  math.sqrt(pow(x2-x1,2)+pow(y2-y1,2)+pow(z2-z1,2))

def circ_str(p1):
    return f"{p1[0]},{p1[1]},{p1[2]}"

def circ_comb(p1, p2):
    p12 = circ_str(p1)+"-"+circ_str(p2)
    p21 = circ_str(p2)+"-"+circ_str(p1)
    return p12, p21

def str_circ(p):
    p1, p2 = p.split("-")
    x,y,z = map(int,p1.split(","))
    p1 = (x,y,z)
    x,y,z = map(int,p2.split(","))
    p2 = (x,y,z)
    return p1, p2

def p1():
    f = open("d8.txt")
    circuits = []
    for line in f:
        x,y,z = map(int,line.split(","))
        circuits.append((x,y,z))

    dists = defaultdict(lambda: 0)
    sorted_dist = []
    for c1 in tqdm(circuits):
        for c2 in circuits:
            if c1==c2:
                continue
            c12, c21 = circ_comb(c1,c2)
            if not dists[c12]:
                d = dist(c1, c2)
                dists[c12] = d
                dists[c21] = d
                sorted_dist.append((d, c12))

    clusters = []
    connections = []
    sorted_dist = sorted(sorted_dist, key=lambda x: x[0], reverse=False)
    for i in tqdm(range(1000)):
        d, c12 = sorted_dist.pop(0)
        c1,c2 = str_circ(c12)
        connections.append((c1,c2))
    
    for c1,c2 in connections:
        added = False
        for cluster in clusters:
            if c1 in cluster or c2 in cluster:
                added = True
                break
        if not added:
            cluster = set()
            cluster.add(c1); cluster.add(c2)
            clusters.append(cluster)
            changed = True
            while(changed):
                changed = False
                for d1,d2 in connections:
                    if (c1==d1 and c2==d2) or (d1 in cluster and d2 in cluster):
                        continue
                    if d1 in cluster or d2 in cluster:
                        cluster.add(d1); cluster.add(d2)
                        changed = True
    lens = [len(x) for x in clusters]
    result = 1
    for i, l in enumerate(sorted(lens, reverse=True)):
        result = result*l
        print(l)
        if i == 2:
            break
    print(result)


def p2():
    f = open("d8.txt")
    circuits = []
    for line in f:
        x,y,z = map(int,line.split(","))
        circuits.append((x,y,z))

    dists = defaultdict(lambda: 0)
    sorted_dist = []
    for c1 in tqdm(circuits):
        for c2 in circuits:
            if c1==c2:
                continue
            c12, c21 = circ_comb(c1,c2)
            if not dists[c12]:
                d = dist(c1, c2)
                dists[c12] = d
                dists[c21] = d
                sorted_dist.append((d, c12))

    sorted_dist = sorted(sorted_dist, key=lambda x: x[0], reverse=False)
    connected = set()
    connected.add(c1)
    most_expensive = 0
    circuit_pair = ""
    while len(connected) < len(circuits):
        for i in range(len(sorted_dist)):
            d, c12 = sorted_dist[i]
            c1,c2 = str_circ(c12)
            if c1 in connected or c2 in connected:
                sorted_dist.pop(i)
                if d > most_expensive:
                    most_expensive = d
                    circuit_pair, _ = circ_comb(c1,c2)
                connected.add(c1); connected.add(c2)
                break
    print(circuit_pair)
    c1, c2 = str_circ(circuit_pair)
    x1 = c1[0]
    x2 = c2[0]
    print(x1*x2)

#p1()
p2()

