my_dict={'Tanya':1989, 'Olya':1996, 'Sasha':2012}
print(my_dict)
print(my_dict['Tanya'])
print(my_dict.get('Andrey'))
my_dict.update({'Andrey':1995,
                'Natasha':1886})
a=my_dict.pop('Tanya')
print(a)
print(my_dict)
my_set={1,2,3,4,1,2,5}
print((my_set))
my_set.update([17, 'Слово'])
print(my_set.remove('Слово'))
print(my_set)