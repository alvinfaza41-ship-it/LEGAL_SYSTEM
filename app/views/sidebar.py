def create_sidebar(self):

    sidebar = ctk.CTkFrame(

        self,

        width=250,

        fg_color="#2F3542"

    )

    sidebar.grid(

        row=1,

        column=0,

        sticky="nsew"

    )

    menu = [

        "Dashboard",

        "Client",

        "Produk",

        "Legalitas",

        "Invoice",

        "Surat",

        "Laporan",

        "Pengaturan"

    ]

    for item in menu:

        btn = ctk.CTkButton(

            sidebar,

            text=item

        )

        btn.pack(

            fill="x",

            padx=10,

            pady=5

        )
    return sidebar
    import customtkinter as ctk

class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=250)

        menu = [
            "Dashboard",
            "Client",
            "Produk",
            "Legalitas",
            "Invoice",
            "Surat",
            "Laporan",
            "Pengaturan"
        ]

        for item in menu:

            btn = ctk.CTkButton(self, text=item)

            btn.pack(fill="x", padx=10, pady=5)