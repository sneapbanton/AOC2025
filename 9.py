from collections import defaultdict
from tqdm import tqdm

def p1():
    tiles = []
    f = open("d9.txt")
    for line in f:
        x,y = map(int,line[:-1].split(",")) if "\n" in line else map(int,line.split(","))
        tiles.append((x,y))

    areas = defaultdict(lambda:0)
    for (x1,y1) in tiles:
        for (x2,y2) in tiles:
            if (x1==x2 and y1==y2) or (areas[f"{x1},{y1},{x2},{y2}"] or areas[f"{x2},{y2},{x1},{y1}"]):
                continue
            dx = abs(x1-x2)+1
            dy = abs(y1-y2)+1
            areas[f"{x1},{y1},{x2},{y2}"] = dx*dy
    
    print(max(areas.values()))


def p2():
    tiles = []
    f = open("d9.txt")
    for line in f:
        x,y = map(int,line[:-1].split(",")) if "\n" in line else map(int,line.split(","))
        tiles.append((x,y))

    lines = defaultdict(lambda: False)
    for i in range(len(tiles)):
        x1,y1 = tiles[i-1]
        x2,y2 = tiles[i]
        for y3 in range(min(y1,y2),max(y1,y2)+1):
            for x3 in range(min(x1,x2),max(x1,x2)+1):
                lines[f"{x3},{y3}"] = True


    areas = defaultdict(lambda:0)
    areas_l = []
    for (x1,y1) in tiles:
        for (x2,y2) in tiles:
            if (x1==x2 and y1==y2) or (areas[f"{x1},{y1},{x2},{y2}"] or areas[f"{x2},{y2},{x1},{y1}"]):
                continue
            dx = abs(x1-x2)+1
            dy = abs(y1-y2)+1
            areas[f"{x1},{y1},{x2},{y2}"] = dx*dy
            areas_l.append((f"{x1},{y1},{x2},{y2}",dx*dy))

    res = sorted(areas_l,key=lambda x:x[1],reverse=True)
    biggest_area = 0
    for key,val in tqdm(res) :
        x1,y1,x2,y2 = map(int,key.split(","))
        if val <= biggest_area:
            continue
        ok = True
        for x3,y3 in tiles:
            if min(x1,x2) < x3 < max(x1,x2) and min(y1,y2) < y3 < max(y1,y2):
                ok = False
                break
        if not ok:
            continue

        for key in lines:
            x3,y3 = map(int,key.split(","))
            if min(x1,x2) < x3 < max(x1,x2) and min(y1,y2) < y3 < max(y1,y2):
                ok = False
                break
        if not ok:
            continue
        
        if ok:
            biggest_area = val
            print(x1,y1,"  ",x2,y2)
            continue


    print(biggest_area)


#p1()
p2()