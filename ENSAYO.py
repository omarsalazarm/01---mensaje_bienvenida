'''
# ARCHIVO 01
MENSAJE = "Bienvenidos al programa de ingenieria de sistemas"

def main ():
    mostrar_mensaje (MENSAJE)

def mostrar_mensaje (mensaje):
    print (mensaje)
main ()
'''

''' 
# ARCHIVO 02
def main ():
    nombre = ingresar_texto ("Ingrese el nombre: ")
    mensaje = generar_mensaje (nombre)
    mostrar_mensaje (mensaje)
    
def ingresar_texto (parametro):
    texto = input (parametro)
    return texto

def generar_mensaje (nombre_cliente):
    mensaje_uno = f"Bienvenido {nombre_cliente} a la tienda"
    return mensaje_uno

def mostrar_mensaje (pepito):
    print (pepito)
    
main ()                   Tiempo 3:17 - 3.31 - 3:07 - 2:42 minutos
'''

''' 
# ARCHIVO 03
def main ():
    valor_trm = ingresar_entero ("Ingrese el valor TRM: ")
    mensaje = generar_mensaje (valor_trm)
    mostrar_mensaje (mensaje)

def ingresar_entero (TRM):
    valor = int(input(TRM))
    return valor

def generar_mensaje (valor_TRM):
    mensaje_uno = f"El valor de la TRM es: {valor_TRM}"
    return mensaje_uno

def mostrar_mensaje (mensaje_impreso):
    print (mensaje_impreso)

main ()
'''

'''
# ARCHIVO 04
def main ():
    temperatura = ingresar_real ("Ingrese la temperatura: ")
    mensaje = generar_mensaje (temperatura)
    mostrar_mensaje (mensaje)

def ingresar_real (vr_temperatura):
    valor = float(input(vr_temperatura))
    return valor

def generar_mensaje (temperatura_actual):
    mensaje_uno = f"La temperatura actual es: {temperatura_actual:.1f}"
    return mensaje_uno

def mostrar_mensaje (mensaje_final):
    print (mensaje_final)

main ()
'''

""" 
# ARCHIVO 05
def main ():
    cantidad_tubos = ingresar_entero ("Ingrese la cantidad de tubos: ")
    longitud_tubos = ingresar_real ("Ingrese la longitud del tubo: ")
    metros_totales = calcular_metros_totales (cantidad_tubos, longitud_tubos)
    mensaje = generar_mensaje (metros_totales)
    mostrar_mensaje (mensaje)

def ingresar_entero (cantidad):
    valor_1 = int(input(cantidad))
    return valor_1

def ingresar_real (longitud):
    valor_2 = float(input(longitud))
    return valor_2

def calcular_metros_totales (cantidad_tubos, longitud_tubos):
    longitud_total = cantidad_tubos * longitud_tubos
    return longitud_total

def generar_mensaje (longitud_total):
    mensaje = f"La longitud total de los tubos vendidos es: {longitud_total:.1f}"
    return mensaje

def mostrar_mensaje (mensaje_impreso):
    print (mensaje_impreso)

main ()
"""



































