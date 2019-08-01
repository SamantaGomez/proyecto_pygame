import pymysql
import sys
from tkinter import*
from tkinter import ttk
from tkinter import messagebox


def crearNuevoProfesor():
	
	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='base')
	cursor=conexion.cursor()

	cursor.execute("INSERT INTO profesor VALUES('"+miUsuario.get() +
		"','"+miId.get()  +"')")
        
	conexion.commit()



def leerProfe():

	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='base')
	cursor=conexion.cursor()

	conexion.commit()

	try:

		cursor.execute("SELECT * FROM profesor WHERE id ="+miId.get())

		elUsuario=cursor.fetchall()

		for usuario in elUsuario:

			miId.set(usuario[1])

		cursor.execute("UPDATE notas SET idprofesor ='"+miUsuario.get() + "',matematica ='"+miMatematica.get() +"', lenguaje ='"+miLenguaje.get() +"' WHERE numerolista = "+ miLista.get())
	
		messagebox.showinfo("BBDD","USUARIO CORRECTO")

		notas()
	
	except:

		messagebox.showwarning("¡ATENCION!","NO EXISTE EL USUARIO")


def crearNotas():
	
	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='base')
	cursor=conexion.cursor()

	
	cursor.execute("INSERT INTO notas VALUES('"+miLista.get() +
		"','"+miFisica.get() +
		"','"+miMatematica.get() +
		"','"+miLenguaje.get()+"')")



	conexion.commit()

	messagebox.showinfo("BBDD","REGISTRO INSERTADO CON EXITO")

def limpiarCampos():

	miLista.set("")
	miFisica.set("")
	miMatematica.set("")
	miLenguaje.set("")
	


def leerNotasProfe():

	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='base')
	cursor=conexion.cursor()

	conexion.commit()

	cursor.execute("SELECT * FROM notas WHERE numerolista =" + miLista.get())

	elEstudiante=cursor.fetchall()

	for usuario in elEstudiante:
		
		miLista.set(usuario[0])
		miFisica.set(usuario[1])
		miMatematica.set(usuario[2])
		miLenguaje.set(usuario[3])

	conexion.commit()

def actualizar():

	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='base')
	cursor=conexion.cursor()
	
	

	cursor.execute("UPDATE notas SET fisica ='"+miFisica.get() + "',matematica ='"+miMatematica.get() +"', lenguaje ='"+miLenguaje.get() +"' WHERE numerolista = "+ miLista.get())
	
	conexion.commit()
	
	messagebox.showinfo("BBDD","REGISTRO ACTUALIZADO CON EXITO")	


def eliminar():

	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='base')
	cursor=conexion.cursor()

	cursor.execute("DELETE FROM notas WHERE numerolista = "+ miLista.get())
	
	conexion.commit()

	messagebox.showinfo("BBDD", "REGISTRO BORRADO CON EXITOS")



def notas():

	ventanaNotas=Toplevel(ventana)
	ventanaNotas.geometry('500x500')

	miFrame=Frame(ventanaNotas)
	miFrame.pack()

	cuadroEstudiante=Entry(miFrame, textvariable=miLista)
	cuadroEstudiante.grid(row=1,column=1,padx=10, pady=10)

	cuadroFisica=Entry(miFrame, textvariable=miFisica)
	cuadroFisica.grid(row=2,column=1,padx=10, pady=10)

	cuadroMatematica=Entry(miFrame,textvariable=miMatematica)
	cuadroMatematica.grid(row=3,column=1,padx=10, pady=10)

	cuadroLenguaje=Entry(miFrame,textvariable=miLenguaje)
	cuadroLenguaje.grid(row=4,column=1,padx=10, pady=10)


	#COMENZAMOS A ETIQUETAR

	

	idLabel=Label(miFrame, text="Numero lista:")
	idLabel.grid(row=1,column=0,sticky="e",padx=10, pady=10)

	fisicaLabel=Label(miFrame, text="Fisica:")
	fisicaLabel.grid(row=2,column=0,sticky="e",padx=10, pady=10)

	matematicaLabel=Label(miFrame, text="Matematica:")
	matematicaLabel.grid(row=3,column=0,sticky="e",padx=10, pady=10)

	lenguajeLabel=Label(miFrame, text="Lenguaje:")
	lenguajeLabel.grid(row=4,column=0,sticky="e",padx=10, pady=10)



	botonCrear=Button(miFrame,text="Nuevo", command = crearNotas)
	botonCrear.grid(row=5,column=0,sticky="e",padx=10,pady=10)

	botonLeer=Button(miFrame,text="Leer", command = leerNotasProfe)
	botonLeer.grid(row=5,column=1,sticky="e",padx=10,pady=10)

	botonActualizar=Button(miFrame,text="Limpiar Campos",command=limpiarCampos)
	botonActualizar.grid(row=6,column=1,sticky="e",padx=10,pady=10)

	botonActualizar=Button(miFrame,text="Actualizar", command=actualizar)
	botonActualizar.grid(row=6,column=2,sticky="e",padx=10,pady=10)

	botonBorrar=Button(miFrame,text="Borrar", command =eliminar)
	botonBorrar.grid(row=6,column=3,sticky="e",padx=10,pady=10)
		







