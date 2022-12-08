# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# creating tuple
new_tuple = tuple((2, "Isaac", ["HaaLand", 23]))
print(new_tuple[2])
new_number = tuple((1, 3, 4))
a, c, d = new_number
print(a, c, d)

fruits = ("Apple", "Banana", "Cherry")
new_list = list(fruits)
print(new_list)
new_list[0] = "Grape"
fruits = tuple(new_list)
print(fruits)

# creating Set
set_sample = ('Isaac', 'Jim', 24, 23, 34)
print(set_sample)

set_sample2 = set(set_sample)
print(set_sample2)

# Set from an Array
numberList = [20, 30, 30, 20, 40]
set_sample3 = set(numberList)
print(set_sample3)

book_set = {"Harry Potter", "Angels and Demons", "Locke and Key"}

for item in book_set:
    print(item)

book_set.clear()
print(book_set)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
