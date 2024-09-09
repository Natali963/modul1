my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
l = my_list
a = len(l)
i = 0


while i <= a:
    if l [i] <= 0:
        i += 1
        continue
    print(l[i])
    i += 1
    if l [i] <= 0:
        i += 1
        break
print(l[i])

    
     

