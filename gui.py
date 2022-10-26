from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk
from ttkthemes import ThemedTk
from turtle import color


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_info():
    messagebox.showinfo('FAQ', 'Project made for BDII\n\n Members:\n  > Mariano Sanchez Toledo\n  > Agustín Montaña\n  > Bruno Orbelli\n  > Mauro Sarmiento\n\n 2022')

window = ThemedTk(theme='breeze')

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    360.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    640.0,
    427.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    640.0,
    354.0,
    image=image_image_3
)

style= ttk.Style()
style.theme_use('breeze')
style.configure("TCombobox", background= "#5E548E")

combo = ttk.Combobox(
    state="readonly",
    values=["Pelicula", "Actor", "Director"],
    justify='center',
    font=('Nunito', 12),
)
combo.set("Filter")
combo.place(
    x=50, 
    y=103,
    height=38,
    width=160
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_info(),
    relief="flat"
)
button_1.place(
    x=1198.0,
    y=20.0,
    width=50.0,
    height=49.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    660.0,
    124.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font= ('Nunito', 12)
)
entry_1.place(
    x=245.0,
    y=103.0,
    width=830.0,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1096.0,
    y=102.0,
    width=159.0,
    height=41.0
)

# Creación Treeview
tree_frame = Frame(window)
tree_frame.place(x = 120, y= 165)
tree_frame.config(bg='white')

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tv = ttk.Treeview(tree_frame, columns=('tittle', 'released', 'runtime', 'genre', 'director'), height= 23, yscrollcommand=tree_scroll.set)

tv.column('#0', width=0, stretch=NO)
tv.column('tittle', width=250, minwidth=200,anchor=CENTER)
tv.column('released', width=170, minwidth=150,anchor=CENTER)
tv.column('runtime', width=170, minwidth=100,anchor=CENTER)
tv.column('genre', width=180, minwidth=100,anchor=CENTER)
tv.column('director', width=230, minwidth=200,anchor=CENTER)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('tittle',text='Tittle', anchor=CENTER)
tv.heading('released',text='Released', anchor=CENTER)
tv.heading('runtime',text='Runtime', anchor=CENTER)
tv.heading('genre',text='Genre', anchor=CENTER)
tv.heading('director',text='Director', anchor=CENTER)

tv.pack()

tree_scroll.config(command=tv.yview)

window.resizable(False, False)
window.mainloop()
