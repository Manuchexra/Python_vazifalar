#1-masala
fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi')
print(fruits[0], fruits[-1])
print(fruits[2])

#2-masala
numbers = (1, 2, 3, 4, 2, 5, 6, 2)
print(numbers.count(2))
print(numbers.index(5))

#3-masala
colors = ('red', 'green', 'blue')
colors_list = list(colors)
colors_list.append('yellow')
colors = tuple(colors_list)
print(colors)

#4-masala
letters = ('a', 'b', 'c', 'd', 'e')
reversed_letters = tuple(reversed(letters))
print(reversed_letters)

#5-masala
nested_tuple = (1, 2, (3, 4, 5), 6, 7)
print(nested_tuple[2][1])
for element in nested_tuple:
    if isinstance(element, tuple):
        for sub_element in element:
            print(sub_element)
    else:
        print(element)

#6-masala
my_tuple = (10, 20, 30, 40, 50)
my_list = list(my_tuple)
my_list.append(60)
my_tuple = tuple(my_list)
print(my_tuple)

#7-masala
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result_tuple = tuple1 + tuple2
print(result_tuple)