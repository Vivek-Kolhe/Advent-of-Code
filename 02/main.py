FILE = r"D:\Code\AoC\02\input.txt"
RED, GREEN, BLUE = 12, 13, 14

def process_input(FILE):
    lines = [line.split(": ")[1].strip() for line in open(FILE, "r").readlines()]
    data = []
    for line in lines:
        line = line.split("; ")
        temp = []
        for l in line:
            temp.append(l.split(", "))
        data.append(temp)
    return data

LINES = process_input(FILE)

def partOne(LINES):
    s = 0
    for i in range(len(LINES)):
        red, green, blue = 0, 0, 0
        set = LINES[i]
        for subset in set:
            for turn in subset:
                t = turn.split(" ")
                match t[1]:
                    case "red":
                        red = max(red, int(t[0]))
                    case "green":
                        green = max(green, int(t[0]))
                    case "blue":
                        blue = max(blue, int(t[0]))
        
        if red <= RED and green <= GREEN and blue <= BLUE:
            s += i + 1
    return s

def partTwo(LINES):
    s = 0
    for i in range(len(LINES)):
        red, green, blue = 0, 0, 0
        set = LINES[i]
        for subset in set:
            for turn in subset:
                t = turn.split(" ")
                match t[1]:
                    case "red":
                        red = max(red, int(t[0]))
                    case "green":
                        green = max(green, int(t[0]))
                    case "blue":
                        blue = max(blue, int(t[0]))
        
        s += (red * green * blue)
    return s

if __name__ == "__main__":
    print(partOne(LINES))
    print(partTwo(LINES))