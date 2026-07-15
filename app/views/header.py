def create_header(self):

    header = ctk.CTkFrame(

        self,

        height=70,

        fg_color="#0B7A3B"

    )

    header.grid(

        row=0,

        column=0,

        columnspan=2,

        sticky="nsew"

    )

    title = ctk.CTkLabel(

        header,

        text="HCMS - Halal Consultant Management System",

        font=("Segoe UI",22,"bold"),

        text_color="white"

    )

    title.pack(pady=20)
    return header
    import customtkinter as ctk

class Header(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=70, fg_color="#0B7A3B")

        self.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            self,
            text="HCMS - Halal Consultant Management System",
            font=("Segoe UI", 22, "bold"),
            text_color="white"
        )

        title.pack(pady=18)