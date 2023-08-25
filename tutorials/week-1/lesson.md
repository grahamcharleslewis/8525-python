# Week 1

## Theory

```text
+-------+       +---------+       +--------+
| Input |------>| Process |------>| Output |
+-------+       +---------+       +--------+
```

- Input/output - `input()` and `print()`
- Variables
- Variable assignment
- String - concatenation - `+` (note: overloaded operator)
- String - length - `len()`
- String - from Number conversion - `str()`
- Number - from String conversion - `int()`
- Get the type of something - `type()`
- Get the methods of something - `dir()`


## Practice

### Say hello


```python
# Ask the user to input their name, then display "Hello <name>!"

name = input("Please enter your name: ")
response = "Hello " + name + "!"
print(response)
```

### How long is a piece of string?

```python
# Ask the user to input some random text.
# Display the text and number of characters in the string.

text = input("Please enter some text: ")
length = len(text)
response = text + " has " + str(length) + " characters"
print(response)
```

### Print a quote

```python
# Ask the user to input a quote, then ask the authors name.
# Display the name of the author and the quote in quote marks (").

quote = input("Quote: ")
author = input("Author: ")
response = author + ' said "' + quote + '"'
print(response)
```

### Basic calculator for 2 numbers

```python
# Ask the user for 2 integer numbers.
# Display the results of adding, subtracting, multiplying and dividing
# those two numbers.

a = int(input("First number: "))
b = int(input("Second number: "))
a_plus_b = str(a + b)
a_minus_b = str(a - b)
a_times_b = str(a * b)
a_div_b = str(a / b)
print(str(a) + " + " + str(b) + " = " + a_plus_b)
print(str(a) + " - " + str(b) + " = " + a_minus_b)
print(str(a) + " * " + str(b) + " = " + a_times_b)
print(str(a) + " / " + str(b) + " = " + a_div_b)
```