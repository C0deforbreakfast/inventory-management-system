from tkinter import *


class ShowMessage:
    def __init__(self):
        pass
        
    def run(self, message):
        root = Tk()

        # specify size of window.
        root.geometry("250x75")


        # Create label
        l = Label(root, text = message)
        l.config(font =("YanoneKaffeesatz Regular", 15 * -1))

        # Create an Exit button.
        b2 = Button(root, text = "Exit",
                    command = root.destroy) 

        l.pack()
        b2.pack()

        root.mainloop()

