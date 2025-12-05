
def p1():
    f = open("d5.txt")
    score = 0
    spans = []
    for line in f:
        data = line[:-1] if line[-1] == "\n" else line
        if "-" in data:
            start, stop = map(int,data.split("-"))
            spans.append((start, stop))
        elif len(data):
            for (start, stop) in spans:
                if start <= int(data) <= stop:
                    print(data)
                    score += 1
                    break
    print(score)

def p2():
    f = open("d5.txt")
    score = 0
    counted_spans = []
    sorted_spans = []
    for line in f:
        data = line[:-1] if line[-1] == "\n" else line
        if "-" in data:
            start, stop = map(int,data.split("-"))
            sorted_spans.append((start,stop))
    sorted_spans = sorted(sorted_spans, key=lambda x: x[0])
    for (start, stop) in sorted_spans:
        dont = False
        for (s1,s2) in counted_spans:
            if s1 <= start <= s2 and s1 <= stop <= s2:
                dont = True
                break
            if s1 <= start <= s2:
                start = s2+1
            if s1 <= stop <= s2:
                stop = s1-1
        if dont:
            continue
        counted_spans.append((start, stop))
        score += stop-start+1
    print(score)


if __name__ == "__main__":
    p2()