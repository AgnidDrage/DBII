from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk
from ttkthemes import ThemedTk
from turtle import bgcolor, color, width
from mongoServices import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_info():
    messagebox.showinfo('FAQ', 'Project made for BDII\n\n Members:\n  > Mariano Sanchez Toledo\n  > Agustín Montaña\n  > Bruno Orbelli\n  > Mauro Sarmiento\n\n 2022')

def showTitle():
    global fullData
    title = entry_1.get()
    dataList, fullData = searchTitle(title)
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
    values = fullData[int(selected)]

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

    label_2 = Button(
        top,
        activebackground='#FFFFFF',
        bg='#FFFFFF',
        font='Nunito 12',
        anchor='w',
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        text=(values[5]["full-name"] if values[5] != "N/A" else "N/A") # Director
    )
    
    label_2.place(
        x=165, 
        y=348,
        width=493.0,
        height=38.0
        )

    label_3 = ttk.Label(
        top,
        background='#FFFFFF',
        font='Nunito 12',
        text=values[2] # Released
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
        text=values[9] # Rating
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
        text=values[8] # Country
    )
    
    label_5.place(
        x=435, 
        y=523,
        width=200.0,
        height=35.0
        )

    label_6 = ttk.Label(
        top,
        background='#FFFFFF',
        font='Nunito 12',
        text=values[3] # Runtime
    )
    
    label_6.place(
        x=490, 
        y=92,
        width=155.0,
        height=38.0
        )
    
    label_7 = ttk.Label(
        top,
        background='#FFFFFF',
        font='Nunito 12',
        wraplength=483,
        justify='left',
        text=values[7] # Plot
    )
    
    label_7.place(
        x=165, 
        y=400,
        width=483.0,
        height=110.0
        )

    # Creación Treeview Genres
    tree_frame_genres = Frame(top)
    tree_frame_genres.place(x = 160, y= 145)
    tree_frame_genres.config(bg='white')

    tree_scroll_genres = Scrollbar(tree_frame_genres)
    tree_scroll_genres.pack(side=RIGHT, fill=Y)

    tv_genres = ttk.Treeview(tree_frame_genres, columns=('genre'), show='tree', height= 2, yscrollcommand=tree_scroll_genres.set)

    tv_genres.column('#0', width=0, stretch=NO)
    tv_genres.column('genre', width=450, minwidth=450,anchor=CENTER)

    tv_genres.heading('#0', text='', anchor=CENTER)
    tv_genres.heading('genre',text='Genre', anchor=CENTER)

    tv_genres.pack()

    for i in tv_genres.get_children():
        tv_genres.delete(i)

    countG = 0
    genre_list = [[i['name']] for i in values[4]]
    for row in genre_list:
        tv_genres.insert(parent='', index='end', iid=countG, text ='', values=(row[0]))
        countG += 1

    # Creación Treeview Actors
    tree_frame_actors = Frame(top)
    tree_frame_actors.place(x = 160, y= 235)
    tree_frame_actors.config(bg='white')

    tree_scroll_actors = Scrollbar(tree_frame_actors)
    tree_scroll_actors.pack(side=RIGHT, fill=Y)

    tv_actors = ttk.Treeview(tree_frame_actors, columns=('actor'), show='tree', height= 3, yscrollcommand=tree_scroll_actors.set)
    
    tv_actors.column('#0', width=0, stretch=NO)
    tv_actors.column('actor', width=450, minwidth=450,anchor=CENTER)

    tv_actors.heading('#0', text='', anchor=CENTER)
    tv_actors.heading('actor',text='Actor', anchor=CENTER)

    tv_actors.pack()

    for i in tv_actors.get_children():
        tv_actors.delete(i)

    countA = 0
    actor_list = []

    for i in range(len(values[6])):
        if values[6] != "N/A":
            actor_list.append([[values[6][i]["full-name"]]])
        else:
            actor_list.append(["N/A"])
            break

    for row in actor_list:
        tv_actors.insert(parent='', index='end', iid=countA, text ='', values=(row[0]))
        countA += 1

    # La variable name tiene el nombre del actor/director que le pasamos en las funciones getNamesDirector o getNamesActor
    def getNames(name):
        topN = Toplevel()
        topN.geometry('700x350')
        topN.iconbitmap('./assets/movie_ico.ico')
        topN.title(name + ' Datasheet')

        #* ACA DEBERIAS GENERAR UNA VARIABLE QUE LLAME LOS DATOS DE LA VARIABLE name, NO LE PONGAS DE NOMBRE values, ponele otro...
        nameData = searchName(name)


        canvasTopN = Canvas(
            topN,
            bg = "#FFFFFF",
            height = 600,
            width = 700,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvasTopN.pack()

        image_image_N1 = PhotoImage(
        file=relative_to_assets("image_N1.png"))
        image_N1 = canvasTopN.create_image(
            350.0,
            300.0,
            image=image_image_N1
        )

        image_image_N2 = PhotoImage(
            file=relative_to_assets("image_N2.png"))
        image_N2 = canvasTopN.create_image(
            246.0,
            214.0,
            image=image_image_N2
        )

        image_image_N3 = PhotoImage(
            file=relative_to_assets("image_N3.png"))
        image_N3 = canvasTopN.create_image(
            349.0,
            173.0,
            image=image_image_N3
        )

        # Esta es la label donde se muestra el nombre del Actor/Director
        label_1N = ttk.Label(
        topN,
        background='#FFFFFF',
        font='Nunito 12',
        text= nameData[0] # Actor/Director Name
        )
    
        label_1N.place(
            x=165, 
            y=35,
            width=495.0,
            height=28.0
            )

        # Esta es la label donde se muestra el Birth-Year
        label_2N = ttk.Label(
        topN,
        background='#FFFFFF',
        font='Nunito 12',
        text= nameData[1] # Birth-Year
        )
    
        label_2N.place(
            x=165, 
            y=78,
            width=185.0,
            height=28.0
            )

        # Esta es la label donde se muestra el Death-Year
        label_3N = ttk.Label(
        topN,
        background='#FFFFFF',
        font='Nunito 12',
        text= nameData[2] # Death-Year
        )
    
        label_3N.place(
            x=490, 
            y=78,
            width=155.0,
            height=28.0
            )

        # Esta es la label donde se muestra la Profesion
        label_4N = ttk.Label(
        topN,
        background='#FFFFFF',
        font='Nunito 12',
        wraplength=483,
        justify='left',
        text=nameData[3] # Plot
        )
        
        label_4N.place(
            x=165, 
            y=120,
            width=483.0,
            height=55.0
            )

        # Creación Treeview Movies
        tree_frame_movies = Frame(topN)
        tree_frame_movies.place(x = 160, y= 190)
        tree_frame_movies.config(bg='white')

        tree_scroll_movies = Scrollbar(tree_frame_movies)
        tree_scroll_movies.pack(side=RIGHT, fill=Y)

        tv_movies = ttk.Treeview(tree_frame_movies, columns=('movie'), show='tree', height= 4, yscrollcommand=tree_scroll_movies.set)
        
        tv_movies.column('#0', width=0, stretch=NO)
        tv_movies.column('movie', width=450, minwidth=450,anchor=CENTER)

        tv_movies.heading('#0', text='', anchor=CENTER)
        tv_movies.heading('movie',text='Actor', anchor=CENTER)

        tv_movies.pack()

        for i in tv_movies.get_children():
            tv_movies.delete(i)

        # Aca se rellena el treeview de las peliculas a mostrar
        countM = 0
        movies_list = [[title] for title in nameData[4]]
        for row in movies_list:
            tv_movies.insert(parent='', index='end', iid=countM, text ='', values=(row))
            countM += 1

        topN.resizable(False, False)
        topN.mainloop()

    # Esta funcion llama a la funcion getNames pasandole como parametro el nombre del director, la funcion toma como entrada el boton
    def getNamesDirector(event):
        if label_2['text'] == 'N/A':
            messagebox.showinfo('Error', 'No hay Datasheet de director disponible')
        else:
            getNames(label_2['text'])

    # Esta funcion llama a la funcion getNames pasandole como parametro el nombre del actor, la funcion toma como entrada el valor seleccionado en el treeview
    def getNamesActor(event):
        selected = tv_actors.focus()
        actorName = tv_actors.item(selected, 'values')
        if actorName[0] == 'N/A':
            messagebox.showinfo('Error', 'No hay Datasheet de actor disponible')
        else:
            getNames(actorName[0])

    label_2.bind("<Double-Button-1>", getNamesDirector)
    tv_actors.bind("<Double-1>", getNamesActor)

    top.resizable(False, False)
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

# Bindear teclas a funciones
tv.bind("<Double-1>", getRow)
entry_1.bind("<Return>", showTitleEnter)

tree_scroll.config(command=tv.yview)

window.resizable(False, False)
window.mainloop()
