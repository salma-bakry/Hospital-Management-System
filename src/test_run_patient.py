from src.Patiant import Patiant
from src.Medical_record import Medical_record
from src.person import Person
##this must be added to the the rest of the functions of the hospital management system.

##this is the main file of the hospital management system. It allows users to add new patients, add records to their medical records, and view their medical records.

#add a new patient details and create a Patiant object
print("Enter patient details:")
Patiant_id=int(input("Enter patient ID: "))
name=input("Enter patient name: ")
age=int(input("Enter patient age: "))
department=input("Enter patient department: ")
patient = Patiant(Patiant_id, name, age, department)
print(f"Patient {patient.name} added successfully with ID {patient.Patiant_id} in department {patient.department}.")


#add a new record to the patient's medical record
print("Now you can add records to the patient's medical record.")
print("Enter record details:")
record_type=int(input("Enter record type (1 for diagnosis, 2 for medications, 3 for test results, 4 for appointments, 5 for medical history): "))
record=input("Enter record: ")
patient.add_record(record_type, record)
print("Record added successfully. Here is the patient's medical record:")


#view the patient's medical record
patient.view_record()

