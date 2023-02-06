# Everything In Python is an Object
## FAQ on how mutable and immutable values behave in Python
Each one of these questions has its answer in a file with the question number followed by "-answer.txt" (except for the 19th exercise). Feel free to experiment in the Python console and check all the answers! But try to igure them out in you head first before opening the answer files.

ALL OF THE FOLLOWING QUESTIONS ARE FROM HOLBERTON
0. What function would you use to print the type of an object?
1. How do you get the variable id (which is the memory address in the CPython implementation)?
2. Are _a_ and _b_ the same object?
```
>>> a = 89
>>> b = 100
```
3. Do _a_ and _b_ point to the same object?
```
>>> a = 89
>>> b = 89
```
4. Do _a_ and _b_ point to the same object?
```
>>> a = 89
>>> b = a
```
5. Do _a_ and _b_ point to the same object?
```
>>> a = 89
>>> b = a + 1
```
6. What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```
7. What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```
8. What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
9. What do these 3 lines print? 
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
10. What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
11. What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
12. What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
13. What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
14. What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
15. What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
16. What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
17. What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
18. What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
19. Write a function 
```
def copy_list(a_list):
```
that returns a copy of a list.
20. Is _a_ a tuple?
```
a = ()
```
21. Is _a_ a tuple?
```
a = (1, 2)
```
22. Is _a_ a tuple?
```
a = (1)
```
23. Is _a_ a tuple?
```
a = (1, )
```
24. What does this script print?
```
a = (1)
b = (1)
a is b
```
25. What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```
26. What does this script print?
```
a = ()
b = ()
a is b
```
27. What does this script print?
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
28. What does this script print?
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
