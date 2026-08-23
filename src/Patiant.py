from src.Medical_record import Medical_record

class Patiant():
    
    def __init__(self):
        self.medical_record=Medical_record()
    
    def view_record(self):
        self.medical_record.view_record()
    
    def add_record(self,record_type,record_id,record):
        self.medical_record.add_record(record_type,record_id,record)
    
    def update_record(self,record_type,record_id,updated_record):
        self.medical_record.update_record(record_type,record_id,updated_record)
    
    def delete_record(self,record_type,record_id):
        self.medical_record.delete_record(record_type,record_id )


        

        