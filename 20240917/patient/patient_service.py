from Patient import Patient
#2. patients[]
patients = []

#3. patient_add(id, name)
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients.append(patient)
    print('patient created successfully')
#4. patient_remove(id)
def patient_remove(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            if input('Are you sure to delete(yes/no)?').lower() == 'yes':
                patients.remove(patient)
                print('Patient deleted successfully!')
            return 
        #end if 
    #end for 
    print(f'No such id {id}')
# display patient by id
def display_id(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
# update patient by id
def patient_update(id,name):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            if ('Are you sure to update the patient?(yes/no):').lower == 'yes':
                patient.name = name
                print('patient details updated succesfully!')
                return

#5. patient_display()
def patient_display():
    global patients
    for patient in patients:
        print(patient)