from src.person import Person
from src.Medical_record import Medical_record

class Patiant(Person):
    '''This class represents a patient in the hospital system. It inherits from the Person class and adds additional attributes such as patient ID, department, and a medical record.    '''
    def __init__(self,Patiant_id:int, name:str, age:int, department:str):
        '''Initialize a Patiant object with the given patient ID, department, name, and age. It also initializes a Medical_record object for the patient.'''
        '''args:
            Patiant_id: The patient's unique identifier.
            department: The department the patient is associated with.
            name: The patient's name.
            age: The patient's age.
        '''
        super().__init__(name, age)
        self.Patiant_id=Patiant_id
        self.department=department
        self.medical_record=Medical_record()
    
    def view_record(self):
        '''View the patient's medical record by calling the view_record method of the Medical_record object.'''
        '''args:
            None
            returns:
            None
        '''
        self.medical_record.view_record()
    
    def add_record(self,record_type:int,record:str):
        '''Add a record to the patient's medical record by calling the add_record method of the Medical_record object.'''
        '''args:
            record_type: An integer representing the type of record (1 for diagnosis, 2 for medications, 3 for test results, 4 for appointments, 5 for medical history).
            record: The record to be added which is a string.
            returns:
            None
        '''
        self.medical_record.add_record(record_type,record)

        

        