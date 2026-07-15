import re
from typing import Tuple


class Validator:
    """Data validation utilities"""
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """Validate email format"""
        if not email:
            return True, ""
        
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return True, ""
        return False, "Invalid email format"
    
    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, str]:
        """Validate phone number format"""
        if not phone:
            return True, ""
        
        # Accept any phone number with at least 10 digits
        digits = re.sub(r"\D", "", phone)
        if len(digits) >= 10:
            return True, ""
        return False, "Phone number must have at least 10 digits"
    
    @staticmethod
    def validate_required(value: str, field_name: str) -> Tuple[bool, str]:
        """Validate required field"""
        if not value or not value.strip():
            return False, f"{field_name} is required"
        return True, ""
    
    @staticmethod
    def validate_client_form(data: dict) -> Tuple[bool, str]:
        """Validate client form data"""
        # Check required fields
        if not data.get("name", "").strip():
            return False, "Client name is required"
        
        # Validate email if provided
        if data.get("email"):
            valid, msg = Validator.validate_email(data["email"])
            if not valid:
                return False, msg
        
        # Validate phone if provided
        if data.get("phone"):
            valid, msg = Validator.validate_phone(data["phone"])
            if not valid:
                return False, msg
        
        return True, ""
    
    @staticmethod
    def validate_invoice_form(data: dict) -> Tuple[bool, str]:
        """Validate invoice form data"""
        if not data.get("invoice_number", "").strip():
            return False, "Invoice number is required"
        
        if not data.get("amount"):
            return False, "Amount is required"
        
        try:
            amount = float(data["amount"])
            if amount <= 0:
                return False, "Amount must be greater than 0"
        except ValueError:
            return False, "Amount must be a valid number"
        
        return True, ""
