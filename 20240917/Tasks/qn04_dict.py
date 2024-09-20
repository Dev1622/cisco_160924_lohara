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
        return {'id': self.id, 'name': self.name}



patients = {}

def add_patient(id,name):
    patient = Patient(id,name)
    patients[patient.id] = patient
    print('Patient created succesfully')

def remove_patient(id):
    #patient = Patient(id)
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return
    print(patient)
    if input('Are you sure to delete(yes/no)?').lower() == 'yes':
        del patients[id] #patients.remove(patient)
        print('Patient deleted successfully!')
        return

def display_patient():
    for id in patients:
        print(patients[id])

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
        display_patient()
    
    return choice

def menus():
    choice = menu()
    while(choice != 4):
        choice = menu()
    
    print("The App is ended")
    
    import json

    #patients_dict = {id:patient.to_dict() for id, patient in patients.items()}
    patients_dict = {patient.to_dict() for patient in patients.items()}
    with open('patients_dict.json','w') as patients_db:
        json.dump(patients_dict,patients_db)
        print("Data written to json file successfully!")
    return


menus()
