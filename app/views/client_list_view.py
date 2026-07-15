import customtkinter as ctk
from app.views.base_view import BaseFrame
from app.models.client_model import ClientModel
from app.themes.islamic_theme import IslamicTheme, Colors


class ClientListFrame(BaseFrame):
    """List all clients with professional Islamic design"""
    
    def __init__(self, parent, on_create=None, on_edit=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.pack(fill="both", expand=True)
        
        self.client_model = ClientModel()
        self.on_create = on_create
        self.on_edit = on_edit
        self.clients = []
        
        self.create_header("Manajemen Klien", "Kelola data klien dengan mudah dan profesional")
        self.create_content()
        self.load_clients()
    
    def create_content(self):
        """Create search bar and client list"""
        container = ctk.CTkFrame(self, fg_color=Colors.APP_BG)
        container.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Search frame
        search_frame = ctk.CTkFrame(container, fg_color=Colors.CARD_BG, corner_radius=IslamicTheme.CORNER_RADIUS)
        search_frame.pack(fill="x", padx=20, pady=20)
        
        # Search content
        search_content = ctk.CTkFrame(search_frame, fg_color=Colors.CARD_BG)
        search_content.pack(fill="x", padx=IslamicTheme.PADDING_MEDIUM, pady=IslamicTheme.PADDING_MEDIUM)
        
        search_label = ctk.CTkLabel(
            search_content,
            text="🔍 Pencarian Klien",
            font=IslamicTheme.FONT_LABEL,
            text_color=Colors.TEXT_PRIMARY
        )
        search_label.pack(anchor="w", pady=(0, 10))
        
        self.search_entry = ctk.CTkEntry(
            search_content,
            placeholder_text="Cari berdasarkan nama, telepon, atau email...",
            height=40,
            font=IslamicTheme.FONT_TEXT,
            fg_color="#f9f9f9",
            border_color=Colors.SIDEBAR_HOVER
        )
        self.search_entry.pack(fill="x", pady=(0, 10))
        
        # Button frame
        button_frame = ctk.CTkFrame(search_content, fg_color=Colors.CARD_BG)
        button_frame.pack(fill="x")
        
        search_btn = ctk.CTkButton(
            button_frame,
            text="🔍 Cari",
            command=self.search_clients,
            fg_color=Colors.BTN_PRIMARY_BG,
            hover_color=Colors.BTN_PRIMARY_HOVER,
            height=40,
            font=IslamicTheme.FONT_LABEL,
            width=120
        )
        search_btn.pack(side="left", padx=(0, 10))
        
        refresh_btn = ctk.CTkButton(
            button_frame,
            text="🔄 Refresh",
            command=self.load_clients,
            fg_color=Colors.INFO,
            hover_color="#0891b2",
            height=40,
            font=IslamicTheme.FONT_LABEL,
            width=120
        )
        refresh_btn.pack(side="left", padx=10)
        
        add_btn = ctk.CTkButton(
            button_frame,
            text="➕ Tambah Klien",
            command=self.on_create,
            fg_color=Colors.SUCCESS,
            hover_color="#059669",
            height=40,
            font=IslamicTheme.FONT_LABEL,
            width=150
        )
        add_btn.pack(side="right", padx=(10, 0))
        
        # Table frame
        table_frame = ctk.CTkFrame(
            container,
            fg_color=Colors.CARD_BG,
            corner_radius=IslamicTheme.CORNER_RADIUS,
            border_width=1,
            border_color=Colors.CARD_BORDER
        )
        table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Headers
        header_frame = ctk.CTkFrame(table_frame, fg_color=Colors.HEADER_BG, corner_radius=0)
        header_frame.pack(fill="x")
        
        columns = ["ID", "Nama", "Telepon", "Email", "Perusahaan", "Status", "Aksi"]
        col_widths = [50, 150, 120, 150, 150, 100, 150]
        
        for col, width in zip(columns, col_widths):
            label = ctk.CTkLabel(
                header_frame,
                text=col,
                font=IslamicTheme.FONT_LABEL,
                text_color="#ffffff"
            )
            label.pack(side="left", padx=10, pady=12, fill="x", expand=False)
        
        # Scrollable area
        self.scrollable_frame = ctk.CTkScrollableFrame(
            table_frame,
            fg_color=Colors.CARD_BG,
            label_font=("", 0),
            label_text=""
        )
        self.scrollable_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Info label
        info_frame = ctk.CTkFrame(container, fg_color=Colors.APP_BG)
        info_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        self.info_label = ctk.CTkLabel(
            info_frame,
            text="Total Klien: 0",
            font=IslamicTheme.FONT_TEXT,
            text_color=Colors.TEXT_SECONDARY
        )
        self.info_label.pack(anchor="w")
    
    def load_clients(self):
        """Load all clients from database"""
        try:
            self.clients = self.client_model.get_all()
            self.display_clients(self.clients)
            self.info_label.configure(text=f"📊 Total Klien: {len(self.clients)}")
        except Exception as e:
            self.show_error(f"Error loading clients: {str(e)}")
    
    def search_clients(self):
        """Search clients"""
        keyword = self.search_entry.get().strip()
        if not keyword:
            self.load_clients()
            return
        
        try:
            self.clients = self.client_model.search(keyword)
            self.display_clients(self.clients)
            self.info_label.configure(text=f"🔍 Hasil Pencarian: {len(self.clients)}")
        except Exception as e:
            self.show_error(f"Error searching clients: {str(e)}")
    
    def display_clients(self, clients):
        """Display clients in table"""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        if not clients:
            empty_label = ctk.CTkLabel(
                self.scrollable_frame,
                text="Tidak ada data klien",
                font=IslamicTheme.FONT_TEXT,
                text_color=Colors.TEXT_SECONDARY
            )
            empty_label.pack(pady=50)
            return
        
        for client in clients:
            self.create_client_row(client)
    
    def create_client_row(self, client):
        """Create a single client row"""
        row_frame = ctk.CTkFrame(
            self.scrollable_frame,
            fg_color=Colors.CARD_BG,
            border_width=1,
            border_color=Colors.BORDER_COLOR,
            corner_radius=6
        )
        row_frame.pack(fill="x", padx=5, pady=3)
        
        # Status color mapping
        status_colors = {
            "active": ("#ecfdf5", "#10b981"),
            "inactive": ("#fef2f2", "#ef4444"),
            "pending": ("#fffbeb", "#f97316"),
        }
        
        bg_color, text_color = status_colors.get(client['status'], ("#f9f9f9", Colors.TEXT_PRIMARY))
        
        # Data
        data = [
            str(client['id']),
            client['name'],
            client['phone'] or '-',
            client['email'] or '-',
            client['company'] or '-',
            client['status'],
        ]
        
        col_widths = [50, 150, 120, 150, 150, 100]
        
        for data_val, width in zip(data, col_widths):
            label = ctk.CTkLabel(
                row_frame,
                text=data_val,
                font=IslamicTheme.FONT_TEXT,
                text_color=Colors.TEXT_PRIMARY
            )
            label.pack(side="left", padx=10, pady=12, fill="x", expand=False)
        
        # Action buttons
        action_frame = ctk.CTkFrame(row_frame, fg_color=Colors.CARD_BG)
        action_frame.pack(side="left", padx=10, pady=8)
        
        edit_btn = ctk.CTkButton(
            action_frame,
            text="✏️",
            command=lambda c=client: self.on_edit(c['id']),
            width=40,
            height=30,
            font=IslamicTheme.FONT_LABEL,
            fg_color=Colors.INFO,
            hover_color="#0891b2"
        )
        edit_btn.pack(side="left", padx=2)
        
        delete_btn = ctk.CTkButton(
            action_frame,
            text="🗑️",
            command=lambda c=client: self.delete_client(c['id']),
            fg_color=Colors.DANGER,
            hover_color="#dc2626",
            width=40,
            height=30,
            font=IslamicTheme.FONT_LABEL
        )
        delete_btn.pack(side="left", padx=2)
    
    def delete_client(self, client_id):
        """Delete client with confirmation"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Konfirmasi Hapus")
        dialog.geometry("350x150")
        dialog.resizable(False, False)
        dialog.configure(fg_color=Colors.APP_BG)
        
        label = ctk.CTkLabel(
            dialog,
            text="⚠️ Apakah Anda yakin ingin menghapus klien ini?",
            wraplength=320,
            font=IslamicTheme.FONT_TEXT,
            text_color=Colors.TEXT_PRIMARY
        )
        label.pack(pady=20)
        
        def confirm_delete():
            try:
                self.client_model.delete(client_id)
                self.show_info("✅ Klien berhasil dihapus")
                dialog.destroy()
                self.load_clients()
            except Exception as e:
                self.show_error(f"Error deleting client: {str(e)}")
                dialog.destroy()
        
        def cancel_delete():
            dialog.destroy()
        
        btn_frame = ctk.CTkFrame(dialog, fg_color=Colors.APP_BG)
        btn_frame.pack(pady=10)
        
        yes_btn = ctk.CTkButton(
            btn_frame,
            text="Ya, Hapus",
            command=confirm_delete,
            fg_color=Colors.DANGER,
            hover_color="#dc2626",
            width=120,
            height=40,
            font=IslamicTheme.FONT_LABEL
        )
        yes_btn.pack(side="left", padx=5)
        
        no_btn = ctk.CTkButton(
            btn_frame,
            text="Batal",
            command=cancel_delete,
            width=120,
            height=40,
            font=IslamicTheme.FONT_LABEL
        )
        no_btn.pack(side="left", padx=5)

