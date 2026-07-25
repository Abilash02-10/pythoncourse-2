Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.



#input Formating
#int float str list tuple set dict

int - int(input())
float - float(input())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int - int(input())
ValueError: invalid literal for int() with base 10: 'float - float(input())'
x = input()
abhi
x
'abhi'
name = input()
bharath

name
'bharath'
name = input("enter name")
enter name
name
''
age = input("enter the name")
enter the name:21
age = int(input())
21
age
21
type(age)
<class 'int'>
names = input("enter the name")
enter the name:abhi
name
''
name.split()
[]
name = input("enter the names")
enter the names : abhi mahesh venu
name
' : abhi mahesh venu'
name = input("enter the names:").split
enter the names:
names = input("enter the name")
enter the name
NAME = input("enter the names")
enter the namesname
name =
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
#list of values
a,b = [1,2]
a
1
b
2
a,b = (1,2)
a
1
b
2
email,password = input("enter the email and password")
enter the email and passwordenter
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    email,password = input("enter the email and password")
ValueError: too many values to unpack (expected 2)
email,password = input("enter the email and password :").split()
enter the email and password :abilashreddy@gmail 1234
email
'abilashreddy@gmail'
password
'1234'
int(password)
1234
a,b,c = list(map(int,input().split()))
123
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,b,c = list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 1)
a,b,c = list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
name,marks = input().split()
abhi 12
name
'abhi'
marks
'12'
int(marks)
12
#using Eval function
#using Eval function
e = Eval(input())
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    e = Eval(input())
NameError: name 'Eval' is not defined. Did you mean: 'eval'?
e  = Eval(input())
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    e  = Eval(input())
NameError: name 'Eval' is not defined. Did you mean: 'eval'?
e = eval(input())
1
e
1
e = eval(input())
abhi
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    e = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'abhi' is not defined
NameError: name 'abhi' is not defined
SyntaxError: invalid syntax
e = eval(input())
12.23
e
12.23
e = eval(input())
"abhi"
e
'abhi'
e = eval(input())
[1,2,3]
e
[1, 2, 3]
#strings concept
s =''
s
''
s = 'codegnana'
s
'codegnana'
'codegnan' + 'PFS'
'codegnanPFS'
'codegnana'*10
'codegnanacodegnanacodegnanacodegnanacodegnanacodegnanacodegnanacodegnanacodegnanacodegnana'
'*'*5
'*****'
>>> s = 'codegnan'
>>> s[4]
'g'
>>> s[-1]
'n'
>>> s[-2]
'a'
>>> names = 'sajid abdul srinivas dherraj'
>>> names[0]
's'
>>> names[0:5]
'sajid'
>>> names[:5]
'sajid'
>>> names[6:11]
'abdul'
>>> names[12:20]
'srinivas'
>>> names[21:}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> names[21:]
'dherraj'
>>> names[-1:-8;-1]
SyntaxError: invalid syntax
>>> NAMES[-1:-8:-1]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    NAMES[-1:-8:-1]
NameError: name 'NAMES' is not defined. Did you mean: 'NAME'?
>>> names[-1:-8:-1]
'jarrehd'
>>> names
'sajid abdul srinivas dherraj'
>>> 'sajid' in names
True
>>> 'dherraj' in names
True
>>> 'karthik' in names
False
