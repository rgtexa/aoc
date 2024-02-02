import sys


def process_file(path):
    print(path)


def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print(f"Usage: {sys.argv[0]} file_to_process")
    else:
        file = args[0]
        process_file(file)


if __name__ == "__main__":
    main()
