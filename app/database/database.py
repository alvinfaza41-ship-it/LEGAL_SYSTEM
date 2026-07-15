import sqlite3
import os
from pathlib import Path

class Database:
    
    def __init__(self):
        db_path = Path("data/database/hcms.db")
        db_path.parent.mkdir(parents=True, exist_ok=True)
        
        self.conn = sqlite3.connect(str(db_path))
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row
    
    def initialize(self):
        """Initialize database with schema"""
        try:
            sql_file = Path("data/database/database.sql")
            if sql_file.exists():
                with open(sql_file, "r", encoding="utf8") as file:
                    sql = file.read()
                    if sql.strip():
                        self.cursor.executescript(sql)
                        self.conn.commit()
            else:
                self._create_default_schema()
        except Exception as e:
            print(f"Error initializing database: {e}")
            self._create_default_schema()
    
    def _create_default_schema(self):
        """Create default schema if no SQL file exists"""
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            full_name TEXT,
            role TEXT DEFAULT 'user',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT,
            address TEXT,
            company TEXT,
            industry TEXT,
            status TEXT DEFAULT 'active',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE IF NOT EXISTS halal_submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            submission_type TEXT,
            status TEXT DEFAULT 'pending',
            submission_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            completion_date DATETIME,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        );
        
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            invoice_number TEXT UNIQUE,
            amount REAL,
            status TEXT DEFAULT 'pending',
            due_date DATE,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        );
        
        CREATE TABLE IF NOT EXISTS certificates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            certificate_number TEXT UNIQUE,
            issue_date DATE,
            expiry_date DATE,
            status TEXT DEFAULT 'active',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        );
        """
        self.cursor.executescript(sql)
        self.conn.commit()
    
    def fetchall(self, query, params=()):
        """Fetch all records"""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")
            return []
    
    def fetchone(self, query, params=()):
        """Fetch single record"""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
    
    def execute(self, query, params=()):
        """Execute query (INSERT, UPDATE, DELETE)"""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            self.conn.rollback()
            print(f"Error executing query: {e}")
            return None
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()