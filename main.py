import customtkinter as ctk
from app.database.database import Database
from app.views.sidebar_view import SidebarFrame
from app.views.dashboard_view import DashboardFrame
from app.views.client_list_view import ClientListFrame
from app.views.client_form_view import ClientFormFrame
from app.themes.islamic_theme import Colors, IslamicTheme

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


class HCMS(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("HCMS - Halal Consultant Management System")
        self.geometry("1600x900")
        self.minsize(1300, 750)
        
        try:
            self.iconbitmap("assets/logo/logo.ico")
        except:
            pass
        
        self.configure(fg_color=Colors.APP_BG)
        
        # Initialize database
        self.db = Database()
        self.db.initialize()
        
        # Grid configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Current frame
        self.current_frame = None
        self.current_menu = None
        
        # Create sidebar
        self.sidebar = SidebarFrame(self, on_menu_select=self.show_page)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        
        # Create content frame
        self.content_frame = ctk.CTkFrame(self, fg_color=Colors.APP_BG)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)
        
        # Show dashboard by default
        self.show_page("dashboard")
    
    def show_page(self, page_name):
        """Show different pages based on menu selection"""
        if self.current_frame:
            self.current_frame.destroy()
        
        try:
            if page_name == "dashboard":
                self.current_frame = DashboardFrame(self.content_frame)
            
            elif page_name == "clients":
                self.current_frame = ClientListFrame(
                    self.content_frame,
                    on_create=lambda: self.show_client_form(),
                    on_edit=lambda cid: self.show_client_form(cid)
                )
            
            elif page_name == "submissions":
                self.current_frame = self._create_placeholder("📋 Pengajuan Halal")
            
            elif page_name == "invoices":
                self.current_frame = self._create_placeholder("💰 Invoice")
            
            elif page_name == "certificates":
                self.current_frame = self._create_placeholder("📜 Sertifikat")
            
            elif page_name == "reports":
                self.current_frame = self._create_placeholder("📊 Laporan")
            
            elif page_name == "settings":
                self.current_frame = self._create_placeholder("⚙️ Pengaturan")
        
        except Exception as e:
            print(f"Error showing page {page_name}: {e}")
            self.current_frame = self._create_placeholder(f"Error: {str(e)}")
    
    def show_client_form(self, client_id=None):
        """Show client form for add/edit"""
        if self.current_frame:
            self.current_frame.destroy()
        
        def on_save():
            self.show_page("clients")
        
        self.current_frame = ClientFormFrame(
            self.content_frame,
            client_id=client_id,
            on_save=on_save
        )
    
    def _create_placeholder(self, title):
        """Create professional placeholder frame"""
        frame = ctk.CTkFrame(self.content_frame, fg_color=Colors.APP_BG)
        frame.pack(fill="both", expand=True)
        
        # Header
        header = ctk.CTkFrame(frame, fg_color=Colors.HEADER_BG, height=80)
        header.pack(fill="x", padx=0, pady=0)
        
        title_label = ctk.CTkLabel(
            header,
            text=title,
            font=IslamicTheme.FONT_HEADING,
            text_color=Colors.HEADER_TEXT
        )
        title_label.pack(pady=20)
        
        # Content
        content = ctk.CTkFrame(frame, fg_color=Colors.APP_BG)
        content.pack(fill="both", expand=True)
        
        message = ctk.CTkLabel(
            content,
            text="⏳ Fitur ini sedang dalam pengembangan",
            font=IslamicTheme.FONT_SUBHEADING,
            text_color=Colors.TEXT_SECONDARY
        )
        message.pack(pady=80)
        
        subtitle = ctk.CTkLabel(
            content,
            text="Mohon ditunggu, segera hadir...",
            font=IslamicTheme.FONT_TEXT,
            text_color=Colors.TEXT_SECONDARY
        )
        subtitle.pack()
        
        return frame


if __name__ == "__main__":
    app = HCMS()
    app.mainloop()

