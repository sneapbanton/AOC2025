from tqdm import tqdm
from functools import cache
import numpy as np
from z3 import *

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


def p2():
    score = 0
    f = open("d10.txt")
    goals = []
    butts = []
    for line in f:
        fields = line.split(" ")
        goal = fields[-1]
        buttons = fields[1:-1]
        goals.append(goal)
        butts.append(buttons)

    for i in tqdm(range(len(goals))):
        solver = Solver()
        goal = goals[i][1:-1] if "\n" not in goals[i] else goals[i][1:-2]
        buttons = butts[i]
        button_presses = []
        g = [int(x) for x in goal.split(",")]

        expr = [0 for x in range(len(g))]
        for k, button in enumerate(buttons):
            new_var = Int("b"+str(k))
            solver.add(new_var > -1)
            button_presses.append(new_var)
            for x in button[1:-1].split(","):
                # print(int(x))
                expr[int(x)] = expr[int(x)]+new_var

        for k, x in enumerate(g):
            eq = expr[k] == x
            solver.add(eq)

        print(solver)
        if solver.check() == sat:
            model = solver.model()
            print(model)

        # print(g)
        # print(button_presses)

    print(score)


p2()
