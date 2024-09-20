#hospital management

#class patient 
#add patient id name
#delete patient id 
#display all patient
#display patient by id
#update patient patient by id

class Patient:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __str__(self):
        return(f'["{self.id}","{self.name}"]')
    def __repr__(self):
        return self.__str__
    
patients = []

def add_patient(id,name):
    patient = Patient(id,name)
    patients.append(patient)
    print('Patient created succesfully')

def remove_patient(id):
    #patient = Patient(id)
    for patient in patients:
        if patient.id == id:
            if(input('Are you sure you want to remove the patient?(yes/no)')).lower() == 'yes':
                patients.remove(patient)
                print('Patient removed succesfully!')
                return 
            return
    print('No such id')
    return

def display_patient():
    global patients
    for patient in patients:
        print(patient)

def display_patient_byId(id):
    #patient = Patient(id)
    for patient in patients:
        if patient.id == id:
            print(patient)
            return
    print('No such id')

def update_patient(id):
    #patient = Patient(id)
    for patient in patients:
        if patient.id == id:
            print(patient)
            if(input('Are you sure you want to update?(yes/no)')).lower() == 'yes':
                name = input('Enter new name:')
                patient.name = name
                print('name updated successfully!')
                return
    print('Invalid patient id')
    return

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



menus()
        

    

