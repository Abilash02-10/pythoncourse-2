Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tokens
>>> length = 10
>>> width = 5
>>> area = length * width
>>> if area > 30:
...     print('large area')
...     else ;
...     
SyntaxError: invalid syntax
>>> if area > 30:
...     print('large area')
...     else ;
...     
SyntaxError: invalid syntax
>>> else :
...     
SyntaxError: invalid syntax
>>> else:
...     
SyntaxError: invalid syntax
>>> #keyword
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> a,b,c = 10,20,30
>>> print(a,b,c)
10 20 30
>>> x = 100
>>> del x
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
