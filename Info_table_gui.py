from tkinter import *


class InfoTable:
    def __init__(self):
        pass

    def run(self, list):
        lst = list
        root = Tk()
        if lst != None:
            total_rows = len(lst)
            total_columns = len(lst[0])
        else:
            total_rows = 0
            total_columns = 0
        
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                
                self.e = Entry(root, width=20, fg='black',
                            font=('YanoneKaffeesatz Regular',16 * -1))
                
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

        root.mainloop()