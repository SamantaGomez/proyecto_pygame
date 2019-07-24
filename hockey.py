# Librerias e importaciones
import sys, pygame
from pygame.locals import *

# medidas de la ventana
WIDTH = 1165
HEIGHT = 800
# creacion del proyecto por clases
#clase de puck
class Puck(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("/*imagen*/", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.4, -0.4]
# Librerias e importaciones
import sys, pygame
from pygame.locals import *

# medidas de la ventana
WIDTH = 1165
HEIGHT = 800

# creacion del proyecto por clases

#clase  para la creacion del DISCO
class DISCO(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("DISCO.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.4, -0.4]

#creacion de funcion mover, dentro del la clase DISCO
     def MoverDisco(self, time, player1,player2,puntaje):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time

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
        if pygame.sprite.collide_rect(self, player1):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if pygame.sprite.collide_rect(self, player2):
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time

        return puntaje
		
class Mango(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("mango1.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.9		
		
#creacion de la funcion MoverMango		
	 def MoverMango(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_w]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_s]:
                self.rect.centery += self.speed * time
        if self.rect.centerx<=HEIGHT:
            if self.rect.bottom <= HEIGHT:
                if keys[K_d]:
                    self.rect.centerx += self.speed * time
        if self.rect.centerx >= 15:
            if self.rect.bottom <= HEIGHT:
                if keys[K_a]:
                    self.rect.centerx -= self.speed * time
					
					
#funcion ganador indico la sintaxis y en donde va a estar tanto en X como en Y

def ganador(goles):

    class Inicio():
        def __init__(self, ):
            self.lineas = 0
            self.caracteres = ['', ]
            self.fuente = pygame.font.Font(None, 25)

            self.distancia = 20
            self.posX = 50
            self.posY = 50
			
		def teclado(self, evento):
		
			if goles == 0:
				registro()
				
			#else:
			#	print ("hola")
			for accion in evento:
				if accion.type == KEYDOWN:
					if accion.key == K_RETURN:
						self.caracteres.append('')
						print("Guardado")
						marcador = goles
						dato = "Player: " + str(self.caracteres)+ "Puntaje: " +str(marcador)
						grabartxt()
						registro()
						
					elif accion.key == K_ESCAPE:
						print("SALIO DEL JUEGO")
						sys.exit()
					elif accion.key == K_BACKSPACE:
						if self.caracteres[self.lineas] == '' and self.lineas>0:
							self.caracteres = self.caracteres[0:-1]
						else:
							self.caracteres[self.lineas]= self.caracteres[self.lineas][0:-1]
							
					else:
						self.caracteres[self.lineas]= str(self.caracteres[self.lineas] +accion.unicode)
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

	#funcion para grabar los datos que ya se han leido		
    def grabartxt(dato):
        archi = open('datos.txt', 'a')
        archi.write(dato + "\n")
        archi.close()	
		
	#Funcion para los registros 
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
    def puntos(): #Aqui registraremos los puntos de cada jugador 
        print("Llego a puntos")
        if __name__ == '__main__':

            salir = False

            pygame.font.init()
            screen = pygame.display.set_mode((894, 550))
            pygame.display.set_caption("******REGISTRO DE PUNTAJES******")
            estiloLetra = pygame.font.SysFont("Bauhaus 93", 35)
            fondo = pygame.image.load("puntages.jpg").convert()