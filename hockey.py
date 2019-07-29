# Módulos
import sys, pygame
from pygame.locals import *
# Medidas de la ventana principal
WIDTH = 1145
HEIGHT = 600
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
# Funciones en general
def ganador(goles):

    class Inicio ():
        def __init__(self, ):
            self.lineas = 0
            self.caracteres = ['', ]
            self.fuente = pygame.font.Font(None, 25)

            self.distancia = 20
            self.posX = 50
            self.posY = 50
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

        def mensaje(self, superficie):#mensaje para que me deje ingresar el nombre del jugador que ocupo el mango
            for self.lineas in range(len(self.caracteres)):
                Img_letra = self.fuente.render(self.caracteres[self.lineas], True, (43, 233, 17))
                superficie.blit(Img_letra, (self.posX, self.posY + self.distancia * self.lineas))
                mensaje = self.fuente.render(("Ingrese su nombre"), 0, (26, 45, 225))
                superficie.blit(mensaje, (10, 30))

            pygame.display.flip()
            
            #Aqui creamos el archivo con formato txt para almacenar los nombres de los jugadpores ganadores
        def creartxt(self, ):
            archi = open('datos.txt', 'w') #guardo los datos de los jugadores
            archi.close()

        def leertxt(self, superficie):
            archi = open('datos.txt', 'r')
            linea = archi.readline()
            valorY = 0
            while linea != "":
                linea = archi.readline()
                lista = self.fuente.render(str(linea), 0, ( 17, 17, 20))
                valorY = valorY + 65
                superficie.blit(lista, (40, valorY))
            archi.close()

    def grabartxt(dato):
        archi = open('datos.txt', 'a') #se guarda los datos de los jugadores 
        archi.write(dato + "\n")
        archi.close()

    def registro():
        pygame.mixer.music.stop()
        if __name__ == '__main__':
            salir = False

            pygame.init()
            pygame.font.init()
            screen = pygame.display.set_mode((894, 550))  #muestro la tabla de puntajes al finalizar el juego acabar tiempo y demas 
            pygame.display.set_caption("MARCADOR")
            estiloLetra = pygame.font.SysFont("Broadway", 45)
            fondo = pygame.image.load("medalla.png").convert()
            sonidoMenu = pygame.mixer.music.load("fin.mp3")
            pygame.mixer.music.play(1)
            ingresoTXT = Inicio()
            screen.blit(fondo, (0, 0))
            while not salir:
                mensaje = estiloLetra.render(("MARCADOR"), 0, (7, 32, 250))
                screen.blit(mensaje, (310, 0))
                eventos = pygame.event.get()
                for action in eventos:
                    if action.type == pygame.MOUSEBUTTONDOWN:
                        menu_inicio()

                ingresoTXT.leertxt(screen)
                pygame.display.flip()
                pygame.time.delay(400)
            pygame.display.flip()

    def puntos(): #Aqui registraremos los puntos de cada jugador 
        print("tiene puntos")
        if __name__ == '__main__':

            salir = False

            pygame.font.init()
            screen = pygame.display.set_mode((894, 550))
            pygame.display.set_caption("MARCADOR")
            estiloLetra = pygame.font.SysFont("Broadway", 35)
            fondo = pygame.image.load("medalla.png").convert()

            pygame.init()
            sonidoMenu = pygame.mixer.music.load("menu.mp3")
            pygame.mixer.music.play(1)

            ingresoTXT = Inicio()
            while not salir:
                eventos = pygame.event.get()

                screen.blit(fondo, (0, 0))

                mensaje = estiloLetra.render(("MARCADOR"), 0, (206, 30, 4))
                screen.blit(mensaje, (310, 0))
                ingresoTXT.Final(eventos)
                ingresoTXT.mensaje(screen)
                ingresoTXT.leertxt(screen)
                # display.update()
                pygame.display.flip()
                pygame.time.delay(400)
            pygame.display.flip()

    puntos()

def load_image(filename, transparent=False): #Retencion de las imagenes dentro del tablero
    try:
        image = pygame.image.load(filename)
    except pygame.error as message:
        raise
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image

def texto(texto, posx, posy, color=(255, 255, 255)):
    fuente = pygame.font.Font(None, 50)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

#Sonido durante el juego
def sonido():
    pygame.init()
    sonidocolision = pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(3)
    print("Melodia")
    pygame.mixer.Sound.stop()

