from app.database.database import Database


class InvoiceModel:

    def __init__(self):
        self.db = Database()

    def get_all(self):
        return self.db.fetchall("SELECT * FROM invoices")
    
    def get_by_id(self, invoice_id):
        return self.db.fetchone(
            "SELECT * FROM invoices WHERE id = ?",
            (invoice_id,)
        )
    
    def get_by_client(self, client_id):
        return self.db.fetchall(
            "SELECT * FROM invoices WHERE client_id = ?",
            (client_id,)
        )
    
    def get_by_status(self, status):
        return self.db.fetchall(
            "SELECT * FROM invoices WHERE status = ?",
            (status,)
        )
    
    def create(self, client_id, invoice_number, amount, due_date, status='pending'):
        return self.db.execute(
            """INSERT INTO invoices 
               (client_id, invoice_number, amount, due_date, status) 
               VALUES (?, ?, ?, ?, ?)""",
            (client_id, invoice_number, amount, due_date, status)
        )
    
    def update(self, invoice_id, **kwargs):
        allowed_fields = ['amount', 'status', 'due_date']
        fields = {k: v for k, v in kwargs.items() if k in allowed_fields}
        
        if not fields:
            return None
        
        set_clause = ", ".join([f"{k} = ?" for k in fields.keys()])
        values = list(fields.values()) + [invoice_id]
        
        return self.db.execute(
            f"UPDATE invoices SET {set_clause} WHERE id = ?",
            tuple(values)
        )
    
    def delete(self, invoice_id):
        return self.db.execute(
            "DELETE FROM invoices WHERE id = ?",
            (invoice_id,)
        )
    
    def get_total_revenue(self):
        result = self.db.fetchone(
            "SELECT SUM(amount) FROM invoices WHERE status = 'paid'"
        )
        return result[0] if result and result[0] else 0
