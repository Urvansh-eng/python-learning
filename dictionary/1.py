# dictionary = a collection of {key:value} pairs
#
#              ordered and changeable. No duplicates

capitals = {"USA" : "Wshington D.C",
            "India" : "New Delhi",
            "China" : "Beijing",
            "Russia" : "Moscow"}
            

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))


# if capitals.get("Russia"):
#     print("This capital exist")
# else:
#     print("That capital doenst exist")

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})
# capitals.pop("India")
# # capitals.popitem()
# # capitals.clear()
# print(capitals)
# keys = capitals.keys()
# print(keys)
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# # print(values)

# for value in capitals.values():
#     print(value)
 
items = capitals.items()
for key, value in capitals.items():
    print(f"{key}:{value}")


