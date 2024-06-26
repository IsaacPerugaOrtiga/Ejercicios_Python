"""Este programa pide primeramente la cantidad total de compras de una persona. 
Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción. 
Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa 
genera de forma aleatoria un número entero del cero al cinco. Cada número corresponderá a un 
color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibirá como premio. 
Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, 
sí se aplicará un descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre 
el total de compra que introdujo inicialmente el usuario, 
de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento."""

import random

def getTotalQuantity(quantity:int):
    if quantity >= 100:
        print('su gasto iguala o supera los $100.00 y por tantoparticipa en la promoción.'.capitalize())
        # Definimos las listas con los nombres y los descuentos
        colores = ["BOLA BLANCA", "BOLA ROJA", "BOLA AZUL", "BOLA VERDE", "BOLA AMARILLA"]
        descuentos = ["NO TIENE", "10 POR CIENTO", "20 POR CIENTO", "25 POR CIENTO", "50 POR CIENTO"]
        # Título de las columnas
        print(f"{'COLOR':<20}{'DESCUENTO'}")

        # Iteramos a través de los colores y los descuentos para imprimirlos alineados
        for color, descuento in zip(colores, descuentos):
            print(f"{color:<20}{descuento}")
        return quantity 
    else:
        print('La cantidad introducida no supera los $100.00 y no se puede efectuar ninguna acción')
        exit()
        
        

class Ball:
    def __init__(self,color,discount):
        self.color = color
        self.discount = discount

    def __str__(self):
       return f"{self.color} {self.discount}"


def randomBall(quantity:int):
    ball = Ball("BLANCA",0)
    ball2 = Ball("ROJA",10)
    ball3 = Ball("AZUL",20)
    ball4 = Ball("VERDE",25)
    ball5 = Ball("AMARILLA",50)
    ball_list = []
    ball_list.append(ball)
    ball_list.append(ball2)
    ball_list.append(ball3)
    ball_list.append(ball4)
    ball_list.append(ball5)
    y = 0
    chosenBall = Ball("",0)
    for i in ball_list:
        y = random.randrange(5)
        chosenBall = ball_list[y]
    print("ALEATORIAMENTE USTED OBTUVO UNA BOLA " + chosenBall.color)
    print("FELICIDADES, HA GANADO UN " + str(chosenBall.discount) + " DE DESCUENTO")
    print("SU NUEVO TOTAL A PAGAR ES: "+str(quantity * (chosenBall.discount*0.01)))
    decision = str(input("SI DESEA SALIR PULSE 1 O DE LO CONTRARIO PULSE OTRA TECLA: "))
    while decision != "1":
        quantity = int(input('Introduzca la cantidad total de la compra: ').capitalize())
        getTotalQuantity(quantity)       
        randomBall(quantity)
    else:
        exit()
        

quantity = int(input('Introduzca la cantidad total de la compra: ').capitalize())
getTotalQuantity(quantity)       
randomBall(quantity)