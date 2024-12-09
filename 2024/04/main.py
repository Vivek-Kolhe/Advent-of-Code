# Code can really be improved but too lazy to do it now

import time

FILE = "input.txt"

def process_input():
    lines = [line.strip() for line in open(FILE, "r").readlines()]
    return lines

lines = process_input()
rows, cols = len(lines), len(lines[0])
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]

def find_occurrences(target):
    occurrences = []

    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == target[0]:
                for dir in dirs:
                    nrow, ncol = r, c
                    temp = lines[nrow][ncol]
                    idx = [(nrow, ncol)]
                    for i in range(len(target) - 1):
                        nrow += dir[0]
                        ncol += dir[1]
                        if nrow >= 0 and nrow < rows and ncol >= 0 and ncol < cols:
                            temp += lines[nrow][ncol]
                            idx.append((nrow, ncol))
                    if temp == target:
                        occurrences.append(idx)
    return occurrences

def part_one():
    return len(find_occurrences("XMAS"))

def part_two():
    res = 0
    mas = find_occurrences("MAS")
    
    for i in range(len(mas)):
        for j in range(len(mas)):
            if (i == j):
                continue
            if mas[i][1][0] != mas[j][1][0] or mas[i][1][1] != mas[j][1][1]:
                continue
            
            a, b = mas[i], mas[j]
            if a[0][0] == b[0][0] and abs(a[0][1] - b[0][1]) == 2 and a[2][0] == b[2][0] and abs(a[2][1] - b[2][1]) == 2:
                res += 1
            if a[0][1] == b[0][1] and abs(a[0][0] - b[0][0]) == 2 and a[2][1] == b[2][1] and abs(a[2][0] - b[2][0]) == 2:
                res += 1
    return res // 2


if __name__ == '__main__':
    start = time.perf_counter()
    print(part_one(), part_two(), sep="\n")
    print(f"Time taken: {(time.perf_counter() - start) * 1000} ms")