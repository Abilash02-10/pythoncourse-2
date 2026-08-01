Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l = [1,2,3,4]
l = [10,19,6,5,4,1]
id(l)
2431451909056
l.insert(3)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    l.insert(3)
TypeError: insert expected 2 arguments, got 1
l.extend([53,42,31])
l
[10, 19, 6, 5, 4, 1, 53, 42, 31]
l[3] = 60
l
[10, 19, 6, 60, 4, 1, 53, 42, 31]
l.pop()
31
l.remove(6)
l
[10, 19, 60, 4, 1, 53, 42]
l.clear()
l
[]
id(l)
2431451909056
del l[1]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    del l[1]
IndexError: list assignment index out of range
max(l)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    max(l)
ValueError: max() iterable argument is empty
l = [15,20,6,8]
l(max)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l(max)
TypeError: 'list' object is not callable
max(l)
20
min(l)
6
sorted(l)
[6, 8, 15, 20]
l.reverse()
l
[8, 6, 20, 15]
l.sort()
l
[6, 8, 15, 20]
l.sort(reverse = True)
sum(1)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sum(1)
TypeError: 'int' object is not iterable
sum(l)
49
l = [1,2,3]
m = [1,2,3]
>>> l
[1, 2, 3]
>>> m
[1, 2, 3]
>>> l.append(5)
>>> l
[1, 2, 3, 5]
>>> m = l.copy()
>>> m
[1, 2, 3, 5]
>>> m.append(7)
>>> m
[1, 2, 3, 5, 7]
>>> l
[1, 2, 3, 5]
>>> all([10,'',[],(),set(),{},False])
False
>>> all([10,'',[],(),set(),{},False])
False
>>> any([1,'',[],(),set(),{},False])
True
>>> l.index(2)
1
>>> l.count(20)
0
>>> #nested list
>>> l =
SyntaxError: invalid syntax
>>> l =[[1,2,3,4],[5,6,7,8]]
>>> l[0]
[1, 2, 3, 4]
>>> l[1]
[5, 6, 7, 8]
>>> l[0][1]
2
>>> l[1][1]
6
>>> l[-1][-1]
8
>>> #tuple
