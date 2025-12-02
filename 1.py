
def p1():
    f = open("d1.txt", "r")

    counter = 50
    score = 0
    for line in f:
        vect = line[0]
        dial = int(line[1:])
        if vect == "L":
            counter -= dial
        else:
            counter += dial
        print(counter)

        if counter == 0 or str(counter)[-2:] == "00":
            score += 1
    print(score)

def p2():
    f = open("d1.txt", "r")

    counter = 50
    score = 0
    for line in f:
        vect = line[0]
        dial = int(line[1:])
        for i in range(dial):
            if vect == "L":
                counter -= 1
            else:
                counter += 1
            
            if counter == 0 or str(counter)[-2:] == "00":
                score += 1 
        print(counter)
    print(score)

if "__main__" == __name__:
    p2()