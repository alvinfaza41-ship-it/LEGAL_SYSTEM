import customtkinter as ctk


def create_statusbar(self):
    """Create a status bar attached to the given widget instance.

    Saves widgets as attributes on self: self.status_frame and self.status_label
    so callers can later update the label text via self.status_label.configure(text=...).
    """
    # Frame for the status bar
    self.status_frame = ctk.CTkFrame(self, height=30, fg_color="#DDDDDD")
    self.status_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

    # Label inside the status bar
    self.status_label = ctk.CTkLabel(self.status_frame, text="Status : Ready")
    self.status_label.pack(side="left", padx=10)
    import customtkinter as ctk

class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=30)

        label = ctk.CTkLabel(
            self,
            text="Status : Ready"
        )

        label.pack(side="left", padx=10)
        import sqlite3
from pathlib import Path

DB_FOLDER = Path("data/database")
DB_FOLDER.mkdir(parents=True, exist_ok=True)

DB_PATH = DB_FOLDER / "hcms.db"


class Database:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()