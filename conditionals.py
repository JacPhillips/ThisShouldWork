# simple conditional
from typing import List, Any

lista = []
listb = []

if lista == listb:
    print("The same")

lista = listb # assign lista to listb
lista.append('dog')
print(lista, listb)  # prints same value

if lista == listb:
    print("The same")
else:
    print("not the same")
if "dog" in lista:
    print("woof")



# indentation incorrect - error message IndentationError
# if lista == listb:
# print("The same")

# use of built in any and all
listnoise = [2, ""]
if not all(listnoise):
    print(bool(listnoise[1]))# prints false as there is an empty string

if any(listnoise):
    print ("This is true", bool(listnoise[0]))# prints This is true True as value first element is true

# exception handling example - comparison string and integer
cat_lives = 8
try:
    if cat_lives < "9":
        print ('Wow!')
    else:
        print ('Doh!')
except TypeError:
        print("Invalid types compared")

# While loops
too_hot = ["socks", "hat", "scarf", "hoody"]
while too_hot:
    print(too_hot.pop())
    pass
print("Cooled down")

