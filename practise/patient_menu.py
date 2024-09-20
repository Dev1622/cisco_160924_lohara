from patient_service import add_patient,remove_patient,display_patient,display_patient_byId,update_patient

def menu():
    choice = int(input('''1.add patient
2.remove patient 
3.display all patient
4.display patient by id
5.update patient by id
6.End
Enter your choice:'''))
    if(choice == 1):
        id = int(input('Enter the patient id:'))
        name = input('Enter the patinet name:')
        add_patient(id,name)
        
    elif(choice == 2):
        id = int(input('Enter the patient id:'))
        remove_patient(id)
            
    elif(choice == 3):
        display_patient()
            
    elif(choice == 4):
        id = int(input('Enter patient id:'))
        display_patient_byId(id)
            
    elif(choice == 5):
        id = int(input('Enter patient id:'))
        update_patient(id)
    elif(choice == 6):
        pass
    else:
        print('Invalid menu')

    return choice

def menus():
    choice = menu()
    while(choice != 6):
        choice = menu()
    
    print("The App is ended")
    return