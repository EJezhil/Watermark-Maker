import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

bg_img_path = None
logo_img_path = None

path = os.getenv('PATH')

path = rf'{path}'

def watermark():
    logo_img = Image.open(logo_img_path).convert("RGBA")
    bg_img = Image.open(bg_img_path).convert("RGBA")

    logo_width, logo_height = logo_img.size
    bg_width, bg_height = bg_img.size
    logo_img = logo_img.resize((int(bg_width / 7), int(bg_height / 7)))

    logo_x = bg_img.width - logo_img.width - 5
    logo_y = bg_img.height - logo_img.height - 5
    bg_img.paste(logo_img, (logo_x, logo_y), mask=logo_img)
    bg_img.show()
    bg_img.save(fp=path, format="PNG")


def open_bg_img():
    global bg_img_path
    bg_img_path = filedialog.askopenfilename()


def open_logo_img():
    global logo_img_path
    logo_img_path = filedialog.askopenfilename()


screen = tk.Tk()
screen.title("Watermark Desktop GUI APP")
screen.geometry('1000x400')
screen.config(bg="lightblue", padx=300, pady=60)

lable = tk.Label(text="Welcome to Watermark image maker", font=("Arial", 16))
lable.grid_configure(row=2, column=2)

bg = tk.Button(text="Select Background Image", command=open_bg_img)
bg.grid_configure(row=4, column=2)

logo_pic = tk.Button(text="Select Logo Image", command=open_logo_img)
logo_pic.grid_configure(row=6, column=2)

show_wm_pic = tk.Button(text="Show Watermark Image", command=watermark)
show_wm_pic.grid_configure(row=8, column=2)

screen.mainloop()
