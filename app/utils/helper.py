from datetime import datetime


class Helper:
    """Helper utilities"""
    
    @staticmethod
    def format_currency(amount):
        """Format number as Indonesian Rupiah"""
        if not amount:
            return "Rp 0"
        try:
            return f"Rp {int(amount):,}".replace(",", ".")
        except:
            return str(amount)
    
    @staticmethod
    def format_date(date_obj):
        """Format date to string"""
        if not date_obj:
            return "-"
        if isinstance(date_obj, str):
            return date_obj
        try:
            return datetime.fromisoformat(str(date_obj)).strftime("%d-%m-%Y")
        except:
            return str(date_obj)
    
    @staticmethod
    def format_datetime(dt_obj):
        """Format datetime to string"""
        if not dt_obj:
            return "-"
        if isinstance(dt_obj, str):
            return dt_obj
        try:
            return datetime.fromisoformat(str(dt_obj)).strftime("%d-%m-%Y %H:%M")
        except:
            return str(dt_obj)
    
    @staticmethod
    def get_status_color(status):
        """Get color for status badge"""
        colors = {
            "active": "#10b981",
            "inactive": "#ef4444",
            "pending": "#f97316",
            "completed": "#06b6d4",
            "paid": "#10b981",
            "unpaid": "#ef4444",
        }
        return colors.get(status, "#6b7280")
    
    @staticmethod
    def truncate_text(text, length=50):
        """Truncate text to specified length"""
        if not text:
            return "-"
        if len(text) <= length:
            return text
        return text[:length] + "..."
