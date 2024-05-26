# DICTIONARY - Object

# object key should be string
my_dict = {
    'key1': 'value1',
    'key2': 'value2',
}

prices_lookup = {
    'apple': 2.99,
    'oranges': 1.99,
    'milk': 5.80
}

print(prices_lookup['apple'])

d = {
    'k1': 123,
    'k2': [0, 1, 2, 'a', 'b', 'c'],
    'k3': {
        'insideKey': 100
    }
}

print(d['k2'][-1].upper())
print(d['k3']['insideKey'])

new_dict = {
    'k1': 100,
    'k2': 200,
    'k3': 300
}

print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())

# checkout --> ordereddict