>>> my_list = [1, 2, 3, 4]
...
... for value in my_list:
...     print(value)
...
1
2
3
4
>>> my_list = [1, 2, 3, 4]
...
... for value in my_list:
...     print(value*20)
...
20
40
60
80
>>> list = ["Elie", "Tim", "Matt"]
... first_letters = [name[0] for name in list]
... print(first_letters)
...
['E', 'T', 'M']
>>> list = [1, 2, 3, 4, 5, 6]
... even_numbers = [num for num in list if num % 2 == 0]
... print(even_numbers)
...
[2, 4, 6]
>>> list1 = [1, 2, 3, 4]
... list2 = [3, 4, 5, 6]
...
... intersection = [num for num in list1 if num in list2]
... print(intersection)
...
[3, 4]
>>> list = ["Elie", "Tim", "Matt"]
... reversed_lower = [word[::-1].lower() for word in list]
... print(reversed_lower)
...
['eile', 'mit', 'ttam']
>>> list1 = "first"
... list2 = "third"
...
... common_letters = list(set(list1) & set(list2))
... print(common_letters)
...
Traceback (most recent call last):
  File "<python-input-6>", line 4, in <module>
    common_letters = list(set(list1) & set(list2))
TypeError: 'list' object is not callable
>>> list1 = "first"
... list2 = "third"
...
... common_letters = list(set(first) & set(third))
... print(common_letters)
...
Traceback (most recent call last):
  File "<python-input-7>", line 4, in <module>
    common_letters = list(set(first) & set(third))
                              ^^^^^
NameError: name 'first' is not defined. Did you mean: 'list'?
>>> list1 = "first"
... list2 = "third"
...
... common_letters = list(set(list1) & set(list2))
... print(common_letters)
...
Traceback (most recent call last):
  File "<python-input-8>", line 4, in <module>
    common_letters = list(set(list1) & set(list2))
TypeError: 'list' object is not callable
>>> first = "first"
... third = "third"
...
... common_letters = list(set(first) & set(third))
... print(common_letters)
...
Traceback (most recent call last):
  File "<python-input-9>", line 4, in <module>
    common_letters = list(set(first) & set(third))
TypeError: 'list' object is not callable
>>> list1 = "first"
... list2 = "third"
...
... common_letters = set(list1) & set(list2))
... print(common_letters)
...
  File "<python-input-10>", line 4
    common_letters = set(list1) & set(list2))
                                            ^
SyntaxError: unmatched ')'
>>> list1 = "first"
... list2 = "third"
...
... common_letters = set(list1) & set(list2)
... print(common_letters)
...
{'i', 'r', 't'}
>>> list = range(1, 101)
>>>
>>>
>>> list = range(0, 100)
>>>
>>> list = range(0, 100):
  File "<python-input-17>", line 1
    list = range(0, 100):
                        ^
SyntaxError: invalid syntax
>>> list = range(0, 100) :
  File "<python-input-18>", line 1
    list = range(0, 100) :
                         ^
SyntaxError: invalid syntax
>>> list = range(0, 100)
... div_by_12 = [num for num in list if num % 12 == 0]
... print(div_by_12)
...
[0, 12, 24, 36, 48, 60, 72, 84, 96]
>>> word = "amazing"
... vowels = "a, e, i, o, u"
... result = [char for char in word if char not in vowels]
... print(result)
...
...
['m', 'z', 'n', 'g']
>>> list = (0, 1, 2)
... z = list.copy()
... print(z)
...
Traceback (most recent call last):
  File "<python-input-21>", line 2, in <module>
    z = list.copy()
        ^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'copy'
>>> list = (0, 1, 2)
>>> list = (0, 1, 2) copy1 = list.copy()
  File "<python-input-23>", line 1
    list = (0, 1, 2) copy1 = list.copy()
                     ^^^^^
SyntaxError: invalid syntax
>>> list = (0, 1, 2)
>>>     copy1 = list.copy()
  File "<python-input-25>", line 1
    copy1 = list.copy()
IndentationError: unexpected indent
>>> list = (0, 1, 2)
... copy1 = list.copy()
... copy2 = list.copy()
... result = [copy1, copy2]
... print()
...
Traceback (most recent call last):
  File "<python-input-26>", line 2, in <module>
    copy1 = list.copy()
            ^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'copy'
>>> chiffre = (0, 1, 2)
... copy1 = chiffre.copy()
... copy2 = chiffre.copy()
... result = [copy1, copy2]
... print(result)
...
Traceback (most recent call last):
  File "<python-input-27>", line 2, in <module>
    copy1 = chiffre.copy()
            ^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'copy'
>>> original = [0, 1, 2]
... copy1 = original.copy()
... copy2 = original.copy()
...
... result = [copy1, copy2]
... print(result)
...
[[0, 1, 2], [0, 1, 2]]
>>> chiffre = [0, 1, 2]
... copy1 = chiffre.copy()
... copy2 = chiffre.copy()
... result = [copy1, copy2]
... print(result)
...
[[0, 1, 2], [0, 1, 2]]