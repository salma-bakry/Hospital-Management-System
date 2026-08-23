class Medical_record():
  
    def __init__(self):
        self.diagnosis={}
        self.medications={}
        self.test_results={}
        self.appointments={}
        self.medical_history={}
    def add_record(self,record_type,record_id,record):
        if record_type=="diagnosis":
            self.diagnosis[record_id]=record
        elif record_type=="medications":
            self.medications[record_id]=record
        elif record_type=="test_results":
            self.test_results[record_id]=record
        elif record_type=="appointments":
            self.appointments[record_id]=record
        elif record_type=="medical_history":
            self.medical_history[record_id]=record
    def view_record(self):
        print("Diagnosis:",self.diagnosis)
        print("Medications:",self.medications)
        print("Test Results:",self.test_results)
        print("Appointments:",self.appointments)
        print("Medical History:",self.medical_history)
    def update_record(self,record_type,record_id,updated_record):
        if record_type=="diagnosis":
            self.diagnosis[record_id]=updated_record
        elif record_type=="medications":
            self.medications[record_id]=updated_record
        elif record_type=="test_results":
            self.test_results[record_id]=updated_record
        elif record_type=="appointments":
            self.appointments[record_id]=updated_record
        elif record_type=="medical_history":
            self.medical_history[record_id]=updated_record
    def delete_record(self,record_type,record_id):
        if record_type=="diagnosis":
            del self.diagnosis[record_id]
        elif record_type=="medications":
            del self.medications[record_id]
        elif record_type=="test_results":
            del self.test_results[record_id]
        elif record_type=="appointments":
            del self.appointments[record_id]
        elif record_type=="medical_history":
            del self.medical_history[record_id]
        
    
    