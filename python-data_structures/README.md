# Python Data Structures
## Python: How to iterate through, modify and copy, lists, and how to work with iterables OF lists, tuples and strings
## Disclaimer
MUTABLE DEFAULT PARAMETERS LIKE THIS:
```
def test(default=[]):
```
WERE PART OF THE REQUIREMENT OF THE EXERCISES AT HOLBERTON.
UNFORTUNATELY, THEY CAN BE A REAL CURVEBALL FOR MOST BEGGINERS,
AND THAT'S WHY I'VE PUT THIS WARNING HERE, ALONG WITH
EVERY SINGLE EXERCISE THAT CONTAINS IT.

### Explanation
MUTABLE DEFAULT ARGUMENTS
ARE DEFINED AT FUNCTION DEFINITION
TIME, AND NOT AT FUNCTION CALL TIME!!!

THIS MEANS THE LIST ABOVE IS PUT INTO MEMORY
WHEN THIS FUNCTION GETS DEFINED,
AND EVERY TIME THIS FUNCTION IS CALLED WITH
THE DEFAULT PARAMETER, THE LOADED PARAMETER
WILL BE THE SAME LIST LOADED THE LAST TIME,
AND NOT A NEW LIST. THIS CAN HAVE THE PREVIOUS
CALLS AFFECT THE EMPTY LIST BY THE TIME THE
CURRENT CALL RUNS.

FOR A CLEARER EXPLANATION, VISIT:
https://docs.python-guide.org/writing/gotchas/

## Directory
0. how to print all items in a list
- how to iterate through a list (or any iterable) in a for-loop
1. how to get an item from a list at an index
2. how to replace an item from a list at an index with another item
3. how to iterate through a list in reverse
- how to use the built-in 'reversed' iterable
- how to check if a value is None
4. how to replace an item from a list at an index in a COPY of that list
5. how to create a copy of a string without it's "c" or "C" substrings
- how to use the str.join method
- how to use a generator comprehension (a generator is just another iterable)
- how to use the "if" syntax in a generator comprehension
6. how to print all items in a matrix
- how to use nested for-loops
7. how to add the first two items of two tuples with the other tuple's corresponding item to create a new tuple
8. how to return tuples
- tuples don't always need parenthesis!!! :)
9. how to find the biggest int (or any item that can be compared) in a list WITHOUT USING 'max'
- look at exercise 0 for help
- short-circuiting
10. how to make a list with booleans that correspond to ints being devisible by 2 in another list
11. how to delete an item at an index in a list without using 'list.pop'
- del keyword
12. how to swap values with tuple unpacking
