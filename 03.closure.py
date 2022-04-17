def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))

def make_repeater_of(n):
    def repeater(word):
        assert type(word) == str, "Solo puedes utilizar string"
        return word * n
    return repeater

repeat_5 = make_repeater_of(5)
print(repeat_5("Hola"))
print(repeat_5("Mauro"))
print(repeat_5("Platzi"))
