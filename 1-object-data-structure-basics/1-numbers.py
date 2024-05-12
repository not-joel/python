# x = 1 + 1 # add
# x = 7 - 4 # subtract
# x = 7 * 4 # multiply
# x = 7 / 4 # divide
# x = 7 % 4 # modulo / mod
# x = 2 ** 4 # power
# x = (2 + 10) * (10 + 3) # BODMAS
# x = 0.1 + 0.2 - 0.3


# Strings

# x = 'Hello'
# print(x)

# String slicing
# [start:stop:step]

# print(x[2:])
# print(x[:4])
# print(x[::2])

# string properties

# concatenation
# x = "Hello World"
# x = x + " & Hello Python"
# print(x)
# x += " & Hello Python"
# x += " & Hello Python"
# print(x)
# print(2+4)
# print('2'+'4')
# y = 'Joe'
# print(y*4)

# x = "hello world"
# y = x.capitalize() # returns capitized string
# print(y)
# z = x.upper()
# a = x.split()

# Strings are not mutable
# x = 'hello'
# x[1] = a # ❌

# Print formatting with Strings
# .format()

print('this is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
# using keywords
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 48/92
print('The result is {r}'.format(r=result))
# Float formatting follows "{value:width.precision f}"
print('The result is {r:10.3f}'.format(r=result))