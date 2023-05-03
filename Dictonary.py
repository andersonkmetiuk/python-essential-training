animals = {
    'a': 'aardvark',
    'b': 'bear',
    'c': 'cat',
}

print(animals)
print(animals['a'])

animals['d']='dog'
print(animals)

animals['a']='antilope'
print(animals)

print(animals.keys())
print(animals.values())

print(animals.get('e')) #se nao existe retorna None