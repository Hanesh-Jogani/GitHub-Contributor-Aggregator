from tkinter import *
from main import *

class Result(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("600x350+250+130")
        self.title("Repository Details")
        self.resizable(False, False)

        # frames
        self.top = Frame(self, height=150, bg="white")
        self.top.pack(fill=X)
        self.bottom = Frame(self, height=500, bg="#6574BB")
        self.bottom.pack(fill=X)

        # top frame design
        self.invite = Label(self.top, text="Repository Details", font="arial 15 bold", bg="white", fg="#281E5D")
        self.invite.place(x=200, y=50)

        # self.label  = Label(self.top, text = (list(Output_Json.keys())[0]) )
        # self.label.place(x=200, y=90)

        f1 = Frame(self.bottom)
        f1.pack(fill="y")

        for row in range(len(Output_Json)+1):
            for column in range(3):
                if row == 0 and column == 0:
                    label = Label(f1, text="Company Name", padx=3, pady=3, bg="#6574BB", fg="white")
                    label.config(font=('Arial', 12))
                    label.grid(row=row, column=column, sticky="nsew", padx=3, pady=3)
                    f1.grid_columnconfigure(column, weight=1)

                elif row == 0 and column == 1:
                    label = Label(f1, text="Total Contribution", padx=3, pady=3, bg="#6574BB", fg="white")
                    label.config(font=('Arial', 12))
                    label.grid(row=row, column=column, sticky="nsew", padx=3, pady=3)
                    f1.grid_columnconfigure(column, weight=1)

                elif row == 0 and column == 2:
                    label = Label(f1, text="Unique Contributions", padx=3, pady=3, bg="#6574BB", fg="white")
                    label.config(font=('Arial', 12))
                    label.grid(row=row, column=column, sticky="nsew", padx=3, pady=3)
                    f1.grid_columnconfigure(column, weight=1)

                elif column == 0:
                    label = Label(f1, text=list(Output_Json.keys())[row-1], padx=3, pady=3, bg="#6574BB", fg="white")
                    label.config(font=('Arial', 12))
                    label.grid(row=row, column=column, sticky="nsew", padx=3, pady=3)
                    f1.grid_columnconfigure(column, weight=1)

                elif column == 1:
                    label = Label(f1, text=Output_Json[list(Output_Json.keys())[row-1]]['Total Contributions'], padx=3, pady=3, bg="#6574BB", fg="white")
                    label.config(font=('Arial', 12))
                    label.grid(row=row, column=column, sticky="nsew", padx=3, pady=3)
                    f1.grid_columnconfigure(column, weight=1)

                elif column == 2:
                    label = Label(f1, text=Output_Json[list(Output_Json.keys())[row-1]]['Unique Contributors'], padx=3, pady=3, bg="#6574BB", fg="white")
                    label.config(font=('Arial', 12))
                    label.grid(row=row, column=column, sticky="nsew", padx=3, pady=3)
                    f1.grid_columnconfigure(column, weight=1)

                else:
                    label = Label(f1, text="Row : " + str(row) + " , Column : " + str(column), bg="#6574BB", fg="white")
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    f1.grid_columnconfigure(column, weight=1)
