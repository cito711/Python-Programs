import random
import sys
import os

'''  This is a 
multi-line comment
'''

# This is a single line comment

pi_tuple = (3,1,4,1,5,9)

new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

print(new_tuple)

super_villains = {'Riddler' : 'Edward Nigma',
                  'Penguin' : 'Oswald Cobblepot',
                  'Joker' : 'Unknown',
                  'Poison Ivy' : 'Pam Isley',
                  'Catwoman' : 'Selina Kyle',
                  'Hush' : 'Tommy Elliot'}

print(super_villains['Riddler'])

del super_villains['Hush']

super_villains['Poison Ivy'] = 'Pamela Isley'

print(len(super_villains))

print(super_villains.get("Penguin"))

print(super_villains.keys())

print(super_villains.values())


