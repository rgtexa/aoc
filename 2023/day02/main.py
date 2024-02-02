import sys

MAX_BLUE = 14
MAX_RED = 12
MAX_GREEN = 13


def process_file(path):
    with open(path) as f:
        # line = f.readline().rstrip()
        total = 0
        total_power = 0
        for line in f:
            game_power = 1
            # print(line)
            game = line.split(": ")
            pulls = game[1].split("; ")
            seen_red = 0
            seen_green = 0
            seen_blue = 0
            for pull in pulls:
                cubes = pull.split(", ")
                # print(cubes)
                for i in range(0, len(cubes)):
                    cube = cubes[i].split()
                    if cube[1] == "blue":
                        if seen_blue < int(cube[0]):
                            seen_blue = int(cube[0])
                    elif cube[1] == "red":
                        if seen_red < int(cube[0]):
                            seen_red = int(cube[0])
                    elif cube[1] == "green":
                        if seen_green < int(cube[0]):
                            seen_green = int(cube[0])
            if seen_blue > 0:
                game_power *= seen_blue
            if seen_green > 0:
                game_power *= seen_green
            if seen_red > 0:
                game_power *= seen_red
            # print(f"sb: {seen_blue}, sr: {seen_red}, sg: {seen_green}")
            if (
                (seen_green <= MAX_GREEN)
                and (seen_blue <= MAX_BLUE)
                and (seen_red <= MAX_RED)
            ):
                # print(f"{game[0]} possible!")
                total += int(game[0].split()[1])
            # else:
            # print(f"{game[0]} NOT possible!")
            total_power += game_power
    print(f"Total power: {total_power}")


def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print(f"Usage: {sys.argv[0]} file_to_process")
    else:
        file = args[0]
        process_file(file)


if __name__ == "__main__":
    main()
