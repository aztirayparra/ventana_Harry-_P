import tkinter as tk

#Creación de la ventana
ventana=tk.Tk()
ventana.title("Sombrero seleccionador")
ventana.iconbitmap("Snitch.ico")
ventana.geometry("900x700+400+50")

#Creación de los Marcos,etiquetas y botones
frame1=tk.Frame()
frame1.configure(bg="red4",bd=20,width=300,height=300)
label1 = tk.Label(frame1, text=" Gryffindor")

frame2=tk.Frame()
frame2.configure(bg="gold2",bd=20,width=300,height=300)
label2 = tk.Label(frame2, text="Hufflepuff")

frame3=tk.Frame()
frame3.configure(bg="blue4",bd=20,width=300,height=300)
#método del botón
def averiguar_personajes():
    print("Luna Lovegood, Cho Chang")
boton=tk.Button(frame3,text="Haga click", command=averiguar_personajes)#commmand es para llamar al metodo
label3 = tk.Label(frame3, text="Ravenclaw")

frame4=tk.Frame()
frame4.configure(bg="dark green",bd=20,width=200,height=200)
label4 = tk.Label(frame4, text="Slytherin")

# Botón en el lado derecho de la etiqueta
def conocer_personajes():
    print("Draco Malfoy, Severus Snape, Tom Riddle")
boton_frame4 = tk.Button(frame4, text="Haga click", command=conocer_personajes)
boton_frame4.pack(side=tk.RIGHT, padx=5, pady=10) 


#Empaquetamiento de marcos, etiquetas y botones
frame1.grid(row=0, column=0,padx=10)
label1.pack(pady=10)

frame2.grid(row=0, column=1)
label2.pack(pady=10)

frame3.grid(row=1, column=0,pady=25)
label3.pack(pady=10)
boton.pack()

frame4.grid(row=1, column=1, pady=10)
label4.pack(side=tk.LEFT, pady=10)  # Empaquetar etiqueta en frame4 a la izquierda


ventana.mainloop()

