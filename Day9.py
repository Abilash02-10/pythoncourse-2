Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = set()
s = {1,2,3,4,5,6,7,8}
s
{1, 2, 3, 4, 5, 6, 7, 8}
s.add(1)
s.add(12.2)
s.add(2 + 4j)
s.add()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s ={1,1,1,1,1}
s
{1}
l = {10,2,30,}
m = {1,2,3,4}
l+ m
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l+ m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a = {1,2,3,4}
b = {6789}
b = {6789}
b = {6,7,8,9}
a | b
{1, 2, 3, 4, 6, 7, 8, 9}
a  & b
set()
a - b
{1, 2, 3, 4}
a ^ b
{1, 2, 3, 4, 6, 7, 8, 9}
{1} <=a
True
{1,2}<=a
True
a
{1, 2, 3, 4}
{1,2,3,4}<=a
True
b
{8, 9, 6, 7}
a .isdisjoint(b)
True
a.isdisjoint(b)
True
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 6, 7, 8, 9}
a.intersect(b)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.intersect(b)
AttributeError: 'set' object has no attribute 'intersect'. Did you mean: 'intersection'?
a.issuperset(b)
False
a
{1, 2, 3, 4}
b in a
False
7 in a
False
a
{1, 2, 3, 4}
min(a)
1
max(a)
4
sorted(a)
[1, 2, 3, 4]
sum(a)
10
a
{1, 2, 3, 4}
b = a
b
{1, 2, 3, 4}
b.add(12)
b
{1, 2, 3, 4, 12}
a
{1, 2, 3, 4, 12}
c = a.copy()
c.add(12)
c.add(13)
c
{1, 2, 3, 4, 12, 13}
a.add(123)
a
{1, 2, 3, 4, 12, 123}
a.update({15,12,23})
a
{1, 2, 3, 4, 12, 15, 23, 123}
a.discard(12)
a.discard(4)
a
{1, 2, 3, 15, 23, 123}
a.remove(3)
a
{1, 2, 15, 23, 123}
a.pop()
1
a
{2, 15, 23, 123}
b.pop()
2
a
{15, 23, 123}
all(a)
True
any(a)
True
a = frozenset({1,11,22,33})
a
frozenset({1, 11, 22, 33})
a.add(12)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
#dictionary
d = {}
d = dict{}
SyntaxError: invalid syntax
type(d)
<class 'dict'>
d = {'k1' : 'v1', 'k2':'v2','k3':'v3'}
id(d)
3227049399936
d['k4'] = 'v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d['k4'] = 'v3'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v3'}
d[1] = 'int'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v3', 1: 'int'}
d[12.3] = 'fit'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v3', 1: 'int', 12.3: 'fit'}
>>> d['str']= 'string'
>>> d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v3', 1: 'int', 12.3: 'fit', 'str': 'string'}
>>> d[(1,2,3)]= 'tuple'
>>> d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v3', 1: 'int', 12.3: 'fit', 'str': 'string', (1, 2, 3): 'tuple'}
>>> 9 in d
False
>>> 'str' in d
True
>>> d[k1]
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    d[k1]
NameError: name 'k1' is not defined
>>> d.get(10)
>>> d.get(1)
'int'
>>> d.get(10,"key is not present")
'key is not present'
>>> d.get(k1,"key is present")
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    d.get(k1,"key is present")
NameError: name 'k1' is not defined
>>> d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v3', 1: 'int', 12.3: 'fit', 'str': 'string', (1, 2, 3): 'tuple'}
>>> d[k1] = '12'
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    d[k1] = '12'
NameError: name 'k1' is not defined
>>> d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v3', 1: 'int', 12.3: 'fit', 'str': 'string', (1, 2, 3): 'tuple'}
>>> d[k1] = 12
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    d[k1] = 12
NameError: name 'k1' is not defined
