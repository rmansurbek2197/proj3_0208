#11
books = ['Novel', 'Poetry', 'Science', 'Fiction']
books.append('History')
books.remove('Poetry')
books.insert(books.index('Science'), 'Math')
books.sort()
print(books)

#12
scores = [85, 90, 78]
scores.extend([92, 88, 95])
scores.remove(78)
scores.sort()
scores.pop(0)
print(scores)

#13
cities = ['Paris', 'London', 'Berlin', 'Madrid']
cities.insert(0, 'Rome')
print(cities.index('Berlin'))
cities.remove('Madrid')
cities_copy = cities.copy()
print(cities_copy)

#14
animals = ['lion', 'tiger', 'bear', 'tiger', 'wolf', 'tiger']
print(animals.count('tiger'))
animals_copy = animals.copy()
animals.remove('bear')
animals_copy.remove('wolf')
print(animals)
print(animals_copy)

#15
products = ['shirt', 'pants', 'jacket', 'shoes']
print(products.index('jacket'))
products.remove('shoes')
products.extend(['hat', 'belt'])
print(products)
products.clear()
print(products)
