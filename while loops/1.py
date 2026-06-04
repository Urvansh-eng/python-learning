# execute some code while some conditions remains true

# name = input("Enter your name: ")

# while name == "":
#     print("u didnt enter your name")
#     name = input("Enter your name: ")

# print(f"Welcome {name}")    

# age = int(input("Enter your age: "))

# while age < 0 :
#     print("age invalid")
#     age = int(input("Enter your age: "))

# print(f"U are {age} year old" )    


# food = input("Enter ur fav. food (q to quit): ")

# while not food == "q":
#     print(f"Your fav food is {food}")
#     food = input("Enter another fav. food (q to quit): ")

# print("Bye")    

num = int(input("Enter num between 1 to 10: "))

while num < 1 or num > 10:
    print("Enter within range of 1 to 10")
    num = int(input("Enter num between 1 to 10"))
print(f"user selected number {num}")    

