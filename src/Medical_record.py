class Medical_record():
    '''This class represents a medical record for a patient. It contains various types of records such as diagnosis, medications, test results, appointments, and medical history.    '''
    def __init__(self):
        '''Initialize a Medical_record object with empty lists for each type of record.'''
        self.diagnosis=[]
        self.medications=[]
        self.test_results=[]
        self.appointments=[]
        self.medical_history=[]
    def add_record(self,record_type:int,record:str):
        '''Add a record to the appropriate list based on the record type(number for each record type).'''
        '''args:
            record_type: An integer representing the type of record (1 for diagnosis, 2 for medications, 3 for test results, 4 for appointments, 5 for medical history).
            record: The record to be added which is a string.
            returns:
            None
        '''
        if record_type==1:
            self.diagnosis.append(record)
        elif record_type==2:
            self.medications.append(record)
        elif record_type==3:
            self.test_results.append(record)
        elif record_type==4:
            self.appointments.append(record)
        elif record_type==5:
            self.medical_history.append(record)
    def view_record(self):
        '''Print all records in the medical record.'''
        '''args:
            None
            returns:
            None'''
        print("Diagnosis:",self.diagnosis)
        print("Medications:",self.medications)
        print("Test Results:",self.test_results)
        print("Appointments:",self.appointments)
        print("Medical History:",self.medical_history)


    
    