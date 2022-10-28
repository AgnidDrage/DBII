from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk
from ttkthemes import ThemedTk
from turtle import color
from mongoServices import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_info():
    messagebox.showinfo('FAQ', 'Project made for BDII\n\n Members:\n  > Mariano Sanchez Toledo\n  > Agustín Montaña\n  > Bruno Orbelli\n  > Mauro Sarmiento\n\n 2022')

def generate_table():
    table0 = [] # La tabla table0 se conserva para control

    for i in tv.get_children(): # Reinicia los datos de la tabla despues de cada envio de datos
        tv.delete(i)
    for i in range(0):
        table0.append()
        tv.insert('',END,text=str(i),values=()) # Se insertan los datos de la tabla de resultados en la primer tabla

    len_cols = len() # Cantidad de columnas
    cols = []

    for i in range(len_cols): # Agrega la cantidad de columnas a una lista cols que les asigna un ID a cada columna
        cols.append(i)
    cols.pop()

    tv2 = ttk.Treeview(window,columns=cols,height=8) # Agrega las columnas reconocidas a la tabla en forma dinamica
    tv2.column('#0', width=80) # Se le asigna formato a la primer columna
    for i in range(len(cols)): # Se les asigna formato al resto de columnas
        tv2.column(i, width=80)
    tv2.place(x=50,y=750) # Se posiciona la tercer tabla

    values_gen = [] # Lista de valores a posicionar en la tabla

    for i in range(): # Se rellenan los datos de la tabla
        for l in range(len(cols)):
            values_gen.append()
        tv2.insert('',i, text='' ,values=values_gen)
        for j in range(len(cols)):
            values_gen.pop()

def showTitle():
    title = entry_1.get()
    dataList = searchTitle(title)
    for i in tv.get_children():
        tv.delete(i)
        
    count = 0
    if len(dataList) != 0:
        for row in dataList:
            tv.insert(parent='', index='end', iid=count, text ='', values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            count += 1
    else:
        messagebox.showinfo('Error', 'No se encontraron resultados')

def showTitleEnter(event):
    showTitle()

def getRow(event):
    selected = tv.focus()
    values = tv.item(selected, 'values')

    top = Toplevel()
    top.geometry('700x600')
    top.iconbitmap('./assets/movie_ico.ico')
    top.title(values[0] + ' Datasheet')

    canvasTop = Canvas(
        top,
        bg = "#FFFFFF",
        height = 600,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvasTop.pack()

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvasTop.create_image(
        350.0,
        300.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvasTop.create_image(
        257.0,
        475.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvasTop.create_image(
        349.0,
        298.0,
        image=image_image_6
    )

    label_1 = ttk.Label(
        top,
        background='#FFFFFF',
        font='Nunito 12',
        text=values[0] # Title
    )
    
    label_1.place(
        x=165, 
        y=38,
        width=495.0,
        height=38.0
        )

    label_2 = ttk.Label(
        top,
        background='#FFFFFF',
        font='Nunito 12',
        text=values[4] # Director
    )
    
    label_2.place(
        x=165, 
        y=348,
        width=495.0,
        height=38.0
        )

    label_3 = ttk.Label(
        top,
        background='#FFFFFF',
        font='Nunito 12',
        text=values[1] # Released
    )
    
    label_3.place(
        x=165, 
        y=92,
        width=188.0,
        height=38.0
        )

    label_4 = ttk.Label(
        top,
        background='#FFFFFF',
        font='Nunito 12',
        text=values[5] # Rating
    )
    
    label_4.place(
        x=165, 
        y=525,
        width=140.0,
        height=35.0
        )

    label_5 = ttk.Label(
        top,
        background='#FFFFFF',
        font='Nunito 12',
        text='#VALUE#' # Country
    )
    
    label_5.place(
        x=435, 
        y=523,
        width=200.0,
        height=35.0
        )

    label_5 = ttk.Label(
        top,
        background='#FFFFFF',
        font='Nunito 12',
        text=values[2] # Runtime
    )
    
    label_5.place(
        x=490, 
        y=92,
        width=155.0,
        height=38.0
        )
    
    top.mainloop()

window = ThemedTk(theme='breeze')

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")
window.title('The Film Library - 2022')
window.iconbitmap('./assets/movie_ico.ico')

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
combo.set("Pelicula")
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
    command=lambda: showTitle(),
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

tv = ttk.Treeview(tree_frame, columns=('tittle', 'released', 'runtime', 'genre', 'director', 'rating'), height= 23, yscrollcommand=tree_scroll.set)

tv.column('#0', width=0, stretch=NO)
tv.column('tittle', width=230, minwidth=200,anchor=CENTER)
tv.column('released', width=150, minwidth=150,anchor=CENTER)
tv.column('runtime', width=150, minwidth=100,anchor=CENTER)
tv.column('genre', width=160, minwidth=100,anchor=CENTER)
tv.column('director', width=220, minwidth=200,anchor=CENTER)
tv.column('rating', width=90, minwidth=80,anchor=CENTER)

tv.heading('#0', text='', anchor=CENTER)
tv.heading('tittle',text='Tittle', anchor=CENTER)
tv.heading('released',text='Released', anchor=CENTER)
tv.heading('runtime',text='Runtime', anchor=CENTER)
tv.heading('genre',text='Genre', anchor=CENTER)
tv.heading('director',text='Director', anchor=CENTER)
tv.heading('rating',text='Rating', anchor=CENTER)

tv.pack()

tv.bind("<Double-1>", getRow)
entry_1.bind("<Return>", showTitleEnter)

tree_scroll.config(command=tv.yview)

window.resizable(False, False)
window.mainloop()
