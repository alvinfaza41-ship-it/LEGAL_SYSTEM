class Formatter:
    """Data formatting utilities"""
    
    @staticmethod
    def format_client_data(client):
        """Format client data for display"""
        if not client:
            return None
        
        return {
            "id": client["id"],
            "name": client["name"],
            "phone": client["phone"] or "-",
            "email": client["email"] or "-",
            "address": client["address"] or "-",
            "company": client["company"] or "-",
            "industry": client["industry"] or "-",
            "status": client["status"],
            "created_at": client["created_at"],
        }
    
    @staticmethod
    def format_invoice_data(invoice):
        """Format invoice data for display"""
        if not invoice:
            return None
        
        return {
            "id": invoice["id"],
            "invoice_number": invoice["invoice_number"],
            "client_id": invoice["client_id"],
            "amount": invoice["amount"],
            "status": invoice["status"],
            "due_date": invoice["due_date"],
            "created_at": invoice["created_at"],
        }
    
    @staticmethod
    def format_certificate_data(cert):
        """Format certificate data for display"""
        if not cert:
            return None
        
        return {
            "id": cert["id"],
            "certificate_number": cert["certificate_number"],
            "client_id": cert["client_id"],
            "issue_date": cert["issue_date"],
            "expiry_date": cert["expiry_date"],
            "status": cert["status"],
        }
