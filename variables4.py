Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a,b,c=20
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a,b,c=20
TypeError: cannot unpack non-iterable int object
>>> a=b=c=20
>>> print(a,b,c)
20 20 20
>>> a,b,c=3,4,5,6,7,8,9
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a,b,c=3,4,5,6,7,8,9
ValueError: too many values to unpack (expected 3, got 7)
>>> a,b,c=6,7,8
>>> print(a,b,c)
6 7 8
>>> fname="bharath"
>>> lname="m"
>>> 
>>> 
>>> pprint(fname+lname)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pprint(fname+lname)
NameError: name 'pprint' is not defined. Did you mean: 'print'? Or did you forget to import 'pprint'?
>>> 
