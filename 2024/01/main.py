FILE = "input.txt"

def process_input():
    lines = [line.split() for line in open(FILE, "r").readlines()]
    a, b = [], []

    for line in lines:
        a.append(int(line[0]))
        b.append(int(line[1]))
    return a, b

a, b = process_input()

def part_one():
    c, d = sorted(a), sorted(b)
    dist = 0
    
    for i in range(len(c)):
        dist += (abs(c[i] - d[i]))
    return dist

def part_two():
    cnt = dict()
    for num in b:
        if cnt.get(num) is None:
            cnt[num] = 0
        cnt[num] += 1
    
    score = 0
    for num in a:
        if cnt.get(num) is None:
            continue
        score += (num * cnt[num])
    return score

if __name__ == '__main__':
    print(part_one(), part_two(), sep="\n")