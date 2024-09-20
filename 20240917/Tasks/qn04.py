#class patient

class Patient:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __str__(self):
        return(f'[id={self.id},name={self.name}]')
    def __repr__(self):
        return self.__str__
    def to_dict(self):
        return{'id' : self.id,'name' : self.name}



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

def menu():
    choice = int(input('''1.add patient
2.remove patient 
3.display patient
4.End
Enter your choice:'''))
    if(choice == 1):
        id = int(input('Enter the patient id:'))
        name = input('Enter the patinet name:')
        add_patient(id,name)
        
    elif(choice == 2):
        id = int(input('Enter the patient id:'))
        remove_patient(id)

    elif(choice == 3):
        for patient in patients:
            print(patient)
    
    return choice

def menus():
    choice = menu()
    while(choice != 4):
        choice = menu()
    
    print("The App is ended")
    
    import json
    patients_list = [patient.to_dict() for patient in patients]
    
    with open('patients.json', 'w') as patients_db:
        json.dump(patients_list, patients_db)
        print("Data written to JSON file successfully!")
    return


menus()