def main(decision):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Hockey de Mesa")

    background_image = load_image('tablero.png')
    puck = Disco()

    #Posicion inciial de los mangos
    jugador1 = Mangos(30)
    jugador2 = Mangos(WIDTH -30)

    clock = pygame.time.Clock()

    auxTime=0  #Tiempo del juego
    estiloLetra = pygame.font.SysFont("Broadway", 30)

    puntos = [0, 0]
    decicion=True

    colorPuntos=(169, 62, 17)
    colorTiempo=(29, 133, 28)
    if decicion==True:
        auxTime=auxTime*auxTime
        print("Se inicializa tiempo "+str(auxTime))
        contP1 = 0              
        contP2=0
        tiempoMaximo=25     #Hacemos un contador regresivo para el tiempo de juego con un maximo de 25 segundos de duracion
        while decicion:
            time = clock.tick(60)
            keys = pygame.key.get_pressed() #para que vaya acorde al movimiento el tiempo vaya corriendo, contador
            tiempo = pygame.time.get_ticks() / 1000  # para el reloj
            if auxTime<= tiempo:
                print (str(auxTime)+" Segundos")
                auxTime+=1
                tiempoMaximo -=1
            for eventos in pygame.event.get():
                if eventos.type == QUIT:
                    sys.exit(0)

            puntos = puck.mover( time, jugador1,jugador2,puntos)
            jugador1.movermango1(time, keys)
            jugador2.movermango2(time,puck,keys)

            p_jug, p_jug_rect = texto("Jugador 1 "+str(puntos[0]), WIDTH / 4, 40,colorPuntos)
            p_cpu, p_cpu_rect = texto("Jugador 2 "+str(puntos[1]), WIDTH - WIDTH / 4, 40,colorPuntos)
            screen.blit(background_image, (0, 0))
            screen.blit(p_jug, p_jug_rect)
            screen.blit(p_cpu, p_cpu_rect)
            screen.blit(puck.image, puck.rect)
            screen.blit(jugador1.image, jugador2.rect)
            screen.blit(jugador2.image, jugador1.rect)
            if puntos[0]==contP1+1:
                pygame.init()
                sonidocolision = pygame.mixer.music.load("musica.mp3")#aqui se repite la cancion durante el juego con tiempos cortos de 6 segundos
                pygame.mixer.music.play(6)
                contP1= contP1+1

            if puntos[1]==contP2+1:
                pygame.init()
                sonidocolision = pygame.mixer.music.load("musica.mp3")#se vuelve a repetir la cancion si hace el punto
                pygame.mixer.music.play(6)
                contP2= contP2+1

            mensajeReloj = estiloLetra.render("Tiempo :" + str(tiempoMaximo), 0,colorTiempo)  # mensaje de reloj en pantalla
            screen.blit(mensajeReloj, (465, 0))  # aparicion de reloj en pantalla
            if int(tiempoMaximo) == 0:
                score=0
                print("Cumple la condicion de tiempo")
                if puntos[0] > puntos[1]:
                    print("Ganador jugador 1")
                    pygame.time.wait(4000)
                    score=auxTime*puntos[0]
                    print("Puntage total de jugador 1: "+str(score))
                    ganador(score)
                    # irREgistro()
                    # sys.exit(0)
                elif puntos[0] < puntos[1]:
                    print("Ganador jugador 2")
                    pygame.time.wait(4000)
                    score=auxTime*puntos[1]
                    print("Puntage total de jugador 2: "+str(score))
                    ganador(score)
                else:
                    print("Juego empatado")#puntajes y condicional si existe un empate
                    print("Puntage total de jugador 1: "+str(puntos[0]))
                    print("Puntage total de jugador 1: " + str(puntos[1]))
                    puntos()

            pygame.display.flip()
        return 0

def puntos():
    print("Sus puntos son:")
    if __name__ == '__main__':

        salir = False

        pygame.font.init()
        screen = pygame.display.set_mode((800, 550))
        pygame.display.set_caption("MARCADOR FIN DE JUEGO")
        estiloLetra = pygame.font.SysFont("Broadway", 45)
        fondo = pygame.image.load("medalla.png").conv
        # Musica de fondo para la impresion del marcadorert()#se muestra la imagen al final del juego
        menu = Menu(opciones)
        pygame.init()
        sonidoMenu = pygame.mixer.music.load("fin.mp3")
        pygame.mixer.music.play(6)

        while not salir:

            for e in pygame.event.get():
                if e.type == QUIT:
                    salir = True
                    sys.exit(0)

            screen.blit(fondo, (0, 0))

            mensaje = estiloLetra.render(("MARCADOR"), 0, (206, 45, 225))
            screen.blit(mensaje, (310, 0))
            pygame.display.flip()
            pygame.time.delay(6)
        pygame.display.flip()

class Menu:
    "Representa un menú con opciones para un juego"


    def __init__(self, opciones):

        self.opciones = opciones
        self.font = pygame.font.SysFont('Snap ITC', 30) #ESTILO Y TAMAÑO DE LETRA DEL MENU DE INICIO
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""

        k = pygame.key.get_pressed()

        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                print("Selecciona la opción '%s'." % (titulo))
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        total = self.total
        indice = 0
        altura_de_opcion = 55
        x = 450 #posicion del menu con cordenadas en el 4to cuadrante
        y = 250

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

#Funciones que se llaman en la pantalla principal como menu
def comenzar_nuevo_juego():
    print(" Jugar")
    pygame.mixer.music.stop()
    if __name__ == '__main__':
        pygame.init()
        main(False)
    return 0


def puntajes():
    print(" Mostrar el marcador.")
    ganador(0)


def salir_del_programa():
    import sys
    print("Salir")
    sys.exit(0)


def menu_inicio():
    if __name__ == '__main__':

        salir = False
        opciones = [
            ("Jugar", comenzar_nuevo_juego),
            ("Marcador", puntajes),
            ("Salir", salir_del_programa)
        ]

        pygame.font.init()
        screen = pygame.display.set_mode((630, 405))
        pygame.display.set_caption("HOCKEY DE MESA")
        fondo = pygame.image.load("inicio.png").convert()
        menu = Menu(opciones)
        #llama al menu pricipal para iniciar el juego de fondo tendra una imagen 
        pygame.init()
        sonidoMenu = pygame.mixer.music.load("menu.mp3")
        pygame.mixer.music.play(6)

        while not salir:

            for e in pygame.event.get():
                if e.type == QUIT:
                    salir = True

            screen.blit(fondo, (0, 0))
            menu.actualizar()
            menu.imprimir(screen)

            pygame.display.flip()
            pygame.time.delay(6)
menu_inicio()
