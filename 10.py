from tqdm import tqdm
import sys
from functools import cache

@cache
def search(goal, state, buttons):
    if all(a==b for a, b in zip(goal, state)):
        return 0
    min_val = -1
    for i in range(len(buttons)):
        statel = list(state)
        for j in buttons[i]:
            statel[j] = statel[j]==False
        new_buttons = list(buttons)
        new_buttons.pop(i)
        if min_val==-1:
            min_val = 1+search(goal, tuple(statel),tuple(new_buttons))
        else:
            min_val = min(min_val, 1+search(goal, tuple(statel),tuple(new_buttons)))
    return min_val

def p1():
    score = 0
    f = open("d10.txt")
    goals = []
    butts = []
    for line in f:
        fields = line.split(" ")
        goal = fields[0]
        buttons = fields[1:-1]
        goals.append(goal)
        butts.append(buttons)

    for i in tqdm(range(len(goals))):
        goal = goals[i][1:-1]
        buttons = butts[i]
        g = ["#"==x for x in goal]
        bs = []
        for button in buttons:
            b = tuple([int(x) for x in button[1:-1].split(",")])
            bs.append(b)
        res = search(tuple(g),tuple([False for x in range(len(g))]), tuple(bs))
        score += res
        # print(res)

    print(score)
p1()
