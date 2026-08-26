from patient import Patient
from staff import Staff

class Department:
    """Class representing a department in the hospital."""
    def __init__(self, name: str, capacity: int = 5):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.staff = []


    def add_patient(self, patient):
        """Add a patient to the department."""
        if len(self.patients) >= self.capacity:
            print(f"Cannot add {patient.name}. Department {self.name} is full!")
            return False
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")
        return True

    
    def remove_patient(self, patient_name: str):
        """Remove a patient from the department."""
        for patient in self.patients:
            if patient.name.lower() == patient_name.lower():
                self.patients.remove(patient)
                print(f"Patient '{patient_name}' discharged from {self.name}.")
                return True
        print(f"Patient '{patient_name}' not found in {self.name}.")
        return False

    
    def add_staff(self, staff_member):
        """Add staff member to the department."""
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")


    def get_occupancy_rate(self) -> float:
        """Calculate occupancy percentage."""
        return (len(self.patients) / self.capacity) * 100


    def display_department_details(self):
        """Display department details and lists."""
        print(f"Department Name: {self.name}")
        print(f"Beds Occupancy: {len(self.patients)}/{self.capacity} ({self.get_occupancy_rate():.1f}%)")
        print("Staff Members:")
        if not self.staff:
            print("  - No staff members assigned.")
        else:
            for staff_member in self.staff:
                print(f"  - {staff_member.view_info()}")
        print("Patients List:")
        if not self.patients:
            print("  - No patients admitted.")
        else:
            for patient in self.patients:
                print(f"  - {patient.view_record()}")
