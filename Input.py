from tkinter import *
import datetime
from Result import *
from main import *

date = str(datetime.datetime.now().date())

class Application(object):

    def result(self):
        result = Result()

    def __init__(self, root):
        self.root = root
        # frames
        self.top = Frame(root, height=150, bg="#FFFFFF")
        self.top.pack(fill=X)
        self.bottom = Frame(root, height=500, bg="#6574BB")
        self.bottom.pack(fill=X)

        # top frame design
        self.image = PhotoImage(file="git.png")
        self.image_label = Label(self.top, image=self.image, bg="#FFFFFF", height=100)
        self.image_label.place(x=100, y=22)

        self.invite = Label(self.top, text="Welcome to GitHub Aggregator", font="arial 15 bold", bg="#FFFFFF", fg="#281E5D")
        self.invite.place(x=200, y=60)

        self.date = Label(self.top, text=date, font="arial 10", bg="#FFFFFF", fg="#281E5D")
        self.date.place(x=600, y=17)

        # bottom frame design
        self.repolabel = Label(self.bottom, text="Repository Name", bg="#6574BB", fg="white", font="Serif 14")
        self.repolabel.place(x=150, y=50)

        self.repoinput = Entry(self.bottom, width=30)
        self.repoinput.place(x=330, y=55)

        self.sdatelabel = Label(self.bottom, text="Start Date Range", bg="#6574BB", fg="white", font="Serif 14")
        self.sdatelabel.place(x=150, y=90)

        self.sdateinput = Entry(self.bottom, width=30)

        # self.sdateinput.insert(0, 'DD-MM-YY')
        self.sdateinput.place(x=330, y=95)

        self.edatelabel = Label(self.bottom, text="End Date Range", bg="#6574BB", fg="white", font="Serif 14")
        self.edatelabel.place(x=150, y=130)

        self.edateinput = Entry(self.bottom, width=30)
        self.edateinput.place(x=330, y=135)

        self.search = Button(self.bottom, text="  Search  ", font="arial 13", bg="#FF6347", fg="white", command=self.result)
        self.search.place(x=310, y=180)

def main():
    box = Tk()
    app = Application(box)
    box.title("GitHub Aggregator by Maniac")
    box.geometry("700x400+200+100")
    box.resizable(False, False)
    box.mainloop()

if __name__ == '__main__':
    main()