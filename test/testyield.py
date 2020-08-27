def provider():
    for i in range(5):
        yield i

p = provider()
print(next(p))
print(next(p))
print(next(p))
 