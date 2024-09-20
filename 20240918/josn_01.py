import json
patients = [
    {'id':101,'name':'Dravid'},
    {'id':102,'name':'mahesh'},
    {'id':103,'name':'rohit'}
]
patients_str = json.dumps(patients)
print(patients_str)

with open('patients_data.json','w') as patients_db:
    json.dump(patients,patients_db)

patients_obj = json.loads(patients_str)
print(patients_obj)

with open('patients_data.json','r') as patients_db:
    patinet_list = json.load(patients_db)
    print(patinet_list,type(patinet_list))