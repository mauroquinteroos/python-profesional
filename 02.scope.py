x = 5

def my_func():
    x = 3
    def my_other_func():
        x = 2
        print('Local: ', x)
        print('Local variables: ', locals())

    my_other_func()
    print('Enclosing: ', x)

my_func()
print('Global: ', x)
print('Global variables: ', globals())
print('------------------------------------------')


def my_func_global():
    global x
    x = 10
    print('Global keyword: ', x)

my_func_global()
print('Global: ', x)
print('------------------------------------------')
