import sys

FILE = r"D:\Code\AoC\05\input.txt"
LINES = open(FILE, "r").read().split("\n\n")

seeds, *mappers = LINES
seeds = list(map(int, seeds.split(": ")[1].split()))
mappers = [item.split(":")[1].strip().split("\n") for item in mappers]
final_mappers = [[[int(num) for num in item.split()] for item in mapper] for mapper in mappers]

def partOne(seeds, mappers):
    ans = sys.maxsize
    for seed in seeds:
        res = seed
        for mapper in mappers:
            for rang in mapper:
                dest, src, diff = rang
                if src <= res < src + diff:
                    res += (dest - src)
                    break
        ans = min(res, ans)
    return ans

if __name__ == "__main__":
    print(partOne(seeds, final_mappers))