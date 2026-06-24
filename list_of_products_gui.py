from tkinter import *
from backend import Main


class ListOfProducts:
    def __init__(self):
        pass

    def run(self):
        lst = Main().list_of_products()
        root = Tk()
        total_rows = len(lst)
        total_columns = len(lst[0])
        
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                
                self.e = Entry(root, width=20, fg='black',
                            font=('YanoneKaffeesatz Regular',16 * -1))
                
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

        root.mainloop()
    
