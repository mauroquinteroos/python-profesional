def decorator(func):
    def wrapper():
        func()
        print('Esto se añade a la función original')
    return wrapper

def greeting1():
    print('Hola 1!')

greeting1 = decorator(greeting1)
greeting1()

@decorator
def greeting2():
    print('Hola 2!')

greeting2()


def upper_words(func):
    def wrapper(word):
        return func(word).upper()
    return wrapper

@upper_words
def message(word):
    return f'{word} recibiste un mensaje'

print(message('Mauro'))
