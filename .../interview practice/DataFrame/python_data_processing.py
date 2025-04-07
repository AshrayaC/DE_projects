import json 

def calculate_total_billed(json_file):

    with open(json_file, "r") as file:
        data = json.load(file)
    
    total_billed_per_patient = {}

    print(data)
    for patient in data:
        patient_id = patient["patient_id"]
        total_billed = sum(visit["amount_billed"] for visit in patient["visits"])
        print(f'Total Billed : {total_billed}')
        total_billed_per_patient[patient_id] = total_billed
        print(total_billed_per_patient)
    
    return total_billed_per_patient

json_file = "test_data.json"
print(calculate_total_billed(json_file))