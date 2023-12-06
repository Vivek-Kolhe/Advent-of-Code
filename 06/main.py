import re

FILE = r"D:\Code\AoC\06\input.txt"
LINES = open(FILE, "r").read().split("\n")
time = re.sub(" +", " ", LINES[0].split(":")[1]).strip().split(" ")
dist = re.sub(" +", " ", LINES[1].split(":")[1]).strip().split(" ")

def get_range(time, dist):
    low, high = 1, time
    while low <= high:
        mid = (low + high) // 2
        if (time - mid) * mid  <= dist:
            low = mid + 1
        else:
            high = mid - 1
    s = time - low

    low, high = 1, time
    while low <= high:
        mid = (low + high) // 2
        if (time - mid) * mid > dist:
            low = mid + 1
        else:
            high = mid - 1
    e = time - low
    return s, e

def partOne(time, dist):
    time = list(map(int, time))
    dist = list(map(int, dist))
    ans = 1
    for t, d in zip(time, dist):
        s, e = get_range(t, d)
        ans *= (s - e)
    return ans

def partTwo(time, dist):
    time = int("".join(time))
    dist = int("".join(dist))
    s, e = get_range(time, dist)
    return s - e

if __name__ == "__main__":
    print(partOne(time, dist))
    print(partTwo(time, dist))
