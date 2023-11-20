import tkinter as tk 

def display_game_interface():
    #Creer une fenetre
    window= tk.Tk()
    #personnaliser la fenetre
    window.title("Memory Game")
    window.iconbitmap("3997691.png")
    window.minsize(480,360)



    #Configuration de la fenetre 
    window.config(background='#C597FF')


    #Création des étiquettes
    title_label=tk.Label(window,text="MEMORY GAME", font=("Tahoma",40), bg='#C597FF', fg='white')
    title_label.pack(expand = "Yes")

    frame= tk.Frame(window , bg="#C597FF")

    def open_window():
        secondary_window= tk.Toplevel(window)
        secondary_window.title("Game")
        secondary_window.iconbitmap("3997691.ico")
        secondary_window.minsize(480,360)
        secondary_window.config(background= "#C597FF")

    #ajouter une image
    width=300  
    height=300
    image=tk.PhotoImage(file="3997691.png").zoom(35).subsample(32) 
    canvas= tk.Canvas( width=width,height= height ,bg="#C597FF" ,bd=0)
    canvas.create_image(width/2, height/2,image=image )
    canvas.pack(expand='Yes')



        #ajouter un bouton start
    play= tk.Button(frame, text="PLAY",font=("Tahoma",20), bg='#C597FF', fg='white', command= open_window )
    play.pack()
    secondary_label=tk.Label(frame,text="Click PLAY to start", font=("Arial",10), bg='#C597FF', fg='black')
    secondary_label.pack(expand = "Yes")
    frame.pack(expand="Yes")
    #afficher la fenetre
    window.mainloop()
display_game_interface()
