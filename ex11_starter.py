#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# create hyphens string the length of Belgium string
hyphen_string = ''
for i in Belgium:
    hyphen_string +='-' # would join be better
print(hyphen_string)


# separate Belgium string with colons
Belgium = Belgium.replace(',', ":")
print(Belgium)

# population addition
belgium_string = Belgium.split(':')
pop_Belgium = int(belgium_string[1])
pop_Brussels = int(belgium_string[3])
population = str(pop_Belgium+pop_Brussels)
print(population)

# use join to create bigger Belgium string
belgium_list = [hyphen_string, Belgium, population]
Belgium = ':'.join(belgium_list)

print("The final string is : ")
print(Belgium)