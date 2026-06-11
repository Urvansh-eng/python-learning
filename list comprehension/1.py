# List comprehension = A concise way to create lists in Python
#
#                      Compact and easier to read than traditional loops
#
#                      [expression for value in iterable if condition]


double = [x * 2 for x in range(1,11)]
triple = [y * 3 for y in range(1,11)]
square = [z * z for z in range(1,11)]

print(double)
print(triple)
print(square)


fruit = ["apple","banana","pineapple","mango"]

fruits=[fruit.upper() for fruit in fruit]
print(fruits)


numbers = [1,2,-3,-5,3,-7]
positive_num = [num for num in numbers if num >= 0]
negative_num = [num for num in numbers if num <= 0]
print(positive_num)
print(negative_num)


grades =[24,56,78,93,89,34,68,89,55]

passing_grade = [grade for grade in grades if grade >=65]
print(f"those who pass are : {passing_grade}")