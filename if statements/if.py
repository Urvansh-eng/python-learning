age  = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible")
elif age<=0:
    print("You are not even born yet ")    
else:
    print("You are not eligible")



response = input("Are u good?(Y/N): ")

if response == "Y":
    print("Thats great!")
else:
    print("Have some rest!")
