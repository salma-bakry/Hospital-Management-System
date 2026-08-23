class Hospital:
    """Class for managing hospital operations."""
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []  # List to hold departments

    def add_department(self, department):
        """Add a department to the hospital."""
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")
        
    def view_info(self):
        return f"Hospital Name: {self.name}, Location: {self.location}"    
    
    def remove_department(self, department):
        """Remove a department from the hospital."""
        if department in self.departments:
            self.departments.remove(department)
            print(f"Department '{department.name}' removed from {self.name}.")
        else:
            print("Department not found.")
            
    def find_department(self, name):
        """Find a department by name."""
        for department in self.departments:
            if department.name.lower() == name.lower():
                return department

        return None        