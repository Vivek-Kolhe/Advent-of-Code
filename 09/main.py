FILE = r"D:\Code\AoC\09\input.txt"
LINES = [list(map(int, line.strip().split())) for line in open(FILE, "r").readlines()]

def partOne(LINES):
    s = 0
    for line in LINES:
        temp = [line]
        while any((new := [curr[i+1] - curr[i] for i in range(len(curr) - 1)]) != [0] for curr in temp[-1:]):
            temp.append(new)
        for i in range(len(temp) - 1, -1, -1):
            temp[i].append(temp[i][-1] + temp[i+1][-1] if i < len(temp) - 1 else 0)
        s += temp[0][-1]
    return s

def partTwo(LINES):
    s = 0
    for line in LINES:
        line.reverse()
        temp = [line]
        while any((new := [curr[i+1] - curr[i] for i in range(len(curr) - 1)]) != [0] for curr in temp[-1:]):
            temp.append(new)
        for i in range(len(temp) - 1, -1, -1):
            temp[i].append(temp[i][-1] + temp[i+1][-1] if i < len(temp) - 1 else 0)
        s += temp[0][-1]
    return s

if __name__ == "__main__":
    print(partOne(LINES))
    print(partTwo(LINES))