import customtkinter as ctk
from app.views.base_view import BaseFrame
from app.models.client_model import ClientModel
from app.themes.islamic_theme import IslamicTheme, Colors


class ClientFormFrame(BaseFrame):
    """Form to add or edit client with professional Islamic design"""
    
    def __init__(self, parent, client_id=None, on_save=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.pack(fill="both", expand=True)
        
        self.client_model = ClientModel()
        self.client_id = client_id
        self.on_save = on_save
        self.is_edit = client_id is not None
        
        title = "Edit Data Klien" if self.is_edit else "Tambah Klien Baru"
        subtitle = "Perbarui informasi klien" if self.is_edit else "Isi data klien dengan lengkap"
        self.create_header(title, subtitle)
        self.create_form()
        
        if self.is_edit:
            self.load_client_data()
    
    def create_form(self):
        """Create professional form fields"""
        container = ctk.CTkFrame(self, fg_color=Colors.APP_BG)
        container.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Scrollable form
        scroll_frame = ctk.CTkScrollableFrame(
            container,
            fg_color=Colors.APP_BG,
            label_text="",
            label_font=("", 0)
        )
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Form card
        form_frame = ctk.CTkFrame(
            scroll_frame,
            fg_color=Colors.CARD_BG,
            corner_radius=IslamicTheme.CORNER_RADIUS,
            border_width=1,
            border_color=Colors.BORDER_COLOR
        )
        form_frame.pack(fill="x", padx=0, pady=0)
        
        # Form content
        content = ctk.CTkFrame(form_frame, fg_color=Colors.CARD_BG)
        content.pack(fill="both", padx=IslamicTheme.PADDING_LARGE, pady=IslamicTheme.PADDING_LARGE)
        
        # Form fields
        self.form_fields = {}
        
        fields = [
            ('name', '👤 Nama Klien', True),
            ('phone', '📱 Nomor Telepon', False),
            ('email', '✉️ Email', False),
            ('address', '🏠 Alamat', False),
            ('company', '🏢 Nama Perusahaan', False),
            ('industry', '🏭 Industri', False),
        ]
        
        for field_name, label_text, required in fields:
            self.create_form_field(content, field_name, label_text, required)
        
        # Status field
        label = ctk.CTkLabel(
            content,
            text="📊 Status Klien",
            font=IslamicTheme.FONT_LABEL,
            text_color=Colors.TEXT_PRIMARY
        )
        label.pack(anchor="w", pady=(20, 5))
        
        self.status_combo = ctk.CTkComboBox(
            content,
            values=["active", "inactive", "pending"],
            height=40,
            font=IslamicTheme.FONT_TEXT,
            fg_color="#f9f9f9",
            border_color=Colors.SIDEBAR_HOVER
        )
        self.status_combo.set("active")
        self.status_combo.pack(fill="x", pady=(0, 25))
        
        # Buttons
        button_frame = ctk.CTkFrame(content, fg_color=Colors.CARD_BG)
        button_frame.pack(fill="x", pady=(20, 0))
        
        save_btn = ctk.CTkButton(
            button_frame,
            text="💾 Simpan",
            command=self.save_client,
            fg_color=Colors.SUCCESS,
            hover_color="#059669",
            font=IslamicTheme.FONT_LABEL,
            height=45,
            width=150
        )
        save_btn.pack(side="left", padx=10)
        
        cancel_btn = ctk.CTkButton(
            button_frame,
            text="❌ Batal",
            command=self.on_save,
            fg_color=Colors.TEXT_SECONDARY,
            hover_color="#4b5563",
            font=IslamicTheme.FONT_LABEL,
            height=45,
            width=150
        )
        cancel_btn.pack(side="left", padx=10)
    
    def create_form_field(self, parent, field_name, label_text, required):
        """Create individual form field"""
        label = ctk.CTkLabel(
            parent,
            text=label_text,
            font=IslamicTheme.FONT_LABEL,
            text_color=Colors.TEXT_PRIMARY
        )
        label.pack(anchor="w", pady=(15, 5))
        
        entry = ctk.CTkEntry(
            parent,
            height=40,
            font=IslamicTheme.FONT_TEXT,
            fg_color="#f9f9f9",
            border_color=Colors.SIDEBAR_HOVER
        )
        entry.pack(fill="x", pady=(0, 3))
        
        if required:
            req_label = ctk.CTkLabel(
                parent,
                text="* Wajib diisi",
                font=IslamicTheme.FONT_SMALL,
                text_color=Colors.DANGER
            )
            req_label.pack(anchor="w", pady=(0, 10))
        
        self.form_fields[field_name] = entry
    
    def load_client_data(self):
        """Load client data for editing"""
        try:
            client = self.client_model.get_by_id(self.client_id)
            if client:
                self.form_fields['name'].insert(0, client['name'])
                self.form_fields['phone'].insert(0, client['phone'] or '')
                self.form_fields['email'].insert(0, client['email'] or '')
                self.form_fields['address'].insert(0, client['address'] or '')
                self.form_fields['company'].insert(0, client['company'] or '')
                self.form_fields['industry'].insert(0, client['industry'] or '')
                self.status_combo.set(client['status'])
        except Exception as e:
            self.show_error(f"Error loading client data: {str(e)}")
    
    def save_client(self):
        """Save client to database"""
        try:
            name = self.form_fields['name'].get().strip()
            if not name:
                self.show_error("❌ Nama klien tidak boleh kosong!")
                return
            
            # Email validation
            email = self.form_fields['email'].get().strip()
            if email and '@' not in email:
                self.show_error("❌ Format email tidak valid!")
                return
            
            # Phone validation
            phone = self.form_fields['phone'].get().strip()
            if phone and len(phone.replace('-', '').replace(' ', '')) < 10:
                self.show_error("❌ Nomor telepon minimal 10 digit!")
                return
            
            data = {
                'name': name,
                'phone': phone or None,
                'email': email or None,
                'address': self.form_fields['address'].get().strip() or None,
                'company': self.form_fields['company'].get().strip() or None,
                'industry': self.form_fields['industry'].get().strip() or None,
                'status': self.status_combo.get()
            }
            
            if self.is_edit:
                self.client_model.update(self.client_id, **data)
                self.show_info("✅ Data klien berhasil diperbarui")
            else:
                self.client_model.create(**data)
                self.show_info("✅ Klien baru berhasil ditambahkan")
            
            if self.on_save:
                self.on_save()
        
        except Exception as e:
            self.show_error(f"❌ Error menyimpan data: {str(e)}")
    
    def clear_form(self):
        """Clear all form fields"""
        for entry in self.form_fields.values():
            entry.delete(0, "end")
        self.status_combo.set("active")

