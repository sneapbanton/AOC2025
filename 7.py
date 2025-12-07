
"""
This day was solved on mobile phone, extra messy code
"""

def p1():
    
    rows = []
    f = open("D1.txt")
    for line in f:
        rows.append(list(line[:-1] if "\n" in line else line))

    score = 0
    for y in range(len(rows)):
        r = rows[y]
        for x in range(len(rows[0])):
            if r[x]=="S":
                r[x]="|"
            elif r[x]=="^" and rows[y-1][x]=="|":
                split=0
                if r[x-1]==".":
                    r[x-1]="|"
                    split+=1
                if r[x+1]==".":
                    r[x+1]="|"
                    split+=1
                if split:
                    score +=1
            elif rows[y-1][x]=="|":
                r[x]="|"

    print(score)

def p2():
    from functools import cache
    rows = []
    f = open("D1.txt")
    for line in f:
        rows.append(list(line[:-1] if "\n" in line else line))

    score = 0
    for y in range(len(rows)):
        r = rows[0]
        for x in range(len(rows[0])):
            if r[x]=="S":
                break

    @cache
    def search(x, y):
        if y==len(rows):
            return 1
        if rows[y][x]=="^":
            return search(x-1, y+1) + search(x+1,y+1)
        return search(x, y+1)

    print(search(x, 0))

p1()
p2()

