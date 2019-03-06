colors = {'Red', 'Green', 'Blue'}
print(colors)
print('Red' in colors)
colors.add('Yellow')
print(colors)
colors.remove('Red')
print(colors)

colors.clear()
print(colors)
print(dir(colors))
del colors