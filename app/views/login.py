def __init__(self, *args, **kwargs):

    super().__init__(*args, **kwargs)
    self.create_content()


def create_content(self):

    self.content = ctk.CTkFrame(

        self,

        fg_color="white"

    )

    self.content.grid(

        row=1,

        column=1,

        sticky="nsew"

    )

    label = ctk.CTkLabel(

        self.content,

        text="Selamat Datang di HCMS",

        font=("Segoe UI",26,"bold")

    )

    label.pack(

        pady=50

    )