>>> def find_largest(numbers):
...     if not numbers:
...         return None  # Return None if the list is empty
...     return max(numbers)
...
>>> print(find_largest([1, 2, 3, 4]))
4
>>> print(find_largest([10, 20, 5]))
20
>>> def check_letter(word, letter):
...     return letter in word
...
>>> print(check_letter("apple", "a"))
True
>>> print(check_letter("banana", "z"))
False
>>>
>>> def count_to_number(number):
...     for i in range(1, number + 1):
...         print(i)
...
>>> count_to_number(3)
1
2
3
>>>
... count_to_number(5)
1
2
3
4
5
>>>