import re

def mul(a,b):
    return a*b

enabled = True

def process(token):
    global enabled
    if token == "do()": 
        enabled = True
        return 0
    elif token == "don't()":
        enabled = False
        return 0
    elif enabled:
        return eval(token)
    else:
        return 0

def solve1(input):
    l = re.findall(r"mul\(\d*,\d*\)", input)
    return sum(map(eval, l))


def solve2(input):
    l = re.findall(r"mul\(\d*,\d*\)|don't\(\)|do\(\)", input)
    return sum(map(process, l))


if __name__ == "__main__":
    with open("inputs/03.txt") as f:
        lines = f.read()
    
    print(solve1(lines))
    print(solve2(lines))
