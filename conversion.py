# name = input("Please enter your name: ")
# print(f'Hello {name}')

numbers = range(256)
for i in numbers:
    print(f'{i}\t{hex(i)}\t{bin(i)}')