from tkinter import Entry, Tk, Label, Frame, Button
from PIL import Image, ImageTk, ImageDraw, ImageFont
import numpy as np

class app:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("720x480")
        self.root.title("TOKI PONA Daily")
        font = ("sans serif", 25)
        Label(self.root, font=font, text="TOKI Pona").grid(row=0)
        Label(self.root, text="Description").grid(row=1)
        self.toky_entry = Entry(font=font)
        self.toky_entry.grid(row=0, column=1)

        self.desc_entry = Entry(font=font)
        self.desc_entry.grid(row=1, column=1)

        self.generate_button = Button(
            command=self.generate, 
            text="Generate").grid(row=3, column=1)
       
        
        self.main_frame  = Frame(self.root, width=300, height=300).grid(row=3, padx=30, pady=30)
        self.root.mainloop()

    def generate(self):
        color = tuple(np.random.choice(range(256), size=3))
        color2 = tuple(np.random.choice(range(256), size=3))
        color3 = tuple(np.random.choice(range(256), size=3))
        first = Image.new("RGB", (300, 300), color)
        second = Image.new("RGB", (270,270), color2)
        third = Image.new("RGB", (250, 130), color3)
        draw = ImageDraw.Draw(second)
        draw2 = ImageDraw.Draw(third)
        font = ImageFont.truetype("HELVETICA.TTF", 30)
        font2 = ImageFont.truetype("sitelen-pona-pona.otf", 130)
        desc = self.desc_entry.get()
        toki = self.toky_entry.get()
        draw.text(((270 - font.getlength(desc)) / 2, 197.5-15), desc,(0,0,0), font=font)
        draw2.text(((250 - font.getlength(toki))/ 2, -15), toki, (0, 0, 0), font=font2, features="liga")
        second.paste(third, (10, 10))
        first.paste(second, (15, 15))
        self.generate_image = first
        self.generate_image.save("./image.png")
        self.tkImage = ImageTk.PhotoImage(self.generate_image)
        Label(self.main_frame,image=self.tkImage).grid(row=3, sticky="n")



       

if __name__ == "__main__":
    app = app()