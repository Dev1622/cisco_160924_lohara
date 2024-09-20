from Patient import Patient

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