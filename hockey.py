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