def UsuarioProfesor():

	ventanaProfe=Toplevel(ventana)
	ventanaProfe.geometry('300x200')


	cuadroUsuario=Entry(ventanaProfe, textvariable=miUsuario)
	cuadroUsuario.grid(row=0,column=1,padx=10, pady=10)

	cuadroContrasena=Entry(ventanaProfe, textvariable=miId)
	cuadroContrasena.grid(row=1,column=1,padx=10, pady=10)

	#COMENZAMOS A ETIQUETAR
	usuarioLabel=Label(ventanaProfe, text="USUARIO:")
	usuarioLabel.grid(row=0,column=0,sticky="e",padx=10, pady=10)

	contrasenaLabel=Label(ventanaProfe, text="CONTRASEÑA:")
	contrasenaLabel.grid(row=1,column=0,sticky="e",padx=10, pady=10)

	#AÑADIMOS UN BOTON A ENTRAR
	botonEntrar=Button(ventanaProfe,text="ENTRAR",command=leerProfe)
	botonEntrar.grid(row=3,column=0,sticky="e",padx=10,pady=10)

	#AÑADIMOS UN BOTON A AÑADIR
	botonUsuario=Button(ventanaProfe,text="CREAR USUARIO",command=crearNuevoProfesor)
	botonUsuario.grid(row=4,column=0,sticky="e",padx=10,pady=10)
	#ADIREMOS UN BOTEN CREAR


def leerEstudiante():

	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='base')
	cursor=conexion.cursor()

	conexion.commit()

	try:

		cursor.execute("SELECT * FROM estudiante WHERE idEstudiante ="+miIdEstudiante.get())

		elUsuario=cursor.fetchall()

		for usuario in elUsuario:

			miIdEstudiante.set(usuario[1])

		messagebox.showinfo("BBDD","ESTUDIANTE MATRICULADO")

		notasEstudiante()
	
	except:

		messagebox.showwarning("¡ATENCION!","NO EXISTE EL DATOS DEL ESTUDIANTE")


def leerNotasEstudiante():

	conexion=pymysql.connect(host='localhost',port=3306, user='root', passwd='', db='base')
	cursor=conexion.cursor()

	conexion.commit()

	cursor.execute("SELECT * FROM notas WHERE numerolista =" + miLista.get())

	elEstudiante=cursor.fetchall()

	for usuario in elEstudiante:
		
		miLista.set(usuario[0])
		miFisica.set(usuario[1])
		miMatematica.set(usuario[2])
		miLenguaje.set(usuario[3])

	conexion.commit()

def notasEstudiante():

	ventanaEstudiante=Toplevel(ventana)
	ventanaEstudiante.geometry('500x500')

	miFrame=Frame(ventanaEstudiante)
	miFrame.pack()

	cuadroEstudiante=Entry(miFrame, textvariable=miLista)
	cuadroEstudiante.grid(row=1,column=1,padx=10, pady=10)

	cuadroFisica=Entry(miFrame, textvariable=miFisica)
	cuadroFisica.grid(row=2,column=1,padx=10, pady=10)

	cuadroMatematica=Entry(miFrame,textvariable=miMatematica)
	cuadroMatematica.grid(row=3,column=1,padx=10, pady=10)

	cuadroLenguaje=Entry(miFrame,textvariable=miLenguaje)
	cuadroLenguaje.grid(row=4,column=1,padx=10, pady=10)


	#COMENZAMOS A ETIQUETAR

	

	idLabel=Label(miFrame, text="Numero lista:")
	idLabel.grid(row=1,column=0,sticky="e",padx=10, pady=10)

	fisicaLabel=Label(miFrame, text="Fisica:")
	fisicaLabel.grid(row=2,column=0,sticky="e",padx=10, pady=10)

	matematicaLabel=Label(miFrame, text="Matematica:")
	matematicaLabel.grid(row=3,column=0,sticky="e",padx=10, pady=10)

	lenguajeLabel=Label(miFrame, text="Lenguaje:")
	lenguajeLabel.grid(row=4,column=0,sticky="e",padx=10, pady=10)


	botonLeer=Button(miFrame,text="Leer", command = leerNotasEstudiante)
	botonLeer.grid(row=5,column=1,sticky="e",padx=10,pady=10)




def UsuarioEstudiante():

	ventanaEstudiante=Toplevel(ventana)
	ventanaEstudiante.geometry('300x200')


	cuadroUsuario=Entry(ventanaEstudiante, textvariable=miUsuarioEstudiante)
	cuadroUsuario.grid(row=0,column=1,padx=10, pady=10)

	cuadroContrasena=Entry(ventanaEstudiante, textvariable=miIdEstudiante)
	cuadroContrasena.grid(row=1,column=1,padx=10, pady=10)

	#COMENZAMOS A ETIQUETAR
	usuarioLabel=Label(ventanaEstudiante, text="USUARIO:")
	usuarioLabel.grid(row=0,column=0,sticky="e",padx=10, pady=10)

	contrasenaLabel=Label(ventanaEstudiante, text="CONTRASEÑA:")
	contrasenaLabel.grid(row=1,column=0,sticky="e",padx=10, pady=10)

	#AÑADIMOS UN BOTON A ENTRAR
	botonEntrar=Button(ventanaEstudiante,text="ENTRAR",command=leerEstudiante)
	botonEntrar.grid(row=3,column=0,sticky="e",padx=10,pady=10)












#VENTANA PARA PROFESOR Y ESTUDIANTE

ventana= Tk()
ventana.config(bd=80)

#MI USUARIO PROFESOR
miUsuario=StringVar()
miId=StringVar()

#MI USUARIO PROFESOR
miUsuarioEstudiante=StringVar()
miIdEstudiante=StringVar()


#MI USUARIO NOTAS
miLista=StringVar()
miFisica=StringVar()
miMatematica=StringVar()
miLenguaje=StringVar()



miFrame=Frame()
miFrame.pack()

botonCrear=Button(miFrame,text="PROFESOR", command=UsuarioProfesor)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame,text="ESTUDIANTE",command=UsuarioEstudiante)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)





ventana.mainloop()
