#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv) - 1  # count the shell arguments, but not this script
    print(argc, end=" ")
    print(f"argument{'' if argc == 1 else 's'}{'.' if not argc else ':'}")
    # possible outputs:
    # 0 arguments.
    # 1 argument:
    # 2 arguments:
    # ...

    argc += 1  # list the argument indexes from index 1 to the last,
    # without this executable
    for index in range(1, argc):
        argument = argv[index]
        print(f"{index}: {argument}")
