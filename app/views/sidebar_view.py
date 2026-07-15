import customtkinter as ctk
from app.themes.islamic_theme import IslamicTheme, Colors


class SidebarFrame(ctk.CTkFrame):
    """Sidebar with professional Islamic design"""
    
    def __init__(self, parent, on_menu_select=None, **kwargs):
        super().__init__(
            parent,
            fg_color=Colors.SIDEBAR_BG,
            width=280,
            **kwargs
        )
        
        self.on_menu_select = on_menu_select
        self.buttons = {}
        self.active_button = None
        
        self.create_menu()
    
    def create_menu(self):
        """Create professional menu with Islamic theme"""
        # Logo/Header section
        header = ctk.CTkFrame(self, fg_color=Colors.SIDEBAR_BG)
        header.pack(fill="x", padx=0, pady=0)
        
        # App title with Islamic symbol
        title = ctk.CTkLabel(
            header,
            text="☪️ HCMS",
            font=("Segoe UI", 28, "bold"),
            text_color=Colors.SIDEBAR_ACTIVE
        )
        title.pack(pady=(25, 5), padx=20)
        
        # Subtitle
        subtitle = ctk.CTkLabel(
            header,
            text="Halal Consultant",
            font=("Segoe UI", 12),
            text_color=Colors.SIDEBAR_TEXT
        )
        subtitle.pack(padx=20, pady=(0, 25))
        
        # Separator with Islamic pattern
        separator = ctk.CTkFrame(header, fg_color=Colors.SIDEBAR_ACTIVE, height=2)
        separator.pack(fill="x", padx=15, pady=10)
        
        # Scrollable menu frame
        menu_container = ctk.CTkScrollableFrame(
            self,
            fg_color=Colors.SIDEBAR_BG,
            label_text="",
            label_font=("", 0)
        )
        menu_container.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Menu items
        menu_items = [
            ("🏠", "Dashboard", "dashboard"),
            ("👥", "Manajemen Klien", "clients"),
            ("📋", "Pengajuan Halal", "submissions"),
            ("💰", "Invoice", "invoices"),
            ("📜", "Sertifikat", "certificates"),
            ("📊", "Laporan", "reports"),
            ("⚙️", "Pengaturan", "settings"),
        ]
        
        for icon, label, key in menu_items:
            self._create_menu_button(menu_container, icon, label, key)
        
        # Bottom separator
        bottom_sep = ctk.CTkFrame(self, fg_color=Colors.SIDEBAR_ACTIVE, height=1)
        bottom_sep.pack(fill="x", padx=15, pady=20, side="bottom")
        
        # Logout button at bottom
        logout_btn = ctk.CTkButton(
            self,
            text="🚪 Keluar",
            command=self.on_logout,
            fg_color=Colors.DANGER,
            hover_color="#dc2626",
            text_color="white",
            font=IslamicTheme.FONT_LABEL,
            height=45,
            corner_radius=IslamicTheme.CORNER_RADIUS,
            border_width=0
        )
        logout_btn.pack(fill="x", padx=15, pady=(0, 20), side="bottom")
        
        # Prayer info at bottom
        prayer_info = ctk.CTkLabel(
            self,
            text="🕌 Dzuhur: 12:30",
            font=("Segoe UI", 9),
            text_color=Colors.SIDEBAR_ACTIVE
        )
        prayer_info.pack(side="bottom", pady=(0, 5))
    
    def _create_menu_button(self, parent, icon, label, key):
        """Create individual menu button"""
        btn = ctk.CTkButton(
            parent,
            text=f"  {icon}  {label}",
            command=lambda k=key: self.select_menu(k),
            fg_color=Colors.SIDEBAR_HOVER,
            hover_color=Colors.SIDEBAR_ACTIVE,
            text_color=Colors.SIDEBAR_TEXT,
            font=IslamicTheme.FONT_TEXT,
            height=50,
            corner_radius=IslamicTheme.CORNER_RADIUS,
            border_width=0,
            anchor="w"
        )
        btn.pack(fill="x", padx=15, pady=8)
        self.buttons[key] = btn
    
    def select_menu(self, menu_key):
        """Handle menu selection"""
        # Reset previous button
        if self.active_button:
            self.active_button.configure(
                fg_color=Colors.SIDEBAR_HOVER,
                border_width=0
            )
        
        # Highlight current button
        self.buttons[menu_key].configure(
            fg_color=Colors.SIDEBAR_ACTIVE,
            text_color=Colors.SIDEBAR_BG,
            border_width=2,
            border_color=Colors.SIDEBAR_TEXT
        )
        self.active_button = self.buttons[menu_key]
        
        if self.on_menu_select:
            self.on_menu_select(menu_key)
    
    def on_logout(self):
        """Handle logout"""
        pass

