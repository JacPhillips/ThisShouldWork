list_animals = ["cat", "dog", "zebra"]

for ind, line in enumerate(open("snake.txt")):# enumerate over a piece of text
    print(ind, line, end="")

for position, animal in enumerate(list_animals, start=1): # enumerate over a list
    print (position, animal)