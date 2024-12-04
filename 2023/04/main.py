import re

FILE = r"D:\Code\AoC\04\input.txt"

def process_input(FILE):
    lines = [line.split(": ")[1].strip() for line in open(FILE, "r").readlines()]
    data = []
    for line in lines:
        line = re.sub(" +", " ", line)
        data.append([list(map(int, item.split())) for item in line.split(" | ")])
    return data

LINES = process_input(FILE)

def bothParts(LINES):
    s, i = 0, 1
    cards = [1] * len(LINES)
    for line in LINES:
        cnt = 0
        for item in line[0]:
            if item in line[1]:
                cnt += 1
        j = i
        for k in range(cnt):
            cards[j+k] += 1 * cards[i-1]
        i += 1
        s += pow(2, cnt - 1) if cnt > 0 else 0
    return [s, sum(cards)]

if __name__ == "__main__":
    print(*bothParts(LINES), sep="\n")
