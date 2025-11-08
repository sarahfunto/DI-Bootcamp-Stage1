Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cat_years = 15
...         dog_years = 15
...     elif human_years == 2:
...         cat_years = 15 + 9
...         dog_years = 15 + 9
...     else:
...         cat_years = 28 + (human_years)
...         dog_years = 29 + (human_years)
...
...
>>> human_years = 10
>>>
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cat_years = 15
...         dog_years = 15
...     elif human_years == 2:
...         cat_years = 15 + 9
...         dog_years = 15 + 9
...     else:
...         cat_years = 28 + (human_years)
...         dog_years = 29 + (human_years)
...
>>> calculate_pet_years(human_years = 10)
>>>
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cat_years = 15
...         dog_years = 15
...     elif human_years == 2:
...         cat_years = 15 + 9
...         dog_years = 15 + 9
...     else:
...         cat_years = 28 + (human_years)
...         dog_years = 29 + (human_years)
...
>>> return [human_years, cat_years, dog_years]
  File "<python-input-7>", line 1
    return [human_years, cat_years, dog_years]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: 'return' outside function
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cat_years = 15
...         dog_years = 15
...     elif human_years == 2:
...         cat_years = 15 + 9
...         dog_years = 15 + 9
...     else:
...         cat_years = 28 + (human_years)
...         dog_years = 29 + (human_years)
...         return [human_years, cat_years, dog_years]
...
>>> calculate_pet_years(1)
>>>
>>> years = int(input("Enter human years: "))
... result = calculate_pet_years(years)
... print(result)
...
Enter human years: 1
None
>>>
>>> 10
10
>>> def calculate_pet_years(human_years):
... ...     if human_years == 1:
... ...         cat_years = 15
... ...         dog_years = 15
... ...     elif human_years == 2:
... ...         cat_years = 15 + 9
... ...         dog_years = 15 + 9
... ...     else:
... ...         cat_years = 28 + (human_years)
... ...         dog_years = 29 + (human_years)
... ...         return [human_years, cat_years, dog_years]
... years = int(input("Enter human years: "))
... ... result = calculate_pet_years(years)
... ... print(result)
...
  File "<python-input-14>", line 2
    ...     if human_years == 1:
    ^^^
IndentationError: expected an indented block after function definition on line 1
>>>
>>>
>>> def calculate-pet-years(human_years):
  File "<python-input-17>", line 1
    def calculate-pet-years(human_years):
                 ^
SyntaxError: expected '('
>>> def calculate_pet_years(human_years)
  File "<python-input-18>", line 1
    def calculate_pet_years(human_years)
                                        ^
SyntaxError: expected ':'
>>> def calculate_pet_years(human_years):
...     if human_years = 1:
...         cats_years = 15
...         dogs_years = 15
...     elif human_years = 2:
...         cats_years = 24
...         dogs_years = 24
...     else human_years > 2:
...         cats_years = 28 + (human_years)
...         dogs_years = 29 + (human_years)
...     human_years = int(input("Enter Human Years"))
...     result = calculate_pet_years(human_years)
...     print(result)
...
  File "<python-input-19>", line 2
    if human_years = 1:
       ^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cats_years = 15
...         dogs_years = 15
...     elif human_years == 2:
...         cats_years = 24
...         dogs_years = 24
...     else human_years > 2:
...         cats_years = 28 + (human_years)
...         dogs_years = 29 + (human_years)
...     human_years = int(input("Enter Human Years"))
...     result = calculate_pet_years(human_years)
...     print(result)
...
  File "<python-input-20>", line 8
    else human_years > 2:
         ^^^^^^^^^^^
SyntaxError: expected ':'
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cats_years = 15
...         dogs_years = 15
...     elif human_years == 2:
...         cats_years = 24
...         dogs_years = 24
...     else:
...         cats_years = 28 + (human_years)
...         dogs_years = 29 + (human_years)
...     human_years = int(input("Enter Human Years"))
...     result = calculate_pet_years(human_years)
...     print(result)
...
>>>
>>>
>>> calculate_pet_years(10)
Enter Human Years10
Enter Human Years1
Enter Human Years 1
Enter Human Years
Traceback (most recent call last):
  File "<python-input-24>", line 1, in <module>
    calculate_pet_years(10)
    ~~~~~~~~~~~~~~~~~~~^^^^
  File "<python-input-21>", line 12, in calculate_pet_years
    result = calculate_pet_years(human_years)
  File "<python-input-21>", line 12, in calculate_pet_years
    result = calculate_pet_years(human_years)
  File "<python-input-21>", line 12, in calculate_pet_years
    result = calculate_pet_years(human_years)
  File "<python-input-21>", line 11, in calculate_pet_years
    human_years = int(input("Enter Human Years"))
