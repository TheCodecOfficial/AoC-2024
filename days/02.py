def solve1(input):
    sum = 0
    for l in input:
        nums = [int(n) for n in l.strip().split(" ")]
        diff = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        sign = 1 if diff[0] > 0 else -1
        sum += all(1 <= sign * d <= 3 for d in diff)
    return sum


def solve2(input):
    sum = 0
    for l in input:
        for i in range(len(l)):
            nums = [int(n) for j, n in enumerate(l.strip().split(" ")) if i != j]
            diff = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            sign = 1 if diff[0] > 0 else -1
            if all(1 <= sign * d <= 3 for d in diff):
                sum += 1
                break
    return sum


if __name__ == "__main__":
    with open("inputs/02.txt") as f:
        lines = f.readlines()
    print(solve1(lines))
    print(solve2(lines))
