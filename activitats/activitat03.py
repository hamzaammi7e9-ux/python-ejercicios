from enum import Enum
import random

columnas = 20
filas = 20
VELOCIDAD_MAXIMA = 5
VELOCIDAD_MINIMA = 0
POSICION_INICIAL = (0, 0)

class Casella(Enum):
    PARET = "\U0001F9F1"
    ROBOT = "\U0001F916"
    ROCA = "\U0001FAA8\uFE0F"
    DINAMITA = "\U0001F9E8"

# creo la matriu 20x20 plena de parets
espai = [[Casella.PARET.value for c in range(columnas)] for f in range(filas)]

# fiquem les roques aleatories
num_roques = random.randint(30, 70)
roques_fetes = 0
while roques_fetes < num_roques:
    rx = random.randint(0, columnas - 1)
    ry = random.randint(0, filas - 1)
    # que no surtin a la casella de sortida 0,0
    if not (rx == 0 and ry == 0):
        fila = (filas - 1) - ry
        # si no hi ha roca ja posada, la fiquem
        if espai[fila][rx] == Casella.PARET.value:
            espai[fila][rx] = Casella.ROCA.value
            roques_fetes += 1


class Robot:
    def __init__(self, x=0, y=0, vel=1):
        self.__x = x
        self.__y = y
        self.__vel = vel
        self.__viu = True
        self.spawn()

    # getters setters
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def vel(self):
        return self.__vel

    @vel.setter
    def vel(self, vel):
        self.__vel = vel

    @property
    def estaViu(self):
        return self.__viu

    @estaViu.setter
    def estaViu(self, viu):
        self.__viu = viu

    # com que 0,0 esta abaix a l'esquerra, hem d'invertir la fila
    def get_fila(self, y):
        return (filas - 1) - y

    # posa el robot al mapa a l'inici
    def spawn(self):
        f = self.get_fila(self.y)
        espai[f][self.x] = Casella.ROBOT.value

    def mover(self, direccion):
        passos = 0
        bloquejat = False

        # bucle per anar casella a casella segons la velocitat
        while passos < self.vel and not bloquejat and self.estaViu:
            nou_x = self.x
            nou_y = self.y

            # calculem a on aniria i mirem que no surti dels limits
            if direccion == "DALT" and self.y < filas - 1:
                nou_y += 1
            elif direccion == "BAIX" and self.y > 0:
                nou_y -= 1
            elif direccion == "ESQUERRA" and self.x > 0:
                nou_x -= 1
            elif direccion == "DRETA" and self.x < columnas - 1:
                nou_x += 1
            else:
                bloquejat = True

            if not bloquejat:
                desti_f = self.get_fila(nou_y)
                desti_c = nou_x

                # si hi ha una pedra xoca i s'atura
                if espai[desti_f][desti_c] == Casella.ROCA.value:
                    bloquejat = True
                else:
                    # deixem dinamita a la casella que deixem enrere
                    f_antiga = self.get_fila(self.y)
                    espai[f_antiga][self.x] = Casella.DINAMITA.value

                    # actualitzem coordenades
                    self.x = nou_x
                    self.y = nou_y

                    # si trepitja dinamita el robot mor y s'acaba el joc, si no, es posa a la nova casella
                    if espai[desti_f][desti_c] == Casella.DINAMITA.value:
                        print("BOOM!... Has trepitjat dinamita.")
                        self.estaViu = False
                    else:
                        espai[desti_f][desti_c] = Casella.ROBOT.value

            passos += 1

    def acelerar(self):
        if self.vel < VELOCIDAD_MAXIMA:
            self.vel += 1

    def frenar(self):
        if self.vel > VELOCIDAD_MINIMA:
            self.vel -= 1

    # reset del robot al punt d'inici
    def reiniciar(self):
        filActual = self.get_fila(self.y)
        espai[filActual][self.x] = Casella.PARET.value
        self.x = 0
        self.y = 0
        self.vel = 1
        self.spawn()

    def mostrar_posicion(self):
        print(f"La posició del robot és ({self.x}, {self.y})")

    def mostrar_velocidad(self):
        print(f"La velocitat del robot és de {self.vel} m/s")

    def mostrar_espacio(self):
        for fila in espai:
            print("".join(fila))


# inicialitzo el robot
walle = Robot()
executant = True

while executant and walle.estaViu:
    instruccio = input("> ")

    if instruccio == "END":
        executant = False
    elif instruccio in ("DALT", "BAIX", "ESQUERRA", "DRETA"):
        walle.mover(instruccio)
    elif instruccio == "ACCELERAR":
        walle.acelerar()
    elif instruccio == "FRENAR":
        walle.frenar()
    elif instruccio == "POSICIO":
        walle.mostrar_posicion()
    elif instruccio == "VELOCITAT":
        walle.mostrar_velocidad()
    elif instruccio == "MOSTRAR":
        walle.mostrar_espacio()
    elif instruccio == "REINICIAR":
        walle.reiniciar()