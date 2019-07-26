# Módulos
import sys, pygame
from pygame.locals import *
# Medidas de la ventana principal
WIDTH = 1145
HEIGHT = 600

# Clases
# ---------------------------------------------------------------------
# CLASE QUE CREA DISCO
class Disco(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #madnamos a llamar la imagen, o el atributo Disco dentro de la clase Disco
        self.image = load_image("DISCO.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2  #Medidas del disco y ubicacion en la ventana
        self.rect.centery = HEIGHT / 2
        self.speed = [0.8, -0.8]

    def mover(self, time, jugador1,jugador2,puntos): #definimos parametros, de las variables involucradas
        self.rect.centerx += self.speed[0] * time #arrancamos el juego 
        self.rect.centery += self.speed[1] * time

        #condicionamos y damos un contador de puntos, cuando el disco marque gol, en los extremos de el tablero
        if self.rect.left <= 0:
            puntos[1] += 1
        if self.rect.right >= WIDTH:
            puntos[0] += 1
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time
        if pygame.sprite.collide_rect(self, jugador1):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if pygame.sprite.collide_rect(self, jugador2):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time

        return puntos

#creamos la clase mango1 que va a ser para el primer jugador
class Mangos(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("mango1.png", True) #mandamos a llamar a la imagen de mango
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2  #el mango uno se presente en la mitad del lado izquierdo
        self.speed = 0.5 #segundos que se demora el mango en movimiento

    def movermango1(self, time, keys):#definimos una funcion para el movimiento del mango1 con las teclas W,S,A,D
        if self.rect.top >= 0:
            if keys[K_w]:       #tecla hacia arriba
                self.rect.centery -= self.speed * time #declaramos time para que vaya corriendo y marque el tiempo de acuerdo al movimiento
        if self.rect.bottom <= HEIGHT:
            if keys[K_s]:       #tecla hacia abajo
                self.rect.centery += self.speed * time

        if self.rect.centerx<=HEIGHT:
            if self.rect.bottom <= HEIGHT:
                if keys[K_d]:   #tecla hacia la derecha
                    self.rect.centerx += self.speed * time

        if self.rect.centerx >= 15:
            if self.rect.bottom <= HEIGHT:
                if keys[K_a]:   #tecla hacia la izquierda
                    self.rect.centerx -= self.speed * time

    def movermango2(self, time, puck_2, keys):#definimos una funcion para el movimiento del mango2 con lsa flechas del key

            if self.rect.top >= 0:
                if keys[K_UP]:          #tecla hacia arriba
                    self.rect.centery -= self.speed * time
            if self.rect.bottom <= HEIGHT:
                if keys[K_DOWN]:        ##tecla hacia abajo
                    self.rect.centery += self.speed * time

            if self.rect.centerx < WIDTH:
                if self.rect.bottom <= WIDTH:
                    if keys[K_RIGHT]:   #tecla hacia la derecha
                        self.rect.centerx += self.speed * time

            if self.rect.centerx >= WIDTH/2:
                if self.rect.bottom <= WIDTH:
                    if keys[K_LEFT]:     #tecla hacia la izquierda
                        self.rect.centerx -= self.speed * time
# ---------------------------------------------------------------------
# Funciones en general
# ---------------------------------------------------------------------
def ganador(goles):

    class Inicio ():
        """def __init__(self, ):
            self.lineas = 0
            self.caracteres = ['', ]
            self.fuente = pygame.font.Font(None, 25)

            self.distancia = 20
            self.posX = 50
            self.posY = 50"""
        def Final(self, evento):#defino la funcion para guardar y moestrar el puntaje de quienes jugaron 
            if goles == 0:
                registro()#indico que si no exiten goles se vaya a la funcion registro, donde me indicara directamente la imagen 
                          #final donde muestra el total de los puntajes y Fin de juego 
            for accion in evento:
                if accion.type == KEYDOWN:
                    if accion.key == K_RETURN:
                        self.caracteres.append('')
                        print("Guardado")
                        marcador = goles
                        dato = "Jugador: " + str(self.caracteres) + " Puntos: " + str(marcador)
                        grabartxt(dato)
                        registro() #si jugó la partida, cuando se acabe el tiempo, 
                                   #al final del juego indicará el puntaje de cada jugador y muestra GAME OVER
                    elif accion.key == K_ESCAPE:#ESC para salir
                        print("Game Over")
                        sys.exit()
                    elif accion.key == K_BACKSPACE:
                        if self.caracteres[self.lineas] == '' and self.lineas > 0:
                            self.caracteres = self.caracteres[0:-1]
                        else:
                            self.caracteres[self.lineas] = self.caracteres[self.lineas][0:-1]

                    else:
                        self.caracteres[self.lineas] = str(self.caracteres[self.lineas] + accion.unicode)
		def peticion(self, superficie):
            for self.lineas in range(len(self.caracteres)):
                Img_letra = self.fuente.render(self.caracteres[self.lineas], True, (43, 233, 17))
                superficie.blit(Img_letra, (self.posX, self.posY + self.distancia * self.lineas))
                peticion = self.fuente.render(("Ingrese su Apodo"), 0, (26, 45, 225))
                superficie.blit(peticion, (10, 30))
				
			pygame.display.flip()
				
		def creartxt(self, ):
            archi = open('datos.txt', 'w')
            archi.close()	
		
		#Se crea una funcion para leer los datos 
		def leertxt(self, superficie):
            archi = open('datos.txt', 'r')
            linea = archi.readline()
            valorY = 0
            while linea != "":
                # print(linea)
                linea = archi.readline()
                lista = self.fuente.render(str(linea), 0, ( 17, 17, 20))
                valorY = valorY + 65
                superficie.blit(lista, (40, valorY))
            archi.close()
	
	def grabartxt(dato): #creareamos una funcion para grabar nuestros datos
        archi = open('datos.txt', 'a')
        archi.write(dato + "\n")
        archi.close()
		
	
	#CREAMOS UNA FUNCION REGISTRO PARA REGISTRAR LOS PUNTAJES DE LOS JUGADORES
	def registro():
        pygame.mixer.music.stop() 
        if __name__ == '__main__':
            salir = False

            pygame.init()
            pygame.font.init()
            screen = pygame.display.set_mode((894, 550))
            pygame.display.set_caption("******Puntajes******")
            estiloLetra = pygame.font.SysFont("Arial Black", 45)
            fondo = pygame.image.load("puntages.jpg").convert()
            sonMenu = pygame.mixer.music.load("puntagesM.mp3")
            pygame.mixer.music.play(1)
            ingresoTXT = Entrada()
            screen.blit(fondo, (0, 0))
            while not salir:
                mensaje = estiloLetra.render(("PUNTAJES "), 0, (7, 32, 250))
                screen.blit(mensaje, (310, 0))
                eventos = pygame.event.get()
                for action in eventos:
                    """if action.key == K_ESCAPE:
                        sys.exit()"""
                    if action.type == pygame.MOUSEBUTTONDOWN:
                        menu_inicio()
				
				ingresoTXT.leertxt(screen)
                pygame.display.flip()
                pygame.time.delay(400)
            pygame.display.flip()
	 def puntos(): #Aqui registramos los puntos de cada jugador 
        print("tiene puntos") 
        if __name__ == '__main__':

            salir = False

            pygame.font.init()
            screen = pygame.display.set_mode((894, 550)) #medidas de la ventana final donde muestra puntajes
            pygame.display.set_caption("******REGISTRO DE PUNTAJES******")
            estiloLetra = pygame.font.SysFont("Arial 93", 35)
            fondo = pygame.image.load("puntajes.png").convert() #mandamos a llamar a el tablero
            
            pygame.init()#inicializamos el menu mandando a llamar el sonido
            sonMenu = pygame.mixer.music.load("menu.mp3")
            pygame.mixer.music.play(1)#determinamos instancia para volver a repetir

            ingresoTXT = Inicio()
            while not salir:
                eventos = pygame.event.get()#mientras no salga seguimos detectando los eventos

                screen.blit(fondo, (0, 0))#fondo por default sin medidas 

                mensaje = estiloLetra.render(("REGISTRO DE PUNTAJES"), 0, (206, 30, 4))
                screen.blit(mensaje, (310, 0))
                ingresoTXT.Final(eventos)
                ingresoTXT.mensaje(screen)#mando a llamar a las funciones que me permiten ingresar el nombre del jugador
                ingresoTXT.leertxt(screen)
                pygame.display.flip()
                pygame.time.delay(400)#tiempo para retrasar al final de la ventana, loq ue me demoro para que salga el jugador 
            pygame.display.flip()

    puntos()

def load_image(filename, transparent=False): #retengo las imagenes en el tablero
    try:
        image = pygame.image.load(filename)#doy limites en coordenadas 
    except pygame.error as message:
        raise
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image

def texto(texto, posx, posy, color=(255, 255, 255)): #llamar a la funcion texto en recursividad
    fuente = pygame.font.Font(None, 50)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect
	
def sonido(): #sonido de fondo en la pantalla principal
    pygame.init()
    sonGolpe = pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(3)
    print("Melodia")
    pygame.mixer.Sound.stop()

#FUNCION MAIN  LAS DESCIONES PARA EL PROGRAMA
def main(decicion):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hockey de mesa")

    background_image = load_image('CanchaMesa.jpg')  #CARGAMOS LAS IMAGENES
    background_image1 = load_image('fondo_pong.png') # CARGAMOS LAS IMAGENES
    puck = Puck()


    jugador1 = Jugador(30) #ESTAMOS DANDO EL TAMAÑO D ELOS MANGOS
    jugador2 = Jugador(WIDTH -30) #ESTAMOS DANDO EL TAMAÑO D ELOS MANGOS

    clock = pygame.time.Clock()

    auxTime=0
    estiloLetra = pygame.font.SysFont("Arial black", 30)

    puntos = [0, 0]
    decicion=True

    colorPuntos=(169, 62, 17)
    colorTiempo=(29, 133, 28)
    
	#CREAMOS UN IF PARA LA DESCION DEL TIEMPO
    if decicion==True:
        auxTime=auxTime*auxTime
        print("se reseteo tiempo actual "+str(auxTime))
        contP1 = 0
        contP2=0
        tiempoMaximo=25
        while decicion:
            time = clock.tick(60)
            keys = pygame.key.get_pressed()
            tiempo = pygame.time.get_ticks() / 1000  # para el reloj
            if auxTime<= tiempo:
                print (str(auxTime)+" Segundos")
                auxTime+=1
                tiempoMaximo -=1
            for eventos in pygame.event.get():
                if eventos.type == QUIT:
                    sys.exit(0)

            puntos = puck.mover( time, jugador1,jugador2,puntos)
            jugador1.mover(time, keys)
            jugador2.ia(time,puck,keys)
			
			#NOS MUESTRA EL JUGADOR Y LOS PUNTOS QUE SE REALIZA AL MOMENTO DE QUE EL DISCO ENTRE EN LA ZONA DE ANOTACION 

            p_jug, p_jug_rect = texto("Jugador A "+str(puntos[0]), WIDTH / 4, 40,colorPuntos)
            p_cpu, p_cpu_rect = texto("Jugador B "+str(puntos[1]), WIDTH - WIDTH / 4, 40,colorPuntos)
            screen.blit(background_image, (0, 0))
            screen.blit(background_image1, (255, 70))
            screen.blit(p_jug, p_jug_rect)
            screen.blit(p_cpu, p_cpu_rect)
            screen.blit(puck.image, puck.rect)
            screen.blit(jugador1.image, jugador2.rect)
            screen.blit(jugador2.image, jugador1.rect)
            if puntos[0]==contP1+1:
                pygame.init()
                sonGolpe = pygame.mixer.music.load("golpe.mp3")
                pygame.mixer.music.play(1)
                contP1= contP1+1

            if puntos[1]==contP2+1:
                pygame.init()
                sonGolpe = pygame.mixer.music.load("golpe.mp3")
                pygame.mixer.music.play(1)
                contP2= contP2+1
				
			#NOS MUESTRA EL TIEMPO QUE TENEMOS PARA JUGAR     
            mensajeReloj = estiloLetra.render("Tiempo :" + str(tiempoMaximo), 0,colorTiempo)  # mensaje de reloj en pantalla
            screen.blit(mensajeReloj, (465, 0))  # aparicion de reloj en pantalla
            if int(tiempoMaximo) == 0:
                score=0
                print("Cumple la condicion de tiempo")
                if puntos[0] > puntos[1]:
                    print("Ganador jugador 1 !!!!!!!!!!!!!!!!!!!!!")
                    pygame.time.wait(4000)
                    score=auxTime*puntos[0]
                    print("Puntage total de jugador 1: "+str(score))
                    ganadore(score)
                    # irREgistro()
                    # sys.exit(0)
                elif puntos[0] < puntos[1]:
                    print("Ganador jugador 2 !!!!!!!!!!!!!!!!!!!!!")
                    pygame.time.wait(4000)
                    score=auxTime*puntos[1]
                    print("Puntage total de jugador 2: "+str(score))
                    ganadore(score)
                else:
                    print("Juego empatado")
                    print("Puntage total de jugador 1: "+str(puntos[0]))
                    print("Puntage total de jugador 1: " + str(puntos[1]))
                    puntajes()

            pygame.display.flip()
        return 0
def puntos():#funcion donde me idnica el final del puntaje y a cuantos puntos llego cada uno 
    print("Llego a puntos")
    if __name__ == '__main__':

        salir = False

        pygame.font.init()#inicializa
        screen = pygame.display.set_mode((894, 550))
        pygame.display.set_caption("******Puntajes******")#idico los puntajes, muestroo mensaje en tablero inicial
        estiloLetra = pygame.font.SysFont("Castellar", 45)#defino letra y tamaño y tipo 
        fondo = pygame.image.load("puntajes.png").convert()#mando a llamar a tablero inicial imagen inicial
        menu = Menu(opciones)
        # ----------inicio de sonido de menu
        pygame.init()
        sonMenu = pygame.mixer.music.load("PuntajesM.mp3")
        pygame.mixer.music.play(3)

		while not salir:

            for e in pygame.event.get():
                if e.type == QUIT:
                    salir = True
                    sys.exit(0)

            screen.blit(fondo, (0, 0))

            mensaje = estiloLetra.render(("***********Puntuaciones*********"), 0, (206, 45, 225))#me permite ver entrando a al funcion 
            screen.blit(mensaje, (310, 0))                  #de puntaje, los puntajes decada juagdor haciendo un contador
            pygame.display.flip()
            pygame.time.delay(10)#tiempo que me retrasa en copilar 
        pygame.display.flip()
		
class Menu:
    
    def __init__(self, opciones): #Representa un menú con opciones para un juego

        self.opciones = opciones
        self.font = pygame.font.SysFont('Castellar', 30)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False
	
    def actualizar(self):
        k = pygame.key.get_pressed()#Altera el valor de 'self.seleccionado' con los direccionales.

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:
                titulo, funcion = self.opciones[self.seleccionado] # Invoca a la función asociada a la opción.
                print("Selecciona la opción '%s'." % (titulo))
                funcion()
        if self.seleccionado < 0:# procura que el cursor esté entre las opciones permitidas
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
 
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN] # indica si el usuario mantiene pulsada alguna tecla.

    def imprimir(self, screen):#Imprime sobre 'screen' el texto de cada opción del menú
        total = self.total
        indice = 0
        altura_de_opcion = 55
        x = 250
        y = 105

        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                # color seleccionado
                color = (46, 144, 32)
            else:
                # color del menu
                color = (23, 62, 196)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)
def comenzar_nuevo_juego(): #funcion para que comienza nuevamente el juego desde cero
    print(" Función que muestra un nuevo juego.")
    pygame.mixer.music.stop()
    if __name__ == '__main__':
        pygame.init()
        main(False)
    return 0
def puntajes(): #opcion del boton puntajes 
    print(" Función que muestra otro menú de opciones.")
    ganador(0)
def salir_del_programa():
    import sys#la importacion de esta libreria sys, nos permite salir del programa x eso la mandamos a llamar
    print(" Gracias por utilizar este programa.")
    sys.exit(0)