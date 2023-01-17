#!/usr/bin/python3
for n in range(10):
    for m in range(10):
        if m > n:
            print("{}{}".format(n, m), end="")
            if n < 8:
                print(", ", end="")
print()
