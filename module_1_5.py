immutable_var = (1,2,'a','b')
print(immutable_var)
print(type(immutable_var))
print('Immutable tuple: ', immutable_var)

immutable_var_ = tuple([1,2,'a','b'])
print(immutable_var_)
print(type(immutable_var_))

#immutable_var[0] = 10
# TypeError: 'tuple' object does not support item assignment
# !особенность кортэжа - он сам неизменяемый, упорядоченный, но внутри кортэжа могут быть изменяемые объекты

mutable_list = [1, 2, 'a', 'b', 'Modified']
print(mutable_list)
mutable_list[2] = 'hello'
mutable_list[3] = input('напиши имя')
print(mutable_list)