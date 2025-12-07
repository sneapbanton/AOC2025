
"""
This day was solved on mobile phone, extra messy code
"""

def p1():
    
    operators = []
    f = open("D1.txt")
    for line in f:
        if "*" in line:
            operators = list(line)

    result = [int(x=="*") for x in operators if x!=" "]
    rows = []
    f = open("D1.txt")
    for line in f:
        if "*" not in line:
            nums = list(line[:-1]) if "\n" in line else line
            rows.append(nums)
            
    operi = 0
    nums = []
    count = -1
    for i in range(len(operators)):
        if operators[i]!=" ":
            operi = i
            oper = operators[i]
            count += 1
            #nums.append(["" for x in range(len(rows))])
        num = ""
        for j in range(len(rows)):
            num += rows[j][i] if rows[j][i]!=" " else ""
        
        if num:
            result[count] = result[count]*int(num) if oper=="*" else result[count]+int(num)



    print(sum(result))

def p2():
    
    operators = []
    f = open("D1.txt")
    for line in f:
        if "*" in line:
            operators = list(line.split(" "))

    operators = [x for x in operators if x]
    result = [int(x=="*") for x in operators]
    f = open("D1.txt")
    for line in f:
        if "*" not in line:
            line = line[:-1] if "\n" in line else line
            nums = [int(x) for x in line.split(" ") if x!=""]
            for i in range(len(nums)):
                result[i] = result[i] * nums[i] if "*" in operators[i] else result[i]+nums[i]

    print()
    print()
    print(operators)
    print(result)
    print(sum(result))


p1()
p2()
