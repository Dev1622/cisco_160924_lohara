names_list = input('Enter the student names(seperated by spaces):').split()
names_set = set(names_list)
names_fset = frozenset(names_set)
names_dict = {name:len(name) for name in names_fset} #Dictionary Comprehension
print(f'Original set {names_list}')
print(f'Set (no duplicates) {names_set}')
print(f'Frozen set {names_fset}')
print(f'Dictionary {names_dict}')

import json

""" with open('qn02.json','w') as names_db:
    json.dump(names_dict,names_db)
print('Dictionary written to JSON file.')

with open('qn02.json','r') as names_db:
    names_dict2 = json.load(names_db)
    print(f'Reading from json file...\n{names_dict2}') """

with open('qn02.json','w') as names_db:
    json.dump(names_dict,names_db)
print('Dictionary written to JSON file.')

with open('qn02.json','r') as names_db:
    names_dict2 = json.load(names_db)
    print(f'Reading from json file...\n{names_dict2}')