import time

FILE = "input.txt"

def process_input():
    lines = [line.strip() for line in open(FILE, "r").readlines()]
    order, seq = [], []
    
    i = 0
    while lines[i] != "":
        order.append(list(map(int, lines[i].split("|"))))
        i += 1
    
    i += 1
    while i < len(lines):
        seq.append(list(map(int, lines[i].split(","))))
        i += 1
    return order, seq

order, seq = process_input()

def valid(arr, prev):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] not in prev[arr[i]]:
                return False
    return True

def get_all_prev():
    prev = {}
    for nums in order:
        if prev.get(nums[0]) is None:
            prev[nums[0]] = set()
        if prev.get(nums[1]) is None:
            prev[nums[1]] = set()
        prev[nums[0]].add(nums[1])
    return prev

prev = get_all_prev()

def part_one():
    res = 0
    for arr in seq:
        if valid(arr, prev):
            res += arr[len(arr)//2]
    return res
    
def part_two():
    res = 0
    for arr in seq:
        if not valid(arr, prev):
            for i in range(len(arr)):
                count = 0
                for j in range(len(arr)):
                    if i == j:
                        continue
                    if arr[j] in prev[arr[i]]:
                        count += 1
                if count == (len(arr) // 2):
                    res += arr[i]
    return res

if __name__ == '__main__':
    start = time.perf_counter()
    print(part_one(), part_two(), sep="\n")
    print(f"Time taken: {(time.perf_counter() - start) * 1000} ms")