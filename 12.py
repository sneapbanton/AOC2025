

def p1():

    f = open("d12.txt")
    figures = []
    figure = []
    slots = {}
    for line in f:
        if "x" in line:
            xy = line.split(":")[0]
            pres = line.split(":")[1]
            pres = [x for x in pres if x!=" " and x!="\n"]
            print(pres)

        elif ":" in line and figure:
            figures.append(figure)
            figure = []
        
        elif "#" in line or "." in line:
            figure.append(list(line[:-1]))

p1()