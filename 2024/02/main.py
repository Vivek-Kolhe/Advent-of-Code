import time

FILE = "input.txt"

def process_input():
    lines = [list(map(int, line.split())) for line in open(FILE, "r")]
    return lines

arr = process_input()

def part_one():
    count = 0
    seen = set()
    for idx, item in enumerate(arr):
        f1, f2 = True, True
        for i in range(1, len(item)):
            if not (item[i-1] < item[i] and abs(item[i-1] - item[i]) >= 1 and abs(item[i-1] - item[i]) <= 3):
                f1 = False
            if not (item[i-1] > item[i] and abs(item[i-1] - item[i]) >= 1 and abs(item[i-1] - item[i]) <= 3):
                f2 = False
        
        if f1 or f2:
            seen.add(idx)
            count += 1
    return seen, count

def part_two():
    seen, partOne = part_one()
    count = 0
    for idx, item in enumerate(arr):
        if idx in seen:
            continue

        n = len(item)
        for i in range(n):
            temp = item.copy()
            temp.pop(i)
            f1, f2 = True, True
            for i in range(1, len(temp)):
                if not (temp[i-1] < temp[i] and abs(temp[i-1] - temp[i]) >= 1 and abs(temp[i-1] - temp[i]) <= 3):
                    f1 = False
                if not (temp[i-1] > temp[i] and abs(temp[i-1] - temp[i]) >= 1 and abs(temp[i-1] - temp[i]) <= 3):
                    f2 = False
            
            if f1 or f2:
                count += 1
                break
    return partOne, partOne + count

if __name__ == '__main__':
    start = time.perf_counter()
    print(part_two())
    print(f"Time taken: {(time.perf_counter() - start) * 1000} ms")