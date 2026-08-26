from hospital import Hospital
from department import Department
from patient import Patient
from staff import Staff

from data_manager import find_hospital, save_current_hospital


def department_menu(hospital):

    while True:

        print("\n" + "=" * 50)
        print("DEPARTMENT MANAGEMENT".center(50))
        print("=" * 50)

        print(f"\nHospital: {hospital.name}")

        print("\n[1] Add Department")
        print("[2] View Departments")
        print("[3] Remove Department")
        print("[4] Back")

        print("\n" + "-" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":

            name = input("\nEnter department name: ")

            capacity_input = input("Enter department capacity: ")

            if not capacity_input.isdigit():
                print("\nPlease enter a valid number.")
                continue

            capacity = int(capacity_input)

            if capacity <=0:
                print("\nCapacity must be greater than 0.")
                continue

            department = Department(name, capacity)

            hospital.add_department(department)

            print(f"\nDepartment '{name}' added successfully.")

            save_current_hospital(hospital)

        elif choice == "2":

            if len(hospital.departments) == 0:

                print("\nNo departments have been added yet.")

            else:

                print("\n" + "-" * 50)
                print("DEPARTMENTS".center(50))
                print("-" * 50)

                for d in hospital.departments:
                    d.display_department_details()

        elif choice == "3":
            department_name = input("\nEnter department name to remove: ")
            department = hospital.find_department(department_name)

            if department is None:
                print(f"\nDepartment '{department_name}' not found.")
            else:
                hospital.remove_department(department)
                save_current_hospital(hospital)


        elif choice == "4":

            break

        else:

            print("\nInvalid choice. Please try again.")



def patient_menu(hospital):

    # A hospital must have at least one department
    # before patients can be managed.
    if len(hospital.departments) == 0:

        print("\n" + "=" * 50)
        print("WARNING".center(50))
        print("=" * 50)
        print("\nYou must create a department before adding patients.")

        input("\nPress Enter to return...")
        return

    while True:

        print("\n" + "=" * 50)
        print("PATIENT MANAGEMENT".center(50))
        print("=" * 50)

        print(f"\nHospital: {hospital.name}")

        print("\n[1] Add Patient")
        print("[2] View Patients")
        print("[3] Remove Patient")
        print("[4] Back")

        print("\n" + "-" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\n" + "-" * 50)
            print("ADD PATIENT".center(50))
            print("-" * 50)

            name = input("\nEnter patient name: ")
            patient_id = int(input("Enter patient ID: "))
            age = int(input("Enter patient age: "))
            department_name = input("Ener patient department: ")

            selected_department = hospital.find_department(department_name)

            # Department does not exist
            if selected_department is None:

                print("\nDepartment not found.")
                continue


            patient = Patient(patient_id, name, age, selected_department.name)
            added = selected_department.add_patient(patient)

            if added:
                print("Enter record details:")

                record_type = int(input("Enter record type (1 for diagnosis, 2 for medications, 3 for test results, 4 for appointments, 5 for medical history): "))
                record = input("Enter record: ")
                patient.add_record(record_type, record)
                
                save_current_hospital(hospital)

                print(
                    f"Patient '{patient.name}' added successfully "
                    f"with ID {patient.patient_id}. "
                    f"in department {patient.department}."
                )



        elif choice == "2":
            print("\n" + "-" * 50)
            print("PATIENTS".center(50))
            print("-" * 50)

            found_patient = False

            for department in hospital.departments:

                if len(department.patients) > 0:

                    print(f"\nDepartment: {department.name}")

                    for patient in department.patients:

                        print(f"\nID: {patient.patient_id}")
                        print(f"Name: {patient.name}")
                        print(f"Age: {patient.age}")
                        print(f"Department: {patient.department}")
                        print(f"Medical Record:")
                        patient.view_record()

                        print("-" * 30)

                        found_patient = True

                if not found_patient:
                    print("\nNo patients have been added yet.")

        elif choice == "3":
            patient_name = input("\nEnter patient name to remove: ")

            found_removed_patient = False
            for department in hospital.departments:
                for patient in department.patients:
                    if patient.name.lower() == patient_name.lower():
                        department.remove_patient(patient_name)
                        save_current_hospital(hospital)
                        found_removed_patient = True
                        break
                if found_removed_patient:
                    break

            if not found_removed_patient:
                print(f"\nPatient '{patient_name}' was not found.")
            

        elif choice == "4":
            break

        else:
            print("\nInvalid choice. Please try again.")



def staff_menu(hospital):

    # A hospital must have at least one department
    # before staff can be added.
    if len(hospital.departments) == 0:

        print("\n" + "=" * 50)
        print("WARNING".center(50))
        print("=" * 50)

        print("\nYou must create a department before adding staff.")

        input("\nPress Enter to return...")
        return

    while True:

        print("\n" + "=" * 50)
        print("STAFF MANAGEMENT".center(50))
        print("=" * 50)

        print(f"\nHospital: {hospital.name}")

        print("\n[1] Add Staff")
        print("[2] View Staff")
        print("[3] Back")

        print("\n" + "-" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\n" + "-" * 50)
            print("ADD STAFF MEMBER".center(50))
            print("-" * 50)

            name = input("\nEnter staff name: ")

            age = int(input("Enter staff age: "))

            position = input("Enter staff position: ")

            department_name = input("Enter staff department: ")

            # Find the department
            selected_department = hospital.find_department(department_name)

            if selected_department is None:

                print("\nDepartment not found.")
                continue

            staff_member = Staff(name, age, position, selected_department.name)

            selected_department.add_staff(staff_member)

            save_current_hospital(hospital)

            print(
                f"Staff member '{staff_member.name}' "
                f"added successfully."
            )


        elif choice == "2":

            print("\n" + "-" * 50)
            print("STAFF MEMBERS".center(50))
            print("-" * 50)

            found_staff = False

            for department in hospital.departments:

                if len(department.staff) > 0:

                    print(f"\nDepartment: {department.name}")

                    for staff_member in department.staff:

                        print(f"\nName: {staff_member.name}")
                        print(f"Age: {staff_member.age}")
                        print(f"Position: {staff_member.position}")
                        print(f"Department: {staff_member.department}")

                        print("-" * 30)

                        found_staff = True

            if not found_staff:

                print("\nNo staff members have been added yet.")

        elif choice == "3":
            break

        else:
            print("\nInvalid choice. Please try again.")


def management_menu(hospital):

    while True:

        print("\n" + "=" * 50)
        print(f"{hospital.name.upper()} MANAGEMENT SYSTEM".center(50))
        print("=" * 50)

        print("\n[1] View Hospital Information")
        print("[2] Department Management")
        print("[3] Patient Management")
        print("[4] Staff Management")
        print("[5] Save and Exit")

        print("\n" + "-" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nHospital Name:", hospital.name)
            print("Location:", hospital.location)
            print("Number of Departments:", len(hospital.departments))

        elif choice == "2":

            department_menu(hospital)

        elif choice == "3":
            patient_menu(hospital)

        elif choice == "4":
            staff_menu(hospital)

        elif choice == "5":
            save_current_hospital(hospital)

            print("\nHospital data saved successfully.")
            print("Returning to main menu...")

            break

        else:
            print("\nInvalid choice. Please try again.")


def first_menu():

    print("\n" + "=" * 50)
    print("HOSPITAL MANAGEMENT SYSTEM".center(50))
    print("=" * 50)

    print("\n[1] Open Existing Hospital")
    print("[2] Create New Hospital")
    print("[3] Exit")

    print("\n" + "-" * 50)

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("\nEnter hospital name: ")
        location = input("Enter hospital location: ")

        hospital = find_hospital(name, location)

        if hospital is not None:
            print("\nHospital found successfully!")
            print(f"Welcome to {hospital.name} Hospital")

            management_menu(hospital)

        else:
            print("\nHospital not found.")
            first_menu()


    elif choice == "2":
        name = input("\nEnter hospital name: ")
        location = input("Enter hospital location: ")

        hospital = Hospital(name, location)

        save_current_hospital(hospital)

        print("\nHospital created successfully!")
        print(f"Welcome to {hospital.name} Hospital")

        management_menu(hospital)
    
    elif choice == "3":
        print("\nThank you for using the Hospital Management System!")

    else:

        print("\nInvalid choice.")
        first_menu()



first_menu()