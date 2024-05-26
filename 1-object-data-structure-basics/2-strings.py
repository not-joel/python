# Strings

x = 'Hello'
print(x)

# String slicing
# [start:stop:step]

print(x[2:])
print(x[:4])
print(x[::2])
print(x[::-1]) # string reverse

# string properties

# concatenation
x = "Hello World"
x = x + " & Hello Python"
print(x)
x += " & Hello Python"
x += " & Hello Python"
print(x)
print(2+4)
print('2'+'4')
y = 'Joe'
print(y*4)

x = "hello world"
y = x.capitalize() # returns capitized string
print(y)
z = x.upper()
a = x.split()

# Strings are not mutable
x = 'hello'
x[1] = a # ❌