Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
print
<built-in function print>
print ("Hello, world")
Hello, world
print ("Hello, world!")
Hello, world!
age=24
print "age"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print (age)
24
student_name=stephanie
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    student_name=stephanie
NameError: name 'stephanie' is not defined
student_name = stephanie
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    student_name = stephanie
NameError: name 'stephanie' is not defined
>>> student name=stephanie
SyntaxError: invalid syntax
>>> STUDENT NAME=stephanie
SyntaxError: invalid syntax
>>> STUDENT_NAME=stephanie
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    STUDENT_NAME=stephanie
NameError: name 'stephanie' is not defined
>>> STUDENT NAME="stephanie"
SyntaxError: invalid syntax
>>> STUDENT_NAME="stephanie"
>>> print (student_name)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print (student_name)
NameError: name 'student_name' is not defined
>>> print (STUDENT_NAME)
stephanie
>>> greeting="Hello,"
>>> name="stephanie"
>>> print (greeting)+(name)
Hello,
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print (greeting)+(name)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
>>> message=greeting + name + "!"
>>> greeting="Hello,"
... name="stephanie"
SyntaxError: multiple statements found while compiling a single statement
>>> greeting="Hello,"
... name="stephanie"
SyntaxError: multiple statements found while compiling a single statement
>>> greeting="Hello"
>>> name="stephanie"
>>> message=greeting + "," + name + "!"
>>> print (message)
Hello,stephanie!
