import sys
import functools

def process_file(file):
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
    print(file)
    foundn = []
    foundc = []
    with open(file) as f:
        #for line in f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        print(line.rstrip())
        for c in line:
            if c.isnumeric():
                foundn.append(c)
        fc = []
        for char in alpha:
            res = [i for i in range(len(line)) if line.startswith(char, i)]
            if len(res) > 0:
                for i in range(0, len(res)):
                    fc.append(char)
        for i in fc:
            foundc.append(str(alpha[i]))
        #foundc.append(alpha[l])
    print(foundn)
    print(foundc)



def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print(f'Usage: {sys.argv[0]} file_to_process')
    else:
        file = args[0]
        process_file(file)

if __name__ == "__main__":
    main()