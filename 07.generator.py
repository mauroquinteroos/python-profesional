import time


def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            counter += 1
            aux = n1 + n2
            n1, n2 = n2, aux
            yield aux


# Generator Expression
my_list = [1,2,3,4,5,6,7]
my_second_list = [x ** 2 for x in my_list] # list comprehension
my_gen = (x ** 2 for x in my_list) # generator expression

print("Lista: ", my_second_list)
print("Generador: ", my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print("------------------------------------------------")

fibonacci = fibo_gen()
for element in fibonacci:
    print(element)
    time.sleep(0.5)
