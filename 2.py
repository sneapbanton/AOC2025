

def p1():
    f = open("2.txt")
    score = 0
    for line in f:
        for span in line.split(","):
            if span == "\n":
                continue
            start, end = map(int, span.split("-"))
            for counter in range(start, end+1):
                strc = str(counter)
                chars = len(strc)
                if chars % 2 != 0:
                    continue
                if strc[:chars//2] == strc[chars//2:]:
                    score += int(strc)
    print(score)


def p2():
    f = open("2.txt")
    score = 0
    for line in f:
        for span in line.split(","):
            if span == "\n":
                continue
            start, end = map(int, span.split("-"))
            for counter in range(start, end+1):
                strc = str(counter)
                chars = len(strc)
                #print(strc, chars)

                for charlen in range(2,chars+1):
                    #print(charlen)
                    if chars%charlen != 0:
                        continue
                    charmult = 0
                    alike = True
                    while(charmult < charlen-1 and alike):
                        
                        alike = strc[charmult*(chars//charlen):(charmult+1)*(chars//charlen)] == strc[(charmult+1)*(chars//charlen):(charmult+2)*(chars//charlen)]
                        #print(counter, strc[charmult*(chars//charlen):(charmult+1)*(chars//charlen)], strc[(charmult+1)*(chars//charlen):(charmult+2)*(chars//charlen)], alike)
                        charmult += 1
                    if alike:
                        #print("found", strc, strc[charmult*(chars//charlen):(charmult+1)*(chars//charlen)])
                        score += int(strc)
                        break
            
                    
    print(score)


if __name__ == "__main__":
    p2()