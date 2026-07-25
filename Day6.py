Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Built in functions in strings
c = ' python programming'
len(c)
19
ord('a')
97
chr(55)
'7'
min('c')
'c'
max('c')
'c'
min(c)
' '
max(c)
'y'
sorted(c)
[' ', ' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
c='abilash'
c.upper()
'ABILASH'
c.lower()
'abilash'
c.capitalize()
'Abilash'
c.title()
'Abilash'
c.swapcase()
'ABILASH'
c.casefold()
'abilash'
'abilash'.casefold()
'abilash'
#Alingment and formating methods
c.center(60,'_')
'__________________________abilash___________________________'
c.ljust(60,'-')
'abilash-----------------------------------------------------'
c.rjust(60,'_')
'_____________________________________________________abilash'
'12'.zfill(4)
'0012'
'1234567'zfill(6)
SyntaxError: invalid syntax
'1234567'.zfill(6)
'1234567'
'1234567'.zfill(8)
'01234567'
c.find('a')
0
cc.rfind('i')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    cc.rfind('i')
NameError: name 'cc' is not defined. Did you mean: 'c'?
c.rfind('i')
2
c.index(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    c.index(a)
NameError: name 'a' is not defined
c.index('a')
0
c.rindex('s')
5
c.count('h')
1
c.count('a')
2
c.replace('a','b')
'bbilbsh'
c.replace('abilash','reddy')
'reddy'
c.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans('aeiou','12345'))
'1b3l1sh'
c.translate(c.maketrans('aeiou','8888888'))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    c.translate(c.maketrans('aeiou','8888888'))
ValueError: the first two maketrans arguments must have equal length
a = 'abilash is studing'
a.split()
['abilash', 'is', 'studing']
'abilash is studing'.split()
['abilash', 'is', 'studing']
'abilash is studing'.split(',')
['abilash is studing']
a.split('_')
['abilash is studing']
'abilash is studing'.rsplit()
['abilash', 'is', 'studing']
a.splitlines()
['abilash is studing']
b = '''
python
is
program
'''
c.splitlines()
['abilash']
b.splitlines()
['', 'python', 'is', 'program']
''.join(['','python','program','lang'])
'pythonprogramlang'
'_'.join(['','python','program','lang'])
'_python_program_lang'
d = 'i am sai charan'
d.partition('_')
('i am sai charan', '', '')
d.rpartition('_)
             
SyntaxError: unterminated string literal (detected at line 1)
d.rpartition('_')
             
('', '', 'i am sai charan')
>>> #strips
...              
>>> d.strip()
...              
'i am sai charan'
>>> d.rstrip()
...              
'i am sai charan'
>>> y = 'vgsthymya hgdjduya'
...              
>>> y.strip()
...              
'vgsthymya hgdjduya'
>>> y = '        vgsthymya     hgdjduya'
...              
>>> y.strip()
...              
'vgsthymya     hgdjduya'
>>> y.rstrip()
...              
'        vgsthymya     hgdjduya'
>>> #Encode
...              
>>> text 'abilash #'
...              
SyntaxError: invalid syntax
>>> text = 'abilash #'
...              
>>> text.encode()
...              
b'abilash #'
>>> text.decode()
...              
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> b'abilash #'.decode()
...              
'abilash #'
