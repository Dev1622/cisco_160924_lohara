from Patient import Patient
#2. patients{}
patients = {} #dict()

#3. patient_add(id, name)
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients[patient.id] = patient #patients.append(patient)
    print('patient created successfully')
#4. patient_remove(id)
def patient_remove(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id {id}')
        return
    print(patient)
    if input('Are you sure to delete(yes/no)?').lower() == 'yes':
        del patients[id] #patients.remove(patient)
        print('Patient deleted successfully!')
        return 
        #end if 
    #end for 
# display patient by id
def display_id(id):
    global patients
    patient = patients.get(id)
    if patient == None:
        print(f'No such id{id}')
    print(patient)
# update patient by id
def patient_update(id):   #(id,name):
    global patients
    patient = patients.get(id)                          #for patient in patients:
    if patient == None:
        print(f'No such patient')
        return
    print(patient)
    if input(('Are you sure to update the patient?(yes/no):')).lower() == 'yes':
        name = input(f'Enter new name({patient.name}):')
        patient.name = name
        print('patient details updated succesfully!')
    return

#5. patient_display()
def patient_display():
    global patients
    for id in patients: # for patient in patients
        print(patients[id])