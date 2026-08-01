Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
data = { "name" : 'abhi',"batch" : 64, "course" : "python" }
data["name"]
'abhi'
63 in data
False
data.get('age','key is not present')
'key is not present'
data.get('course','key is not present')
'python'
data ["batch"] = 64
data
{'name': 'abhi', 'batch': 64, 'course': 'python'}
data["skills'] = ['python','mysql','flask']
     
SyntaxError: unterminated string literal (detected at line 1)
data["skills"] = ['python','mysql','flask']
     
data
     
{'name': 'abhi', 'batch': 64, 'course': 'python', 'skills': ['python', 'mysql', 'flask']}
data.update){'phno' : 9876543210}
SyntaxError: unmatched ')'
data.update({'phno' : 9876543210})
data
{'name': 'abhi', 'batch': 64, 'course': 'python', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210}
data.pop('age')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data.pop('age')
KeyError: 'age'
data.pop('name')
'abhi'
del data['batch']
data
{'course': 'python', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210}
data.popitem()
('phno', 9876543210)
data
{'course': 'python', 'skills': ['python', 'mysql', 'flask']}
data.clear()
data
{}
data.keys()
dict_keys([])
data.values()
dict_values([])
data.items()
dict_items([])
sorted(data)
[]
data
{}
sirted(data)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sirted(data)
NameError: name 'sirted' is not defined. Did you mean: 'sorted'?
sorted(data)
[]
sorted(data,reverse = true)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    sorted(data,reverse = true)
NameError: name 'true' is not defined. Did you mean: 'True'?
sorted(data,reverse = True)
[]
mar(data)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    mar(data)
NameError: name 'mar' is not defined. Did you mean: 'max'?
max(data)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    max(data)
ValueError: max() iterable argument is empty
max(data)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    max(data)
ValueError: max() iterable argument is empty
min(data)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    min(data)
ValueError: min() iterable argument is empty
data
{}
>>> data = {"name": "abhi","age":33}
>>> max(data)
'name'
>>> min(data)
'age'
>>> data
{'name': 'abhi', 'age': 33}
>>> data['age']
33
>>> data.get('age')
33
>>> data.setdefault('age',0)
33
>>> data.setdefault('roll',44)
44
>>> data
{'name': 'abhi', 'age': 33, 'roll': 44}
>>> data.setdefault('sajid',55)
55
>>> data
{'name': 'abhi', 'age': 33, 'roll': 44, 'sajid': 55}
>>> any(data)
True
>>> all(data)
True
>>> a = {1:1,2:2}
>>> c[4] = 4
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c[4] = 4
NameError: name 'c' is not defined
>>> c
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> d =dict.fromkeys(["a","b"],0)
>>> d
{'a': 0, 'b': 0}
