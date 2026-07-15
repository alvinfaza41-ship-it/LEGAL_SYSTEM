from app.models.client_model import ClientModel
from app.models.user_model import UserModel
from app.models.invoice_model import InvoiceModel
from app.models.certificate_model import CertificateModel
from app.models.halal_submission_model import HalalSubmissionModel


class AppController:
    """Main application controller"""
    
    def __init__(self):
        self.client_model = ClientModel()
        self.user_model = UserModel()
        self.invoice_model = InvoiceModel()
        self.certificate_model = CertificateModel()
        self.submission_model = HalalSubmissionModel()
        self.current_user = None
    
    def authenticate_user(self, username, password):
        """Authenticate user login"""
        user = self.user_model.authenticate(username, password)
        if user:
            self.current_user = user
            return True
        return False
    
    def logout(self):
        """Logout current user"""
        self.current_user = None
    
    def get_dashboard_stats(self):
        """Get dashboard statistics"""
        try:
            return {
                "total_clients": len(self.client_model.get_all()),
                "active_clients": len(self.client_model.get_by_status("active")),
                "total_invoices": len(self.invoice_model.get_all()),
                "pending_invoices": len(self.invoice_model.get_by_status("pending")),
                "total_submissions": len(self.submission_model.get_all()),
                "total_certificates": len(self.certificate_model.get_all()),
            }
        except Exception as e:
            print(f"Error getting dashboard stats: {e}")
            return {}
    
    def search_clients(self, keyword):
        """Search clients"""
        return self.client_model.search(keyword)
    
    def get_client_details(self, client_id):
        """Get client details with related data"""
        try:
            client = self.client_model.get_by_id(client_id)
            if not client:
                return None
            
            return {
                "client": client,
                "invoices": self.invoice_model.get_by_client(client_id),
                "certificates": self.certificate_model.get_by_client(client_id),
                "submissions": self.submission_model.get_by_client(client_id),
            }
        except Exception as e:
            print(f"Error getting client details: {e}")
            return None
