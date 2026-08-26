# from hospital import Hospital
# from department import Department
# from patient import Patient
# from staff import Staff
from data_manager import find_hospital, save_current_hospital

def first_menu():

    print("\nWelcome to the Hospital Management System")

    print("1. Open Existing Hospital")
    print("2. Create New Hospital")
    print("3. Exit")

    choice = input("Enter your choice: ")


first_menu()