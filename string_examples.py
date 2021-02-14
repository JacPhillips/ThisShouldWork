# string methods
string_to_number = int('987')
print (string_to_number)

# find substring
my_find = ("I'm looking for a string or two")
print(my_find.find("or")) #finds position  of substring
print(my_find.find("wire")) # returns -1 as wire not in string ie false

# string tests
weather = ('Very cold and raining')
if weather.startswith('Ver'):
    print('Horrible weather')

print(weather.count('n')) # counts number of times element appears in string

# f-strings
name = 'Doris Johnson'
age = 12
person = (f'Name: {name}\n' f'Age: {age}\n')
print(person)

# capitalize
destination = ('Mexico')
print(destination.capitalize())

# uppercase
print(destination.upper())

# zfill
print(destination.zfill(29))

# slicing string
print(destination[3:5]) # prints index 4 to 5

# splitting a string
building =('bungalows are small, houses are big, hotels are bigger')
another = building.split(',')
print(type(another))

#joining a string with a separator
another[0] = 'converted offices not so good'
building = '99'.join(another)
print(type(building), building)