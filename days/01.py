def solve1(input):
    lines = [l.strip().split("   ") for l in input]
    a, b = zip(*lines)
    return sum(abs(int(a) - int(b)) for a, b in zip(sorted(a), sorted(b)))


def solve2(input):
    lines = [l.strip().split("   ") for l in input]
    a, b = zip(*lines)
    return sum(int(a) * b.count(a) for a in a)


if __name__ == "__main__":
    with open("inputs/01.txt") as f:
        lines = f.readlines()
    print(solve1(lines))
    print(solve2(lines))
