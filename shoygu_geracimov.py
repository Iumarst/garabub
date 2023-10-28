#1
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

print('-' * 30)

#2
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

print('-' * 30)

#3
name, age, company = ("Илья", 18, "НГТУ")
print(name)
print(age)
print(company)

print('-' * 30)

#4
people = ["Андрей", "Екатерина", "Сергей"]
first, second, third = people
print(first)
print(second)
print(third)

print('-' * 30)

#5
dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}
r, b, g = dictionary
print(r)
print(b)
print(g)
print(dictionary[g])

print('-' * 30)

#6
people = [
    ("Андрей", 17, "НГТУ"),
    ("Екатерина", 17, "НГУ"),
    ("Сергей", 19, "НГУЭУ")
]

for name, age, company in people:
    print(f"Name: {name}, Age: {age}, Company: {company}")

print('-' * 30)

#7
people = ["Андрей", "Екатерина", "Сергей"]
for index, name in enumerate(people):
    print(f"{index}.{name}")

print('-' * 30)

#8
person =("Илья", 18, "НГТУ")
name, _, company = person
print(name)
print(company)

print('-' * 30)

#9
name, _, company = person
print(_)

print('-' * 30)

#10
num1=1
num2=2
num3=3
*numbers,=num1,num2,num3
print(numbers)

print('-' * 30)

#11
head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)

print('-' * 30)

#12
*head, tail = [1, 2, 3, 4, 5]

print(head)
print(tail)

print('-' * 30)

#13
head, *middle, tail = [1, 2, 3, 4, 5]

print(head)
print(middle)
print(tail)

print('-' * 30)

#14
first, second, *other = [1, 2, 3, 4, 5]

print(first)
print(second)
print(other)

print('-' * 30)

#15
first, _, third, *_, last = [1, 2, 3, 4, 5, 6, 7, 8]

print(first)
print(third)
print(last)

print('-' * 30)

#16
red, *other, green = {"red":"красный", "blue":"синий", "yellow":"желтый", "green":"зеленый"}

print(red)
print(green)
print(other)

print('-' * 30)

#17
nums1 = [1, 2, 3]
nums2 = (4, 5, 6)

nums3 = [*nums1, *nums2]
print(nums3)

print('-' * 30)

#18
dictionary1 = {"red":"красный", "blue":"синий"}
dictionary2 = {"green":"зеленый", "yellow":"желтый"}

dictionary3 = {**dictionary1, **dictionary2}
print(dictionary3)

print('-' * 30)