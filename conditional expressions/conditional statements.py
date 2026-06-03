# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition
# X if condition else Y

A = 1
x = 3
y = 5
Age = 23
user_level = "Guest"
# print("Positive" if A > 0 else "Negative")

# result = "Even" if A%2==0 else "Odd"
# max_num = x if x > y else y
# min_num = x if x < y else y
# status = "Adult" if Age >= 18 else "Child"
Access = "Full access" if user_level == "Admin" else "Limited access"
print(Access)