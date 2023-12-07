from collections import Counter
from functools import cmp_to_key

# def hand_type(hand):
#     counts = [hand.count(card) for card in hand]
#     if 5 in counts:
#         return 6
#     if 4 in counts:
#         return 5
#     if 3 in counts:
#         if 2 in counts:
#             return 4
#         return 3
#     if counts.count(2) == 4:
#         return 2
#     if 2 in counts:
#         return 1
#     return 0

FILE = r"D:\Code\AoC\07\input.txt"
LINES = [line.strip().split() for line in open(FILE, "r").readlines()]
LINES = list(map(lambda x: [x[0], int(x[1])], LINES))
PART_ONE = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
PART_TWO = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

def type_one(hand):
    c = Counter(hand)
    cmn = c.most_common()
    if cmn[0][1] == 5:
        return 6
    if cmn[0][1] == 4:
        return 5
    if cmn[0][1] == 3:
        if cmn[1][1] == 2:
            return 4
        return 3
    if cmn[0][1] == 2:
        if cmn[1][1] == 2:
            return 2
        return 1
    return 0

def type_two(hand):
    c = Counter(hand)
    joker = c["J"]
    del c["J"]
    cmn = c.most_common()
    if len(cmn) < 2:
        return 6
    if cmn[0][1] + joker == 5:
        return 6
    if cmn[0][1] + joker == 4:
        return 5
    if (cmn[0][1] + joker == 3 and cmn[1][1] == 2) or (cmn[0][1] == 3 and cmn[1][1] + joker == 2):
        return 4
    if cmn[0][1] + joker == 3:
        return 3
    if (cmn[0][1] + joker == 2 and cmn[1][1] == 2) or (cmn[0][1] == 2 and cmn[1][1] + joker == 2):
        return 2
    if cmn[0][1] + joker == 2:
        return 1
    return 0

def compare(first, second, order, part):
    first, second = first[0], second[0]
    f = type_two(first) if part else type_one(first)
    s = type_two(second) if part else type_one(second)
    if f != s:
        if f < s:
            return -1
        if f > s:
            return 1
        return 0
    else:
        for i in range(5):
            x, y = order.index(first[i]), order.index(second[i])
            if x < y:
                return -1
            if x > y:
                return 1
    return 0

def partOne(LINES):
    LINES.sort(key=cmp_to_key(lambda x, y: compare(x, y, PART_ONE, 0)))
    ans = 0
    for i in range(len(LINES)):
        ans += ((i + 1) * LINES[i][1])
    return ans

def partTwo(LINES):
    LINES.sort(key=cmp_to_key(lambda x, y: compare(x, y, PART_TWO, 1)))
    ans = 0
    for i in range(len(LINES)):
        ans += ((i + 1) * LINES[i][1])
    return ans

if __name__ == "__main__":
    print(partOne(LINES))
    print(partTwo(LINES))
