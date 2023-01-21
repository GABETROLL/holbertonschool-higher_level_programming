#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    # assuming all arguments are valid numbers:
    print(
            sum(
                int(arg) for arg in argv[1:]
                )
            )
    # gets all the arguments except the first one, by taking
    # a slice of it, and uses the 'sum' function to add
    # all the arguments in it, casted to ints using the
    # generator expression (aka the for loop, a slot in memory
    # aka 'arg' with the next int(value) in argv)

    # and yes, those new lines are allowed
