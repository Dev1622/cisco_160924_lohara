salaries = []

#1.add salary
#2.remove salary
#3.find sum of salary
#4. find avg of salary
#5. find min of salaries
#6. find max of salaries
def salary_add(salary):
    global salaries
    salaries.append(salary)
   # return salaries.append(salary)
def salary_delete(salary):
    global salaries
    try:
        salaries.remove(salary)
    except ValueError as err:
        print('No such salary')
   # return salaries.remove(salary)
def salary_sum():
    return sum(salaries)
def salary_avg():
    global salaries
    s = sum(salaries)
    count = len(salaries)
    avg =  s / count
    return avg
    #return s / count
def salary_max():
    return max(salaries)
def salary_min():
    return min(salaries)


def menu():
    choice = int(input('''1-add
                   2-delete
                   3-sum
                   4-avg
                   5-min
                   6-max
                   7-end
                   your choice :
    '''))
    if choice == 1:
        salary = float(input('Enter salary:'))
        salary_add(salary)
        print(salaries)

    elif choice == 2:
        salary = float(input('Enter salary:'))
        salary_delete(salary)
        print(salaries)
    elif choice == 3:
        s = salary_sum()
        print(s)
    elif choice == 4:
        avg = salary_avg()
        print(avg)
    elif choice == 5:
        min = salary_min
        print(min)
    elif choice == 6:
        max = salary_max
        print(max)
    return choice

def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('App Ended') 

menus()       
            
