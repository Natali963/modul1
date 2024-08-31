my_dict = {'Vasya' : 1975, "Егор" : 1999, "Masha": 2002}
print(my_dict)
print(my_dict["Masha"]) #вывели значение по ключу
print(my_dict.get('Masha'))
print(my_dict.get('Маша', 'нет данных')) #None - если убрать ,'нет данных'
a = my_dict.pop('Егор')
print(a)
#del my_dict['Vasya']
#print(my_dict) 
my_dict.update({'Паша': 1985, 'Петр': 1986})
print(my_dict)

my_set = {1, 1, 2, 'Яблоко', 42.314, 15, 12, 2, 'Арельсин'}
print(my_set)
my_set1 = (5, 6, 1.6)
print(my_set1)
my_set.add(my_set1)
print(my_set)
#print(my_set.discard(15))
#print(my_set)
print(my_set.remove(12))
print(my_set)


