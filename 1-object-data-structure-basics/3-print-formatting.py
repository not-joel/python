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

# f string
name = "Joel"
print(f"My name is {name}")

# placeholders
print("I'm going to inject %s here." %'something')
print("I'm going to inject %s text here and %s text here" %('something', 'more'))

x = 'some'
y = 'more'
print("I'm going to inject %s text here and %s text here" %(x, y))