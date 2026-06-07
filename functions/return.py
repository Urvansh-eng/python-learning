# return = statement used to end a function
#
#          and send a result back to the caller


def sum(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(sum(1,23))
print(subtract(33,23))
print(multiply(1,23))
print(divide(230,23))



def create_name(name,surname):
    name = name.capitalize()
    surname = surname.capitalize()
    return name + " " + surname

full_name = create_name("my","atlantis")
print(full_name)