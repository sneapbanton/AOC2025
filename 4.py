import numpy as np

def p1():
    f = open("d4.txt")
    map = []
    for line in f:
        data = list(line[:-1] if line[-1] == "\n" else line)
        map.append(data)
    map = np.array(map)
    score = 0
    for y in range(map.shape[0]):
        for x in range(map.shape[1]):
            if map[y,x] != "@":
                continue
            rolls = 0
            adjacent_x = [-1+x, 0+x, 1+x]
            adjacent_y = [-1+y, 0+y, 1+y]
            if y == 0:
                adjacent_y.pop(0)
            elif y == map.shape[0]-1:
                adjacent_y.pop(2)
            if x == 0:
                adjacent_x.pop(0)
            elif x == map.shape[1]-1:
                adjacent_x.pop(2)
            for ly in adjacent_y:
                for lx in adjacent_x:
                    if lx==x and ly==y:
                        continue
                    if map[ly, lx] == "@":
                        rolls += 1
            if rolls < 4:
                score += 1
    print(score)


def p2():
    f = open("d4.txt")
    map = []
    for line in f:
        data = list(line[:-1] if line[-1] == "\n" else line)
        map.append(data)
    map = np.array(map)
    score = 0
    changed = True
    while (changed):
        changed = False
        for y in range(map.shape[0]):
            for x in range(map.shape[1]):
                if map[y,x] != "@":
                    continue
                rolls = 0
                adjacent_x = [-1+x, 0+x, 1+x]
                adjacent_y = [-1+y, 0+y, 1+y]
                if y == 0:
                    adjacent_y.pop(0)
                elif y == map.shape[0]-1:
                    adjacent_y.pop(2)
                if x == 0:
                    adjacent_x.pop(0)
                elif x == map.shape[1]-1:
                    adjacent_x.pop(2)
                for ly in adjacent_y:
                    for lx in adjacent_x:
                        if lx==x and ly==y:
                            continue
                        if map[ly, lx] == "@":
                            rolls += 1
                if rolls < 4:
                    changed = True
                    map[y,x] = "."
                    score += 1
        print(score)


if __name__ == "__main__":
    p2()