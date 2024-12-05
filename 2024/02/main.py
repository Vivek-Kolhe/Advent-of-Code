import time

FILE = "input.txt"

def process_input():
    lines = [list(map(int, line.split())) for line in open(FILE, "r")]
    return lines

lines = process_input()

def valid(arr):
    f1, f2 = True, True
    for i in range(1, len(arr)):
        if not (arr[i-1] < arr[i] and abs(arr[i-1] - arr[i]) >= 1 and abs(arr[i-1] - arr[i]) <= 3):
            f1 = False
        if not (arr[i-1] > arr[i] and abs(arr[i-1] - arr[i]) >= 1 and abs(arr[i-1] - arr[i]) <= 3):
            f2 = False
    
    if f1 or f2:
        return True
    return False

def both_parts():
    c1, c2 = 0, 0
    for item in lines:
        if valid(item):
            c1 += 1
            continue

        n = len(item)
        for i in range(n):
            temp = item.copy()
            temp.pop(i)
            if valid(temp):
                c2 += 1
                break
    return c1, c1 + c2

if __name__ == '__main__':
    start = time.perf_counter()
    print(both_parts())
    print(f"Time taken: {(time.perf_counter() - start) * 1000} ms")