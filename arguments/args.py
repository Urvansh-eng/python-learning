# *args   = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#
#            * unpacking operator
#
#            1. positional 2. default 3. keyword 4. ARBITRARY



def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,3,4,5,5))


def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="kukas",
      city="Jaipur",
      state="Rajasthan",
      zip="123106")


def shipping_labels(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print(arg)
    # for kwargs in kwargs.values():
    #     print(kwargs,end=" ") 
    print(f"{kwargs.get('flat')}")   
    print(f"{kwargs.get('tower')}")   
    print(f"{kwargs.get('society')}")   

shipping_labels("Dr.","kumar","patel","sharma",
                flat="201", 
                tower="A-2",
                society="Avalon")