num_pad = ((1,2,3),
           (4,5,6),
           ("*",0,"#"))


for rows in num_pad:
    for num in rows:
        print(num,end=" ")
    print()