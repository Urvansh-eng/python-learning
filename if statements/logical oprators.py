# logical operators = evaluate multiple conditions (or, and, not)

#     or  = at least one condition must be True
#     and = both conditions must be True
#     not = inverts the condition (not False, not True)




# temp = 25
# is_sunny = False

# if temp < 0 or temp > 35 or is_sunny == False:
#     print("Dont go outside")
# else:
#     print("dont cancel plan")    


temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("Hot outside")
elif temp <= 0 and is_sunny:
    print("Cold outside")
elif temp < 28 and temp > 0 and is_sunny:
    print("You can go outside")
elif temp >= 28 and not is_sunny:
    print("Cloudy")
elif temp <= 0 and not is_sunny:
    print("Cloudy")
elif temp < 28 and temp > 0 and not is_sunny:
    print("Cloudy")