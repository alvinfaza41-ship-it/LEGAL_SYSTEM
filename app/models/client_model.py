from app.database.database import Database


class ClientModel:

    def __init__(self):
        self.db = Database()

    def get_all(self):
        return self.db.fetchall("SELECT * FROM clients")
    
    def get_by_id(self, client_id):
        return self.db.fetchone(
            "SELECT * FROM clients WHERE id = ?",
            (client_id,)
        )
    
    def get_by_status(self, status):
        return self.db.fetchall(
            "SELECT * FROM clients WHERE status = ?",
            (status,)
        )
    
    def create(self, name, phone, email, address, company, industry):
        """Create new client"""
        return self.db.execute(
            """INSERT INTO clients 
               (name, phone, email, address, company, industry) 
               VALUES (?, ?, ?, ?, ?, ?)""",
            (name, phone, email, address, company, industry)
        )
    
    def update(self, client_id, **kwargs):
        """Update client"""
        allowed_fields = ['name', 'phone', 'email', 'address', 'company', 'industry', 'status']
        fields = {k: v for k, v in kwargs.items() if k in allowed_fields}
        
        if not fields:
            return None
        
        set_clause = ", ".join([f"{k} = ?" for k in fields.keys()])
        values = list(fields.values()) + [client_id]
        
        return self.db.execute(
            f"UPDATE clients SET {set_clause}, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            tuple(values)
        )
    
    def delete(self, client_id):
        """Delete client"""
        return self.db.execute(
            "DELETE FROM clients WHERE id = ?",
            (client_id,)
        )
    
    def search(self, keyword):
        """Search clients by name, phone, or email"""
        keyword = f"%{keyword}%"
        return self.db.fetchall(
            """SELECT * FROM clients 
               WHERE name LIKE ? OR phone LIKE ? OR email LIKE ?""",
            (keyword, keyword, keyword)
        )