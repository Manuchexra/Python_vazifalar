#1-masala
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
del fruits[1]  
del fruits[2]  
print(fruits)

#2-masala
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [num for num in numbers if num % 2 != 0]
print(numbers)

#3-masala
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
del my_list[3:6]
print(my_list)


#4-masala
cities = ["New York", "London", "Tokyo", "Moscow", "Paris"]
del cities[2]
print(cities)

#5-masala
numbers = [5, 10, 15, 20, 25]
numbers = numbers[1:-1]
print(numbers)

#6-masala
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits = ["banana"]
print(fruits)

#7-masala
items = [1, 2, 3, 4, 5]
items.clear()
print(items)

#8-masala
cars = ["Toyota", "Ford", "BMW", "Audi"]
car = cars.pop(1)
cars.append(car)
print(cars)

#9-masala
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)