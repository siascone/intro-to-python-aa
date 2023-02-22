import datetime

# Join
shopping_list = ['bread', 'milk', 'eggs']
print(', '.join(shopping_list))

# Comma as thousands separator
print('{:,}'.format(1234567890)) # => '1,234,567,890

# Date and Time
d = datetime.datetime(2020, 7, 4, 12, 15, 58)
print(d)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))

# Percentage
points = 190
total = 220
print('Correct ansewers: {:.3%}'.format(points/total))

# Data Table
width = 8
print(' decimal      hex   binary')
print('-'*27)
for num in range(1, 16):
    for base in 'dXb':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=" ")
    print()
    
