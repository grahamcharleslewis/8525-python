# All datatypes in Python:
# Numeric data types: int, float, complex
# String data types: str
# Sequence types: list, tuple, range
# Binary types: bytes, bytearray, memoryview
# Mapping data type: dict
# Boolean type: bool
# Set data types: set, frozenset

# to find the type of a thing...
print(type(2))

# to find the methods you can call on a thing...
print(dir(2))


list = ["one", "two", "three", "four", "five"]
for number in list:
    print(number)
    
dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
for key, value in dict.items():
    print(f"{key} : {value}")
    
tuple = {
    "dec": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "bin": [0, 1],
    "hex": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 10]
}
for key, values in tuple.items():
    print(f"{key} : {values}")
