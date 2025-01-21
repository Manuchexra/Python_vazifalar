#1-masala
numbers = [10, 20, 30, 40, 50]
numbers[0] = 100
numbers.append(60)
print(len(numbers))
print(numbers)

#2-masala
fruits = ['apple', 'banana', 'cherry']
fruits.extend(['orange', 'kiwi'])
fruits[1] = 'mango'
fruits.sort()
print(fruits)

#3-masala
students = ['Ali', 'Olim', 'Zarina', 'Jasur', 'Sabina']
print(students.index('Zarina'))
print(students[0], students[-1])

#4-masala
my_tuple = (5, 10, 15, 20, 25)
print(my_tuple[2])
print(len(my_tuple))

#5-masala
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

#6-masala
colors = ('red', 'green', 'blue')
colors_list = list(colors)
colors_list.append('yellow')
colors = tuple(colors_list)
print(colors)

#7-masala
numbers = [5, 10, 15, 20, 25]
numbers.append(30)
numbers.reverse()
print(numbers)

my_tuple = (10, 20, 30, 40)
reversed_tuple = tuple(reversed(my_tuple))
print(reversed_tuple)

#8-masala
num_list = [10, 20, 30, 40]
num_tuple = (50, 60, 70, 80)
combined_list = num_list + list(num_tuple)
print(max(combined_list), min(combined_list))

#9-masala
nested_tuple = (1, 2, (3, 4, 5), 6, 7)
print(nested_tuple[2])
for element in nested_tuple:
    if isinstance(element, tuple):
        for sub_element in element:
            print(sub_element)
    else:
        print(element)

#10-masala
numbers = [2, 4, 6, 8, 10]
new_numbers = [x * 2 for x in numbers]
print(new_numbers)

#11-masala
my_list = ['apple', 'banana', 'cherry', 'date', 'fig']
my_list.remove('cherry')
my_list.pop()
print(my_list)

#12-masala
ages = [34, 23, 45, 27, 56, 18]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

#13-masala
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = list(set(numbers))
print(unique_numbers)

#14-masala
numbers = (10, 50, 25, 5, 100, 75)
print(max(numbers), min(numbers))

#15-masala
my_list = [10, 20, 30, 40, 50, 60]
pairs = [(my_list[i], my_list[i + 1]) for i in range(0, len(my_list) - 1, 2)]
print(pairs)

#16-masala
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
first_three = alphabet[:3]
last_three = alphabet[-3:]
print(first_three)
print(last_three)

#17-masala
names = ['Ali', 'Olim', 'Zarina', 'Jasur']
for name in names:
    print(f"{name} - talaba")

#18-masala
temperatures = (22, 25, 28, 30, 27, 23)
for temp in temperatures:
    print(temp)

#19-masala
my_list = [1, 5, 'banana', 10, 'apple', 20]
sum_numbers = sum(x for x in my_list if isinstance(x, (int, float)))
print(sum_numbers)

#20-masala
my_list = [10, 20, 30]
my_tuple = (40, 50, 60)
my_list[0], my_tuple = my_tuple[0], (my_list[0], *my_tuple[1:])
print(my_list)
print(my_tuple)