"""
Islamic Theme Configuration
Professional color scheme dengan sentuhan Islami
"""


class IslamicTheme:
    """Theme configuration untuk HCMS dengan sentuhan Islami"""
    
    # Primary Colors - Warna Hijau & Biru Islami
    PRIMARY_GREEN = "#1a5a3f"      # Hijau tua Islami
    PRIMARY_GREEN_LIGHT = "#2d8659" # Hijau cerah
    PRIMARY_BLUE = "#0f4c75"        # Biru Islami
    SECONDARY_GOLD = "#d4af37"      # Emas - Aksent
    
    # Neutral Colors
    DARK_BG = "#0f1419"            # Background gelap
    LIGHT_BG = "#f5f3f0"           # Background terang (warm)
    CARD_BG = "#ffffff"            # Card background
    TEXT_PRIMARY = "#1a1a1a"       # Text gelap
    TEXT_SECONDARY = "#64748b"     # Text abu
    BORDER_COLOR = "#e8e8e8"       # Border line
    
    # Status Colors
    SUCCESS = "#10b981"            # Hijau success
    WARNING = "#f97316"            # Orange warning
    DANGER = "#ef4444"             # Red danger
    INFO = "#06b6d4"               # Cyan info
    
    # Hover/Active States
    HOVER_GREEN = "#0f4c75"
    ACTIVE_GREEN = "#d4af37"
    
    # Fonts
    FONT_TITLE = ("Segoe UI", 32, "bold")
    FONT_HEADING = ("Segoe UI", 24, "bold")
    FONT_SUBHEADING = ("Segoe UI", 18, "bold")
    FONT_LABEL = ("Segoe UI", 12, "bold")
    FONT_TEXT = ("Segoe UI", 11)
    FONT_SMALL = ("Segoe UI", 10)
    
    # Padding & Spacing
    PADDING_LARGE = 30
    PADDING_MEDIUM = 20
    PADDING_SMALL = 10
    
    # Border Radius
    CORNER_RADIUS = 12
    CORNER_RADIUS_SMALL = 6


class Colors:
    """Convenient color access"""
    
    # Sidebar
    SIDEBAR_BG = IslamicTheme.PRIMARY_BLUE
    SIDEBAR_TEXT = "#ffffff"
    SIDEBAR_HOVER = IslamicTheme.PRIMARY_GREEN
    SIDEBAR_ACTIVE = IslamicTheme.SECONDARY_GOLD
    
    # Header
    HEADER_BG = IslamicTheme.PRIMARY_GREEN
    HEADER_TEXT = "#ffffff"
    
    # Cards
    CARD_BG = IslamicTheme.CARD_BG
    CARD_BORDER = IslamicTheme.BORDER_COLOR
    
    # Buttons
    BTN_PRIMARY_BG = IslamicTheme.PRIMARY_GREEN
    BTN_PRIMARY_HOVER = IslamicTheme.PRIMARY_GREEN_LIGHT
    BTN_SUCCESS_BG = IslamicTheme.SUCCESS
    BTN_DANGER_BG = IslamicTheme.DANGER
    
    # Text
    TEXT_PRIMARY = IslamicTheme.TEXT_PRIMARY
    TEXT_SECONDARY = IslamicTheme.TEXT_SECONDARY
    
    # Background
    APP_BG = IslamicTheme.LIGHT_BG
    

def get_card_style(status=None):
    """Get style dict for status-based cards"""
    if status == "active":
        return {"fg_color": "#ecfdf5", "border_color": IslamicTheme.SUCCESS}
    elif status == "warning":
        return {"fg_color": "#fffbeb", "border_color": IslamicTheme.WARNING}
    elif status == "error":
        return {"fg_color": "#fef2f2", "border_color": IslamicTheme.DANGER}
    return {"fg_color": IslamicTheme.CARD_BG, "border_color": IslamicTheme.BORDER_COLOR}


# Islamic Decorative Patterns (ASCII art for UI)
ISLAMIC_PATTERNS = {
    "top_border": "✦ ✦ ✦",
    "bottom_border": "✦ ✦ ✦",
    "divider": "━" * 50,
}
