from app.database.database import Database


class HalalSubmissionModel:

    def __init__(self):
        self.db = Database()

    def get_all(self):
        return self.db.fetchall("SELECT * FROM halal_submissions")
    
    def get_by_id(self, submission_id):
        return self.db.fetchone(
            "SELECT * FROM halal_submissions WHERE id = ?",
            (submission_id,)
        )
    
    def get_by_client(self, client_id):
        return self.db.fetchall(
            "SELECT * FROM halal_submissions WHERE client_id = ?",
            (client_id,)
        )
    
    def get_by_status(self, status):
        return self.db.fetchall(
            "SELECT * FROM halal_submissions WHERE status = ?",
            (status,)
        )
    
    def create(self, client_id, submission_type, status='pending'):
        return self.db.execute(
            """INSERT INTO halal_submissions 
               (client_id, submission_type, status) 
               VALUES (?, ?, ?)""",
            (client_id, submission_type, status)
        )
    
    def update(self, submission_id, **kwargs):
        allowed_fields = ['submission_type', 'status', 'completion_date']
        fields = {k: v for k, v in kwargs.items() if k in allowed_fields}
        
        if not fields:
            return None
        
        set_clause = ", ".join([f"{k} = ?" for k in fields.keys()])
        values = list(fields.values()) + [submission_id]
        
        return self.db.execute(
            f"UPDATE halal_submissions SET {set_clause} WHERE id = ?",
            tuple(values)
        )
    
    def delete(self, submission_id):
        return self.db.execute(
            "DELETE FROM halal_submissions WHERE id = ?",
            (submission_id,)
        )
