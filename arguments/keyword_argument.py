# keyword arguments = an argument preceded by an identifier
#
#                     helps with readability
#                     order of arguments doesn't matter
#
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greetings,title,first,last):
    print(f"{greetings} {title} {first} {last}")

hello("hello",title="Mr.",first="kuro",last="kumo")     




def get_phn(country,area,first,last):
    return(f"{country}-{area}-{first}-{last}")

phn_num = get_phn(country=1,area=123,first=246,last=789)
print(phn_num)