import customtkinter as ctk
from app.themes.islamic_theme import IslamicTheme, Colors


class BaseFrame(ctk.CTkFrame):
    """Base frame class untuk semua pages"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent
        self.configure(fg_color=Colors.APP_BG)
    
    def create_header(self, title, subtitle=None):
        """Create professional header with Islamic theme"""
        header = ctk.CTkFrame(
            self,
            fg_color=Colors.HEADER_BG,
            height=80,
            corner_radius=0
        )
        header.pack(fill="x", padx=0, pady=0)
        
        # Content frame inside header
        header_content = ctk.CTkFrame(header, fg_color=Colors.HEADER_BG)
        header_content.pack(fill="both", expand=True, padx=IslamicTheme.PADDING_LARGE, pady=15)
        
        # Main title
        title_label = ctk.CTkLabel(
            header_content,
            text=f"📍 {title}",
            font=IslamicTheme.FONT_SUBHEADING,
            text_color=Colors.HEADER_TEXT
        )
        title_label.pack(anchor="w")
        
        # Subtitle if provided
        if subtitle:
            subtitle_label = ctk.CTkLabel(
                header_content,
                text=subtitle,
                font=IslamicTheme.FONT_SMALL,
                text_color="#d4af37"
            )
            subtitle_label.pack(anchor="w", pady=(2, 0))
        
        # Bottom decorative line
        separator = ctk.CTkFrame(header, fg_color=Colors.SIDEBAR_ACTIVE, height=2)
        separator.pack(fill="x", padx=0, pady=0)
        
        return header
    
    def create_card(self, parent, title=None, content_frame=None):
        """Create professional card with Islamic theme"""
        card = ctk.CTkFrame(
            parent,
            fg_color=Colors.CARD_BG,
            corner_radius=IslamicTheme.CORNER_RADIUS,
            border_width=1,
            border_color=Colors.CARD_BORDER
        )
        
        if title:
            title_label = ctk.CTkLabel(
                card,
                text=title,
                font=IslamicTheme.FONT_LABEL,
                text_color=Colors.TEXT_PRIMARY
            )
            title_label.pack(fill="x", padx=IslamicTheme.PADDING_MEDIUM, pady=(IslamicTheme.PADDING_MEDIUM, 10))
            
            divider = ctk.CTkFrame(card, fg_color=Colors.SIDEBAR_ACTIVE, height=1)
            divider.pack(fill="x", padx=IslamicTheme.PADDING_MEDIUM)
        
        if content_frame:
            content_frame.pack(fill="both", expand=True)
        
        return card
    
    def create_stat_card(self, value, label, icon, color=None):
        """Create beautiful stat card"""
        card = ctk.CTkFrame(
            None,
            fg_color=Colors.CARD_BG,
            corner_radius=IslamicTheme.CORNER_RADIUS,
            border_width=2,
            border_color=color or Colors.SIDEBAR_HOVER
        )
        
        # Icon & Value
        top_frame = ctk.CTkFrame(card, fg_color=Colors.CARD_BG)
        top_frame.pack(fill="x", padx=IslamicTheme.PADDING_MEDIUM, pady=IslamicTheme.PADDING_MEDIUM)
        
        icon_label = ctk.CTkLabel(
            top_frame,
            text=icon,
            font=("Segoe UI", 32),
            text_color=color or Colors.SIDEBAR_HOVER
        )
        icon_label.pack(side="left", padx=(0, 10))
        
        value_label = ctk.CTkLabel(
            top_frame,
            text=str(value),
            font=("Segoe UI", 28, "bold"),
            text_color=color or Colors.SIDEBAR_HOVER
        )
        value_label.pack(side="left", anchor="n")
        
        # Label
        label_text = ctk.CTkLabel(
            card,
            text=label,
            font=IslamicTheme.FONT_LABEL,
            text_color=Colors.TEXT_SECONDARY
        )
        label_text.pack(anchor="w", padx=IslamicTheme.PADDING_MEDIUM, pady=(0, IslamicTheme.PADDING_MEDIUM))
        
        return card
    
    def show_info(self, message, title="✅ Sukses"):
        """Show info dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title(title)
        dialog.geometry("350x150")
        dialog.resizable(False, False)
        dialog.configure(fg_color=Colors.APP_BG)
        
        label = ctk.CTkLabel(
            dialog,
            text=message,
            wraplength=320,
            font=IslamicTheme.FONT_TEXT,
            text_color=Colors.TEXT_PRIMARY
        )
        label.pack(pady=20)
        
        btn = ctk.CTkButton(
            dialog,
            text="OK",
            command=dialog.destroy,
            fg_color=Colors.BTN_PRIMARY_BG,
            hover_color=Colors.BTN_PRIMARY_HOVER,
            font=IslamicTheme.FONT_LABEL,
            height=35,
            width=100
        )
        btn.pack(pady=10)
    
    def show_error(self, message, title="❌ Terjadi Kesalahan"):
        """Show error dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title(title)
        dialog.geometry("350x150")
        dialog.resizable(False, False)
        dialog.configure(fg_color=Colors.APP_BG)
        
        label = ctk.CTkLabel(
            dialog,
            text=message,
            wraplength=320,
            font=IslamicTheme.FONT_TEXT,
            text_color=Colors.DANGER
        )
        label.pack(pady=20)
        
        btn = ctk.CTkButton(
            dialog,
            text="OK",
            command=dialog.destroy,
            fg_color=Colors.BTN_DANGER_BG,
            hover_color="#dc2626",
            font=IslamicTheme.FONT_LABEL,
            height=35,
            width=100
        )
        btn.pack(pady=10)

