patients = []

#1.add patient
#2.remove patient

def patient_add(patient):
    #global salaries
    patients.append(patient)
   # return salaries.append(salary)
def patient_delete(patient):
    #global salaries
    try:
        patients.remove(patient)
    except ValueError as err:
        print('No such patient')
   # return salaries.remove(salary)


def menu():
    choice = int(input('''1-add_patient
     2-delete_patient
     3-End
                   
    '''))
    if choice == 1:
        patient = str(input('Enter patient_name:'))
        patient_add(patient)
        print(patients)

    elif choice == 2:
        patient = str(input('Enter patient_no:'))
        patient_delete(patient)
        print(patients)
    return choice

def menus():
    choice = menu()
    while choice != 3:
        choice = menu()
    print('App Ended') 

menus() 