grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
print(grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
s = sorted(students)
print (s)

a = (sum(grades[0]) / len(grades[0]))
b = (sum(grades[1]) / len(grades[1]))
c = (sum(grades[2]) / len(grades[2]))
d = (sum(grades[3]) / len(grades[3])) 
h = (sum(grades[4]) / len(grades[4]))
grades_ = a,b,c,d,c
print(grades_)

#grades_ = (sum(grades[0]) / len(grades[0])), (sum(grades[1]) / len(grades[1])), (sum(grades[2]) / len(grades[2])), (sum(grades[3]) / len(grades[3])), (sum(grades[4]) / len(grades[4]))
#print(grades_) 

#grades_ = []
#for num in grades:
#    r = sum(num)/len(num)
#    grades_.append(r)
#my_dict4 = dict(zip(s, grades_))
#print(my_dict4)

# способ1
my_dict1 = {s[0]: a, s[1]: b, s[2]: c, s[3]: d, s[4]:h}
print(my_dict1)

# способ2
#my_dict2 = zip(s, grades_) #не выведится с помощью print, требуется распаковка
my_dict2 = dict(zip(s, grades_))
print(my_dict2)


