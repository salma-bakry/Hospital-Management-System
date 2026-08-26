import json 
import os # helps us check if the file exists


# from hospital import Hospital
# from department import Department
# from patient import Patient
# from staff import Staff


# __file__ : the location of this current Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # the path of src folder 
data_file = os.path.join(BASE_DIR, "..", "data", "hospitals.json") # builds the path to the json file



def load_hospitals(): 
    if not os.path.exists(data_file): 
        return []

    with open(data_file, "r") as file:
        hospitals = json.load(file)

    return hospitals


def save_hospitals(hospitals):
    with open(data_file, "w") as file:
        json.dump(hospitals, file, indent=4)


# obj -> dic (3lshan n save)
def patient_to_dict(patient):

    return {
        "name": patient.name,
        "age": patient.age,
        "medical_record": patient.medical_record
    }


def staff_to_dict(staff_member):

    return {
        "name": staff_member.name,
        "age": staff_member.age,
        "position": staff_member.position
    }


def department_to_dict(department):

    patient_list = []

    for patient in department.patients:
        converted_patient = patient_to_dict(patient)
        patient_list.append(converted_patient)


    staff_list = []

    for staff_member in department.staff:
        converted_staff = staff_to_dict(staff_member)
        staff_list.append(converted_staff)


    return {
        "name": department.name,
        "patients": patient_list,
        "staff": staff_list
    }


def hospital_to_dict(hospital):

    department_list = []

    for department in hospital.departments:
        converted_department = department_to_dict(department)
        department_list.append(converted_department)

    return {
        "name": hospital.name,
        "location": hospital.location,
        "departments": department_list
    }



# dic -> obj 
def dict_to_patient(patient_data):
    patient = Patient(patient_data["name"] , patient_data["age"] , patient_data["medical_record"])
    return patient


def dict_to_staff(staff_data):
    staff_member = Staff(staff_data["name"] , staff_data["age"] , staff_data["position"])
    return staff_member


def dict_to_department(department_data):
    department = Department(department_data["name"])

    for patient_data in department_data["patients"]:
        patient = dict_to_patient(patient_data)
        department.add_patient(patient)

    for staff_data in department_data["staff"]:
        staff_member = dict_to_staff(staff_data)
        department.add_staff(staff_member)

    return department


def dict_to_hospital(hospital_data):
    hospital = Hospital(hospital_data["name"] , hospital_data["location"])

    for department_data in hospital_data["departments"]:
        department = dict_to_department(department_data)
        hospital.add_department(department)

    return hospital


def find_hospital(name , location):
    hospitals = load_hospitals()

    for hospital_data in hospitals:
        if ((hospital_data["name"].lower() == name.lower()) 
            and (hospital_data["location"].lowe() == location.lower())):

            return dict_to_hospital(hospital_data)

    return None 


def save_current_hospital(hospital):
    hospitals = load_hospitals()
    hospital_dict= hospital_to_dict(hospital)

    found = False

    for h in hospitals:
        if ((h["name"].lower() == hospital.name.lower()) 
           and (h["location"].lower() == hospital.location.lower())):

            h.clear()
            h.update(hospital_dict)
            found = True
            break

    if not found:
        hospitals.append(hospital_dict)

    save_hospitals(hospitals)
