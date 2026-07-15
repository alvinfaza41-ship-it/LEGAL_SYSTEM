from app.database.database import Database


class CertificateModel:

    def __init__(self):
        self.db = Database()

    def get_all(self):
        return self.db.fetchall("SELECT * FROM certificates")
    
    def get_by_id(self, cert_id):
        return self.db.fetchone(
            "SELECT * FROM certificates WHERE id = ?",
            (cert_id,)
        )
    
    def get_by_client(self, client_id):
        return self.db.fetchall(
            "SELECT * FROM certificates WHERE client_id = ?",
            (client_id,)
        )
    
    def get_by_status(self, status):
        return self.db.fetchall(
            "SELECT * FROM certificates WHERE status = ?",
            (status,)
        )
    
    def create(self, client_id, certificate_number, issue_date, expiry_date, status='active'):
        return self.db.execute(
            """INSERT INTO certificates 
               (client_id, certificate_number, issue_date, expiry_date, status) 
               VALUES (?, ?, ?, ?, ?)""",
            (client_id, certificate_number, issue_date, expiry_date, status)
        )
    
    def update(self, cert_id, **kwargs):
        allowed_fields = ['certificate_number', 'issue_date', 'expiry_date', 'status']
        fields = {k: v for k, v in kwargs.items() if k in allowed_fields}
        
        if not fields:
            return None
        
        set_clause = ", ".join([f"{k} = ?" for k in fields.keys()])
        values = list(fields.values()) + [cert_id]
        
        return self.db.execute(
            f"UPDATE certificates SET {set_clause} WHERE id = ?",
            tuple(values)
        )
    
    def delete(self, cert_id):
        return self.db.execute(
            "DELETE FROM certificates WHERE id = ?",
            (cert_id,)
        )
