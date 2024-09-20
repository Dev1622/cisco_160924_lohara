""" with open('names.txt','r') as names_db:
    all_names = names_db.read()
    print(all_names) 
 """

# using with read lines
""" with open('names.txt','r') as names_db:
    all_names = names_db.readLine()
    print(all_names) """

#pickle
data = {'name' : 'John','age':30,'city':'New york'}
import pickle
with open('names.pickle','wb') as file:
    pickle.dump(data,file)

with open('names.pickle','rb') as file:
    Temp=pickle.load(file)
print(Temp)