from datetime import datetime


def execution_time(func):
    # positional arguments (args): * es el operador de packing y unpacking que usan
    # keyword arguments (kwargs): ** es el operador de packing y unpacking que usan
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)

        final_time = datetime.now()
        time_elapsed = (final_time - initial_time).total_seconds()
        print(f'Tiempo que se demoro en ejecutar: {format(float(time_elapsed),"f")}')
    return wrapper

@execution_time
def render_func():
    result = [index for index in range(1, 1000000)]
    print(f'Lenght: {len(result)}')
render_func()

@execution_time
def sum_numbers(a: int, b: int) -> int:
    return a+b
values = [5, 5]
sum_numbers(*values)

@execution_time
def greetings(name='Mauro'):
    print(f'Hello {name}')
greetings(name='Pedro')


# La estructura de un decorador que tiene parámetros
def with_custom_message(message):
    def with_message(fuction):
        print(f'{message}: ')
        def wrapper(*args, **kwargs):
            fuction(*args, **kwargs)
        return wrapper
    return with_message

@with_custom_message('Hello')
def multiply(a, b):
    c = a * b
    print(f'The result is {c}')

multiply(10, 2)

# Sería como hacer:
decorator = with_custom_message('Hello')
wrapper_decorator = decorator(multiply)
wrapper_decorator(10, 2)