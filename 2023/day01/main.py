import sys, math


def process_file(file):
    sum = 0
    alpha = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    with open(file) as f:
        for line in f:
            foundn = {}
            foundc = {}
            for c in line:
                res = [i for i in range(len(line)) if line.startswith(c, i)]
                if len(res) > 0 and c.isnumeric():
                    fn = []
                    for i in range(0, len(res)):
                        fn.append(res[i])
                    foundn[c] = fn
            for char in alpha:
                res = [i for i in range(len(line)) if line.startswith(char, i)]
                if len(res) > 0:
                    fc = []
                    for i in range(0, len(res)):
                        fc.append(res[i])
                    foundc[str(alpha[char])] = fc
            sum += find_first_last(foundn, foundc)
    print(sum)


def find_first_last(nl, cl):
    low = float(math.inf)
    high = float(-math.inf)
    found_low = found_high = 0
    for n, i in nl.items():
        for j in i:
            if j <= low:
                low = j
                found_low = n
            if j >= high:
                high = j
                found_high = n
    for c, i in cl.items():
        for j in i:
            if j <= low:
                low = j
                found_low = c
            if j >= high:
                high = j
                found_high = c
    return int(f"{found_low}{found_high}")


def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print(f"Usage: {sys.argv[0]} file_to_process")
    else:
        file = args[0]
        process_file(file)


if __name__ == "__main__":
    main()
