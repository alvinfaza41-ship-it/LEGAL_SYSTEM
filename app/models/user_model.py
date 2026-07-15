from app.database.database import Database
import hashlib


class UserModel:

    def __init__(self):
        self.db = Database()

    def get_all(self):
        return self.db.fetchall("SELECT id, username, email, full_name, role FROM users")
    
    def get_by_id(self, user_id):
        return self.db.fetchone(
            "SELECT id, username, email, full_name, role FROM users WHERE id = ?",
            (user_id,)
        )
    
    def get_by_username(self, username):
        return self.db.fetchone(
            "SELECT id, username, email, full_name, role FROM users WHERE username = ?",
            (username,)
        )
    
    def authenticate(self, username, password):
        """Verify user credentials"""
        user = self.db.fetchone(
            "SELECT id, username, email, password, full_name, role FROM users WHERE username = ?",
            (username,)
        )
        if user and self._verify_password(password, user['password']):
            return {
                'id': user['id'],
                'username': user['username'],
                'email': user['email'],
                'full_name': user['full_name'],
                'role': user['role']
            }
        return None
    
    def create(self, username, email, password, full_name, role='user'):
        """Create new user"""
        hashed_password = self._hash_password(password)
        return self.db.execute(
            """INSERT INTO users 
               (username, email, password, full_name, role) 
               VALUES (?, ?, ?, ?, ?)""",
            (username, email, hashed_password, full_name, role)
        )
    
    def update(self, user_id, **kwargs):
        """Update user"""
        allowed_fields = ['email', 'full_name', 'role']
        fields = {k: v for k, v in kwargs.items() if k in allowed_fields}
        
        if not fields:
            return None
        
        set_clause = ", ".join([f"{k} = ?" for k in fields.keys()])
        values = list(fields.values()) + [user_id]
        
        return self.db.execute(
            f"UPDATE users SET {set_clause} WHERE id = ?",
            tuple(values)
        )
    
    def delete(self, user_id):
        """Delete user"""
        return self.db.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )
    
    def change_password(self, user_id, old_password, new_password):
        """Change user password"""
        user = self.db.fetchone(
            "SELECT password FROM users WHERE id = ?",
            (user_id,)
        )
        
        if user and self._verify_password(old_password, user['password']):
            hashed_password = self._hash_password(new_password)
            return self.db.execute(
                "UPDATE users SET password = ? WHERE id = ?",
                (hashed_password, user_id)
            )
        return None
    
    @staticmethod
    def _hash_password(password):
        """Hash password with SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def _verify_password(password, hashed):
        """Verify password against hash"""
        return hashlib.sha256(password.encode()).hexdigest() == hashed
