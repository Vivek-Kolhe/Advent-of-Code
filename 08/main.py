import math

FILE = r"D:\Code\AoC\08\input.txt"
LINES = open(FILE, "r").read().split("\n\n")

instructions, lables = LINES[0], LINES[1].split("\n")
network = {}

for item in lables:
    node, data = item.split(" = ")
    network[node] = data[1:-1].split(", ")

def partOne(instructions, network):
    cnt = 0
    curr = "AAA"
    while curr != "ZZZ":
        if instructions[0] == "L":
            curr = network[curr][0]
        else:
            curr = network[curr][1]
        cnt += 1
        instructions = instructions[1:] + instructions[0]
    return cnt

def partTwo(instructions, network):
    all_a = [key for key in network if key.endswith("A")]
    ans = None
    for i in range(len(all_a)):
        cnt, ins = 0, instructions
        curr = all_a[i]
        while not curr.endswith("Z"):
            if ins[0] == "L":
                curr = network[curr][0]
            else:
                curr = network[curr][1]
            cnt += 1
            ins = ins[1:] + ins[0]
        if ans is None:
            ans = cnt
        else:
            ans = (ans * cnt) // math.gcd(ans, cnt)
    return ans

if __name__ == "__main__":
    print(partOne(instructions, network))
    print(partTwo(instructions, network))