import csv

file_name = "C:/Users/ivank/Desktop/Ivan/DS učenje/Phase1/week04/patients.csv"

patients = []
with open(file_name, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        patients.append(row)

def get_patient_summary(patients):    
    for row in patients:
        print(str(row["name"]) + " (age " + str(row["age"]) + "): " + "anxiety score " + str(row["anxiety_score"]))
        
get_patient_summary(patients)

           
def get_severe_patients(patients):
    for row in patients:
        if int(row["anxiety_score"]) >=15:
            print(str(row["name"]))

print("Patient with extreme anxiety symptoms:")
get_severe_patients(patients)
    
print(patients)
       




