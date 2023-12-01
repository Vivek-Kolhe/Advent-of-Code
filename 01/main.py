import sys

FILE = r"D:\Code\AoC\01\input.txt"
LINES = [line.strip() for line in open(FILE, "r").readlines()]

def partOne(LINES):
    s = 0
    for line in LINES:
        mini, maxi = sys.maxsize, -1
        for i in range(len(line)):
            if line[i].isdigit():
                maxi = i
                mini = min(mini, i)
        if maxi != -1:
            s += int(line[mini] + line[maxi])
    return s

def partTwo(LINES):
    s = 0
    digitWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in LINES:
        wordmini, wordmaxi = sys.maxsize, -1
        first, second = 0, 0
        for word in digitWords:
            l_ind = line.find(word)
            r_ind = line.rfind(word)
            if l_ind != -1:
                if l_ind < wordmini:
                    first = 10 * (digitWords.index(word) + 1)
                    wordmini = l_ind
                if r_ind > wordmaxi:
                    second = digitWords.index(word) + 1
                    wordmaxi = r_ind
        
        digmini, digmaxi = sys.maxsize, -1
        for i in range(len(line)):
            if line[i].isdigit():
                digmaxi = i
                digmini = min(i, digmini)
        
        if wordmaxi == -1 and digmaxi == -1:
            continue
        if digmini < wordmini:
            first = 10 * int(line[digmini])
        if digmaxi > wordmaxi:
            second = int(line[digmaxi])
        s += first + second
    return s

if __name__ == "__main__":
    print(partOne(LINES))
    print(partTwo(LINES))