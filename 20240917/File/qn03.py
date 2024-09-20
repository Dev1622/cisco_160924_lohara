int_list = []
# n = int(input('Enter the number of values:'))
n = input('Enter the number of values:')
""" for i in range(n):
    number = int(input('Enter the number:'))
    int_list.append(number) """
int_list = list(map(int, n.split()))

int_set = set(int_list)
int_fset = frozenset(int_set)
int_dict = {num:num*num for num in int_fset} #Dictionary Comprehension
print(f'Original set {int_list}')
print(f'Set (no duplicates) {int_set}')
print(f'Frozen set {int_fset}')
print(f'Dictionary {int_dict}')

import json

with open('qn03.json','w') as int_db:
    json.dump(int_dict,int_db)
print('Dictionary written to JSON file.')

with open('qn03.json','r') as int_db:
    int_dict2 = json.load(int_db)
    print(f'Reading from json file...\n{int_dict2}')