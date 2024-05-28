"""Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años.
 Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año 
 se aplica la tasa de interés introducida.
Recordar que un capital C dolares a un interés del x por cien durante n años se convierte 
en C * (1 + x/100)elevado a n (años). Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés 
anual se convierte en 24117.14 dolares al cabo de 20 años."""

def AnnualRate():
    try:
        dollars = int(input("Introduce una cantidad de dolares: "))
        rate = float(input("Introduce uan tasa: "))
        years = int(input("Introduce un numero de años: "))
        calculate = format(dollars * (1 + rate/100)**years,".2f")
        print("Tu capital en "+str(years)+" años es "+str(calculate))
    except ValueError:
        print("El número introducido no es correcto")
        AnnualRate()

AnnualRate()