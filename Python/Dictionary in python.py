d = {'a': 1, 'b': 2, 'c': 3}

print(d.clear())

d = {'a': 1, 'b': 2, 'c': 3}
d_copy = d.copy()
print(d_copy)

print(d.fromkeys(['x', 'y'], 0))

print(d.get('a'))
print(d.get('z'))

print(d.items())

print(d.keys())

print(d.pop('b'))
print(d)

print(d.popitem())
print(d)

d = {'a': 1}
d.setdefault('b', 2)
print(d)
d.setdefault('a', 100)
print(d)

d.update({'c': 3, 'd': 4})
print(d)

print(d.values())
