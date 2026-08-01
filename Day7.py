Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c = 'string.py'
c.startswith('str')
True
c.endswith('py')
True
c.islower()
True
c.isupper()
False
c.isalpha()
False
c.isalnum()
False
's123'.isalnum()
True
's.123'.alnum()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    's.123'.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
's.123'.alnum()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    's.123'.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
>>> 's.123'.isalnum()
False
>>> 's.123'.isalnum()
False
>>> 's123'.isalnum()
True
>>> '      '.isspace()
True
>>> 'h   '.isspace()
False
>>> 'this is title'.istitle()
False
>>> 'This Is Title'.istitle()
True
>>> "my@self'.isidentifier()
SyntaxError: unterminated string literal (detected at line 1)
>>> 'my@self'.isidentifier()
False
>>> 'my_self'.isidentifier()
True
>>> l = []
>>> l = list()
>>> l = [1,2.22, (2+3j),none]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l = [1,2.22, (2+3j),none]
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> l = [1,21,33,2.3,2+3j,'str',[1,2,3]]
>>> l = [1,1,1,1]
>>> type(l)
<class 'list'>
>>> m = [1,2,3]
>>> l+m
[1, 1, 1, 1, 1, 2, 3]
>>> m*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> l[3]
1