ValueError: invalid literal for int() with base 10: ''
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cats_years = 15
...         dogs_years = 15
...     elif human_years == 2:
...         cats_years = 24
...         dogs_years = 24
...     else:
...         cats_years = 28 + (human_years)
...         dogs_years = 29 + (human_years)
...     human_years = int(input("Enter Human Years"))
...     result = calculate_pet_years(human_years)
...     print(result)
...
>>>
>>>
>>> calculate_pet_years
<function calculate_pet_years at 0x0000026C3422A340>
>>> calculate_pet_years()
Traceback (most recent call last):
  File "<python-input-29>", line 1, in <module>
    calculate_pet_years()
    ~~~~~~~~~~~~~~~~~~~^^
TypeError: calculate_pet_years() missing 1 required positional argument: 'human_years'
>>> calculate_pet_years(human_years)
Enter Human Years1
Enter Human Years10
Enter Human Years30
Enter Human Years
Traceback (most recent call last):
  File "<python-input-30>", line 1, in <module>
    calculate_pet_years(human_years)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "<python-input-25>", line 12, in calculate_pet_years
    result = calculate_pet_years(human_years)
  File "<python-input-25>", line 12, in calculate_pet_years
    result = calculate_pet_years(human_years)
  File "<python-input-25>", line 12, in calculate_pet_years
    result = calculate_pet_years(human_years)
  File "<python-input-25>", line 11, in calculate_pet_years
    human_years = int(input("Enter Human Years"))
ValueError: invalid literal for int() with base 10: ''
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cats_years = 15
...         dogs_years = 15
...     elif human_years == 2:
...         cats_years = 24
...         dogs_years = 24
...     else:
...         cats_years = 28 + (human_years)
...         dogs_years = 29 + (human_years)
...     return [human_years, cat_years, dog_years]
...     human_years = int(input("Enter Human Years"))
...     result = calculate_pet_years(human_years)
...     print(result)
...
>>> calculate_pet_years(human_years)
Traceback (most recent call last):
  File "<python-input-32>", line 1, in <module>
    calculate_pet_years(human_years)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "<python-input-31>", line 11, in calculate_pet_years
    return [human_years, cat_years, dog_years]
                         ^^^^^^^^^
NameError: name 'cat_years' is not defined. Did you mean: 'cats_years'?
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cats_years = 15
...         dogs_years = 15
...     elif human_years == 2:
...         cats_years = 24
...         dogs_years = 24
...     else:
...         cats_years = 28 + (human_years)
...         dogs_years = 29 + (human_years)
...     return [human_years, cats_years, dogs_years]
...     human_years = int(input("Enter Human Years"))
...     result = calculate_pet_years(human_years)
...     print(result)
...
>>> calculate_pet_years(human_years)
[10, 38, 39]
>>>
>>>
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cats_years = 15
...         dogs_years = 15
...     elif human_years == 2:
...         cats_years = 24
...         dogs_years = 24
...     else:
...         cats_years = 28 + (human_years)
...         dogs_years = 29 + (human_years)
...
... return [human_years, cats_years, dogs_years]
... human_years = int(input("Enter Human Years"))
... result = calculate_pet_years(human_years)
... print(result)
...
  File "<python-input-37>", line 12
    return [human_years, cats_years, dogs_years]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: 'return' outside function
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cats_years = 15
...         dogs_years = 15
...     elif human_years == 2:
...         cats_years = 24
...         dogs_years = 24
...     else:
...         cats_years = 28 + (human_years)
...         dogs_years = 29 + (human_years)
...
...     return [human_years, cats_years, dogs_years]
... human_years = int(input("Enter Human Years"))
... result = calculate_pet_years(human_years)
... print(result)
...
Enter Human Years1
[1, 15, 15]
>>>
>>>
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cats_years = 15
...         dogs_years = 15
...     elif human_years == 2:
...         cats_years = 24
...         dogs_years = 24
...     else:
...         cats_years = 28 + (human_years)
...         dogs_years = 29 + (human_years)
...
...     return [human_years, cats_years, dogs_years]
... human_years = int(input("Enter Human Years"))
... result = calculate_pet_years(human_years)
... print(result)
...
Enter Human Years2
[2, 24, 24]
>>> def calculate_pet_years(human_years):
...     if human_years == 1:
...         cats_years = 15
...         dogs_years = 15
...     elif human_years == 2:
...         cats_years = 24
...         dogs_years = 24
...     else:
...         cats_years = 28 + (human_years)
...         dogs_years = 29 + (human_years)
...
...     return [human_years, cats_years, dogs_years]
... human_years = int(input("Enter Human Years"))
... result = calculate_pet_years(human_years)
... print(result)
...
Enter Human Years15
[15, 43, 44]
>>>