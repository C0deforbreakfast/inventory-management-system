from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from backend import Main


class SearchStorage:
    def __init__(self):
        OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Martin\Desktop\Database\assets\frame5")

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def run(self, win):
        window = win

        window.geometry("340x410")
        window.configure(bg = "#141A29")

        canvas = Canvas(
            window,
            bg = '#141A29',
            height = 410,
            width = 340,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge" 
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            master=canvas,
            name='img1',
            file=self.relative_to_assets("image_1.png")
        )
        image_1 = canvas.create_image(
            170.0,
            233.0,
            image=image_image_1
        )

        canvas.create_text(
            13.0,
            20.0,
            anchor="nw",
            text="Search for products",
            fill='#FFFFFF',
            font=("YanoneKaffeesatz Regular", 20 * -1)
        )

        canvas.create_text(
            26.0,
            102.0,
            anchor="nw",
            text="Record Id: ",
            fill="#000000",
            font=("YanoneKaffeesatz Regular", 16 * -1)
        )

        entry_image_1 = PhotoImage(
            master=canvas,
            name='ent3',
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            166.5,
            144.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#999B9F",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=31.0,
            y=122.0,
            width=271.0,
            height=43.0
        )

        button_image_1 = PhotoImage(
            master=canvas,
            name="btn9",
            file=self.relative_to_assets("button_1.png")
        )
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.search(entry_1.get()),
            relief="flat"
        )
        button_1.place(
            x=83.0,
            y=345.0,
            width=147.0,
            height=41.0
        )

        window.resizable(False, False)
        window.mainloop()

    def search(self, id: int):
        Main().search_storage(id=id)


if __name__ == '__main__':
    sp = SearchStorage()
    sp.run()