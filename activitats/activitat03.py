
columnas = 20
filas = 20
VELOCIDAD_MAXIMA = 5
POSICION_INICIAL = (0, 0)
VELOCIDAD_MINIMA = 0
pared = " \uD83E\uDDF1"
robot = " \uD83E\uDD16"

espai = [[ pared for c in range(columnas)] for f in range(filas)]


class Robot:
    def __init__(self, x=0, y=0, vel=1):
        self.x = x
        self.y = y
        self.vel = vel

    def spawn(self):
        espai[self.y][self.x] = robot    

    def mover(self, direccion):
        if direccion == "DALT" and self.y > 0:
            self.y -= self.vel
        elif direccion == "BAIX" and self.y < filas - 1:
            self.y += self.vel
        elif direccion == "ESQUERRA" and self.x > 0:
            self.x -= self.vel 
        elif direccion == "DRETA" and self.x < columnas - 1:
            self.x += self.vel
        espai[self.y][self.x] = robot   

    def acelerar(self):
        if self.vel < VELOCIDAD_MAXIMA:
            self.vel +=1
        
    def frenar(self):
        if self.vel > VELOCIDAD_MINIMA:
            self.vel -= 1
        
    def mostrar_posicion(self):
        print(f"Posición del robot: ({self.x}, {self.y})")
        
    def mostrar_velocidad(self):
        print(f"Velocidad del robot: {self.vel}")
    
    def mostrar_espacio(self):
        for fila in espai:
            print("".join(fila))    



