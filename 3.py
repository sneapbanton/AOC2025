

def p1():
    f = open("d3.txt")

    score = 0
    largest = 0
    sec_lar = 0
    for line in f:
        digits = list(map(int, list(line[:-1] if line[-1] == "\n" else line)))
        largest = digits[0]
        large_i = 0
        for i, dig in enumerate(digits[1:-1]):
            if dig > largest:
                largest = dig
                large_i = i+1
        sec_lar = digits[large_i+1]
        for dig in digits[large_i+1:]:
            if dig > sec_lar:
                sec_lar = dig
        score += int(str(largest) + str(sec_lar))

    print(score)

def rec_finder2(digits, num_left):
    if num_left == 1:
        return str(max(digits))
    
    largest = max(digits[:-num_left+1])
    large_i = digits.index(largest)
    
    return str(largest) + rec_finder2(digits[large_i+1:], num_left-1)

def p2():
    f = open("d3.txt")

    score = 0
    for line in f:
        digits = list(map(int, list(line[:-1] if line[-1] == "\n" else line)))
        res = int(rec_finder2(digits, 12))
        score += res
    print(score)

if __name__ == "__main__":
    p2()