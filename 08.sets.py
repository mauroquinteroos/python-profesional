my_set1 = {3, 4, 5}
print(my_set1)

my_set2 = {'Hello', 23.3, False, True}
print(my_set2)

my_set4 = {3, 3, True, True, 7}
print(my_set4)

# my_set5 = {[1, 2, 3], 4, 'World'}
# print(my_set5)

empty_set = {}
print(type(empty_set))

empty_set = set()
print(type(empty_set))

my_list = [1, 2, 3, 4, 5, 6, 7]
my_set5 = set(my_list)
print(my_set5)

my_tuple = (1, 1, 'Hello', 'Hello', 5, 6, 7)
my_set6 = set(my_tuple)
print(my_set6)

my_set = {1, 2, 3}

# Añadir elementos
my_set.add(4)
my_set.update([1, 2, 5])
my_set.update((1, 7, 2), {6, 8})
print(my_set)

# Eliminar elementos
my_set.discard(5)
my_set.remove(4)
my_set.discard(24)
print(my_set)
# my_set.remove(False) Eleva una excepción si el elemento no existe

# Borrar un elemento aleatorio
my_set.pop()
print(my_set)

# Borrar todos los elementos
my_set.clear()
print(my_set)


set1 = {3, 4, 5}
set2 = {5, 6, 7}

set3 = set1 | set2
print(set3)

set3 = set1 & set2
print(set3)

set3 = set1 - set2
print(set3)

set3 = set2 - set1
print(set3)

set3 = set1 ^ set2
print(set3)


def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

random_list = [1, 1, 2, 2, 4]
print(remove_duplicates(random_list))
print(list(set(random_list)))