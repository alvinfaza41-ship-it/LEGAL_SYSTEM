import customtkinter as ctk
from app.views.base_view import BaseFrame
from app.models.client_model import ClientModel
from app.models.halal_submission_model import HalalSubmissionModel
from app.models.invoice_model import InvoiceModel
from app.models.certificate_model import CertificateModel
from app.themes.islamic_theme import IslamicTheme, Colors


class DashboardFrame(BaseFrame):
    """Dashboard page showing statistics and overview"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.pack(fill="both", expand=True)
        
        # Models
        self.client_model = ClientModel()
        self.submission_model = HalalSubmissionModel()
        self.invoice_model = InvoiceModel()
        self.certificate_model = CertificateModel()
        
        self.create_header("Dashboard", "Assalamu Alaikum, Selamat datang di HCMS")
        self.create_dashboard_content()
        self.refresh_data()
    
    def create_dashboard_content(self):
        """Create dashboard layout with stats cards"""
        # Main container
        main_container = ctk.CTkScrollableFrame(
            self,
            fg_color=Colors.APP_BG,
            label_text="",
            label_font=("", 0)
        )
        main_container.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Welcome section
        self.create_welcome_section(main_container)
        
        # Stats grid - Row 1
        self.create_stats_row_1(main_container)
        
        # Stats grid - Row 2
        self.create_stats_row_2(main_container)
        
        # Action buttons
        self.create_action_buttons(main_container)
    
    def create_welcome_section(self, parent):
        """Create welcome message with Islamic greeting"""
        welcome_frame = ctk.CTkFrame(
            parent,
            fg_color=Colors.HEADER_BG,
            corner_radius=IslamicTheme.CORNER_RADIUS
        )
        welcome_frame.pack(fill="x", padx=20, pady=20)
        
        greeting = ctk.CTkLabel(
            welcome_frame,
            text="☪️ Assalamu Alaikum Wa Rahmatullahi Wa Barakatuh",
            font=("Segoe UI", 16, "bold"),
            text_color=Colors.SIDEBAR_ACTIVE
        )
        greeting.pack(pady=15)
        
        message = ctk.CTkLabel(
            welcome_frame,
            text="Selamat datang di Halal Consultant Management System\nSistem manajemen consultant halal profesional dan terpercaya",
            font=IslamicTheme.FONT_TEXT,
            text_color="#ffffff",
            justify="center"
        )
        message.pack(pady=(0, 15))
    
    def create_stats_row_1(self, parent):
        """Create first row of statistics"""
        stats_frame = ctk.CTkFrame(parent, fg_color=Colors.APP_BG)
        stats_frame.pack(fill="x", padx=20, pady=15)
        
        for i in range(3):
            stats_frame.grid_columnconfigure(i, weight=1)
        
        # Total Clients
        self.total_clients_card = self.create_stat_card(
            parent=stats_frame,
            value="0",
            label="Total Klien",
            icon="👥",
            color="#1a5a3f",
            column=0
        )
        
        # Halal Submissions
        self.total_submissions_card = self.create_stat_card(
            parent=stats_frame,
            value="0",
            label="Pengajuan Halal",
            icon="📋",
            color="#0f4c75",
            column=1
        )
        
        # Invoices
        self.total_invoices_card = self.create_stat_card(
            parent=stats_frame,
            value="0",
            label="Invoice",
            icon="💰",
            color="#d4af37",
            column=2
        )
    
    def create_stats_row_2(self, parent):
        """Create second row of statistics"""
        stats_frame = ctk.CTkFrame(parent, fg_color=Colors.APP_BG)
        stats_frame.pack(fill="x", padx=20, pady=15)
        
        for i in range(3):
            stats_frame.grid_columnconfigure(i, weight=1)
        
        # Certificates
        self.total_certificates_card = self.create_stat_card(
            parent=stats_frame,
            value="0",
            label="Sertifikat",
            icon="📜",
            color="#10b981",
            column=0
        )
        
        # Pending Invoices
        self.pending_invoices_card = self.create_stat_card(
            parent=stats_frame,
            value="0",
            label="Invoice Pending",
            icon="⏳",
            color="#ef4444",
            column=1
        )
        
        # Active Clients
        self.active_clients_card = self.create_stat_card(
            parent=stats_frame,
            value="0",
            label="Klien Aktif",
            icon="✅",
            color="#06b6d4",
            column=2
        )
    
    def create_stat_card(self, parent, value, label, icon, color, column):
        """Create beautiful stat card"""
        card = ctk.CTkFrame(
            parent,
            fg_color=Colors.CARD_BG,
            corner_radius=IslamicTheme.CORNER_RADIUS,
            border_width=2,
            border_color=color
        )
        card.grid(row=0, column=column, sticky="nsew", padx=10, pady=10)
        
        # Icon & Value
        top_frame = ctk.CTkFrame(card, fg_color=Colors.CARD_BG)
        top_frame.pack(fill="x", padx=IslamicTheme.PADDING_MEDIUM, pady=15)
        
        icon_label = ctk.CTkLabel(
            top_frame,
            text=icon,
            font=("Segoe UI", 36),
            text_color=color
        )
        icon_label.pack(side="left", padx=(0, 10))
        
        value_label = ctk.CTkLabel(
            top_frame,
            text=value,
            font=("Segoe UI", 26, "bold"),
            text_color=color
        )
        value_label.pack(side="left", anchor="n")
        
        # Divider
        divider = ctk.CTkFrame(card, fg_color=color, height=1)
        divider.pack(fill="x", padx=IslamicTheme.PADDING_MEDIUM, pady=(0, 10))
        
        # Label
        label_text = ctk.CTkLabel(
            card,
            text=label,
            font=IslamicTheme.FONT_LABEL,
            text_color=Colors.TEXT_SECONDARY
        )
        label_text.pack(anchor="w", padx=IslamicTheme.PADDING_MEDIUM, pady=(0, 15))
        
        # Store reference for updating
        value_label.label_text = label
        return value_label
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = ctk.CTkFrame(parent, fg_color=Colors.APP_BG)
        button_frame.pack(fill="x", padx=20, pady=30)
        
        refresh_btn = ctk.CTkButton(
            button_frame,
            text="🔄 Refresh Data",
            command=self.refresh_data,
            fg_color=Colors.BTN_PRIMARY_BG,
            hover_color=Colors.BTN_PRIMARY_HOVER,
            height=45,
            font=IslamicTheme.FONT_LABEL,
            text_color="#ffffff"
        )
        refresh_btn.pack(side="left", padx=10)
        
        prayer_time = ctk.CTkLabel(
            button_frame,
            text="🕌 Waktu Sholat Dhuhur: 12:30 | Ashar: 15:30",
            font=IslamicTheme.FONT_SMALL,
            text_color=Colors.TEXT_SECONDARY
        )
        prayer_time.pack(side="right", padx=10)
    
    def refresh_data(self):
        """Refresh dashboard data from database"""
        try:
            total_clients = len(self.client_model.get_all())
            total_submissions = len(self.submission_model.get_all())
            total_invoices = len(self.invoice_model.get_all())
            total_certificates = len(self.certificate_model.get_all())
            pending_invoices = len(self.invoice_model.get_by_status("pending"))
            active_clients = len(self.client_model.get_by_status("active"))
            
            self.total_clients_card.configure(text=str(total_clients))
            self.total_submissions_card.configure(text=str(total_submissions))
            self.total_invoices_card.configure(text=str(total_invoices))
            self.total_certificates_card.configure(text=str(total_certificates))
            self.pending_invoices_card.configure(text=str(pending_invoices))
            self.active_clients_card.configure(text=str(active_clients))
            
            self.show_info("Data berhasil diperbarui")
            
        except Exception as e:
            self.show_error(f"Error loading dashboard data: {str(e)}")

