#!/usr/bin/python3
for n in range(0, 99):
    print("{} = {}".format(n, hex(n)))
    # the format function just looks at the number's '__str__' attribute,
    # which tells Python what it's string form should be, pretty cool right?
    # :D
    # Also, the 'hex(n)' value is already a string! :)
