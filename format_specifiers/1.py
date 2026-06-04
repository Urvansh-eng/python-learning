# format specifiers = {:flags} format a value based on what
#                     flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator



price1 = 30000.1456
price2 = -45600.14
price3 = 120000.34

print(f"price one is ₹{price1:.2f}")
print(f"price one is ₹{price2:.2f}")
print(f"price one is ₹{price3:.2f}")

print(f"price one is ₹{price1:010}")
print(f"price one is ₹{price2:010}")
print(f"price one is ₹{price3:010}")

print(f"price one is ₹{price1:<010}")
print(f"price one is ₹{price2:<010}")
print(f"price one is ₹{price3:<010}")

print(f"price one is ₹{price1:>010}")
print(f"price one is ₹{price2:>010}")
print(f"price one is ₹{price3:>010}")

print(f"price one is ₹{price1:^10}")
print(f"price one is ₹{price2:^10}")
print(f"price one is ₹{price3:^10}")

print(f"price one is ₹{price1:+}")
print(f"price one is ₹{price2:+}")
print(f"price one is ₹{price3:+}")

print(f"price one is ₹{price1:,}")
print(f"price one is ₹{price2:,}")
print(f"price one is ₹{price3:,}")

print(f"price one is ₹{price1:+,.2f}")
print(f"price one is ₹{price2:+,.2f}")
print(f"price one is ₹{price3:+,.2f}")
