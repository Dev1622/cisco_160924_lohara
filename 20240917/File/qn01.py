fruit_list = input('Enter the fruits name (space seperated):').split()
fruit_tuple = tuple(fruit_list)

print(f'list : {fruit_list}')
print(f'tuple : {fruit_tuple}')

with open('fruits.txt','w') as fruits_db:
    fruits_db.write(f'{fruit_list}\n')
    fruits_db.write(f'{fruit_tuple}\n')
print('Data written into the file')
with open('fruits.txt','r') as fruits_db:
    fruits_list = fruits_db.readline()
    fruits_tuple = fruits_db.readline()
    print('Rading data from the file')
    
print(fruit_list)
print(fruit_tuple)


    
