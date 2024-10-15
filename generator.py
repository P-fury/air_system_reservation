def magic():
    yield 1
    yield 2
    yield 3


x = magic()
print(type(x))
print(next(x))
print(next(x))
print(next(x))
