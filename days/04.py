def solve1(input):
    n = range(len(input) - 3)
    input_ = list(map("".join, zip(*[l.strip()[::-1] for l in input])))
    h = [l[i:i+4] for l in input for i in n]
    v = [l[i:i+4] for l in input_ for i in n]
    d = ["".join([input_[i+k][j+k] for k in range(4)]) for i in n for j in n]
    d2 = ["".join([input[i+k][j+k] for k in range(4)]) for i in n for j in n]
    return sum(l.count(w) for l in [h, d, d2, v] for w in ["XMAS", "SAMX"])

def solve2(input):
    n = range(len(input) - 2)
    sub = ["".join(l[i:i+3] for l in ll)[::2] for i in n for ll in [input[i:i+3] for i in n]]
    return sum(l.count(p) for l in sub for p in ["MSAMS", "MMASS", "SMASM", "SSAMM"])


if __name__ == "__main__":
    with open("inputs/04.txt") as f:
        input = f.readlines()
    
    print(solve1(input))
    print(solve2(input))