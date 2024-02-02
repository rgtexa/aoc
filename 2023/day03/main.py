import sys


def process_file(path):
    with open(path) as f:
        # line = f.readline().rstrip()
        v = []
        for line in f:
            p = line.rstrip().split(".")
            for i in p:
                if len(i) > 0:
                    v.append(i)
        print(v)


def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print(f"Usage: {sys.argv[0]} file_to_process")
    else:
        file = args[0]
        process_file(file)


if __name__ == "__main__":
    main()
