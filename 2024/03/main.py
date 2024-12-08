import time

FILE = "input.txt"

def process_input():
    lines = [line.strip() for line in open(FILE, "r").readlines()]
    return lines

data = "".join(process_input())

# opening parenthesis '('
o = [i for i in range(3, len(data)) if data[i-3:i] == "mul" and data[i] == "("]

# closing parenthesis ')'
c = [i for i in range(len(data)) if data[i] == ")"]

# get all do and dont instructions
def process_do_dont():
    do = {i - 2 for i in range(2, len(data)) if data[i-2:i] == "do"}
    dont = {i - 5 for i in range(5, len(data)) if data[i-5:i] == "don't"}
    for item in dont:
        if item in do:
            do.discard(item)

    return do, dont

do, dont = map(list, process_do_dont())
do.sort()
dont.sort()

def search_next(item, arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return low

def search_prev(item, arr):
    low, high = 0, len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return high

def parse_and_multiply(s):
    commas, nums = 0, []
    temp = ""
    for char in s:
        if char.isnumeric() or char == ",":
            if char.isnumeric():
                temp += char
            else:
                commas += 1
                nums.append(int(temp))
                temp = ""
        else:
            break
    nums.append(int(temp))
    return nums

def part_one():
    res = 0
    for item in o:
        idx = search_next(item, c)

        if not (c[idx] - item - 1 < 3 or c[idx] - item - 1 > 7):
            s = data[item+1:c[idx]]
            nums = parse_and_multiply(s)        
            if len(nums) == 2:
                res += (nums[0] * nums[1])
    return res

def part_two():
    res = 0
    flag = True

    i = 0
    while o[i] < min(do[0], dont[0]):
        idx = search_next(o[i], c)

        if not (c[idx] - o[i] - 1 < 3 or c[idx] - o[i] - 1 > 7):
            s = data[o[i]+1:c[idx]]
            nums = parse_and_multiply(s)
            if len(nums) == 2:
                res += (nums[0] * nums[1])
        i += 1
    
    while i < len(o):
        idx1, idx2 = search_prev(o[i], do), search_prev(o[i], dont)

        if idx1 == -1:
            flag = False
        elif idx2 == -1:
            flag = True
        else:
            flag = do[idx1] > dont[idx2]

        if flag:
            idx = search_next(o[i], c)
            
            if not (c[idx] - o[i] - 1 < 3 or c[idx] - o[i] - 1 > 7):
                s = data[o[i]+1:c[idx]]
                nums = parse_and_multiply(s)
                if len(nums) == 2:
                    res += (nums[0] * nums[1])
        i += 1
    return res

if __name__ == '__main__':
    start = time.perf_counter()
    print(part_one(), part_two(), sep="\n")
    print(f"Time taken: {(time.perf_counter() - start) * 1000} ms")