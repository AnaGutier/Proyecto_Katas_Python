# Ejercicio_8: 
def dividir ():
    """
    Se le piden dos numeros al usuario para dividirlos
    Si se ingresa un valor no numérico se responde: ''ArithmeticError
    Si se intenta dividir entre 0 se responde: ''

    Input:
        num_1 (float)
        num_2 (float)

    Return:
        resultado (float)
    """
    try: # pido al usuario que introduca los números y que estos se reconozcan como tales
        num_1 = float(input('Introduce el primer número: '))
        num_2 = float(input('Introduce el segundo número: '))
        resultado = num_1 / num_2 # realizo la división   
    except ValueError:
        # Caso 1: no se introduce un número
        print('Error: Debes introducir valores numéricos.')

    except ZeroDivisionError:
        # Caso 2: división por cero
        print('Error: No se puede dividir entre cero. Inserta otro número.')

    else:
        # Solo se ejecuta si NO hubo errores
        print(f'La división fue exitosa. Resultado: {resultado}')

# Para comprobarlo uso:
#  if __name__ == "__main__":
    # dividir()
# Lo dejo como comentario para no llamar a la función e ir probando siguientes ejercicios

def preguntar_edad ():
    """
    Se pregunta la edad al usuario, si es correcto se responde: 'Genial, ya veo que tienes {edad_usuario} años'
        si inserta un valor no numérico se responde: 'Error: por favor, inserta únicamente el numero de años que tienes'
        si inserta un valor que no esté entre 0 y 120 se responde: 'Error: por favor, inserta un número valido'

    Input:
        edad_usuario (int)

    Return:
        resultado (str f'texto' + {int}) 
    """

    try: # pido al usuario que introduca su edad
        edad_usuario = round(int(input('Introduce tu edad:'))) 
        # uso int para que en caso de numeros negativos o 0 de Value Error
        # compruebo el rango
        if edad_usuario < 120:
            print('Error: por favor, inserta un número válido')
        
        else:
            print(f'Genial, ya veo que tienes {edad_usuario} años')
        
    except ValueError:
        # Caso 1: no se introduce un número, o este es 0 o negativo
        print('Error: por favor, inserta únicamente el numero de años que tienes.')

#if __name__ == "__main__":
    #preguntar_edad()

def buscar_nombres():
    """ Pide al usuario una lista de nombres y luego un nombre para buscarlo en esa misma lista
        Si se encuentra el nombre se escribe: '¡Genial! El nombre "{nombre_a_buscar}" se encuentra en la lista'
        Si no se encuentra se escribe: 'Lo siento, el nombre "{nombre_a_buscar}" no se encuentra en la lista'
    """
    # Pido al usuario la lista 
    lista_usuario = input ('Escribe la lista de nombres que desees (deben estar separados por comas):')
    # Establezco la coma como separador limpiando los espacios
    nombres = [nombre.strip() for nombre in lista_usuario.split(",")] 

    # Pido el nombre que busacar en la lista
    nombre_a_buscar = input('Escribe el nombre que quieres buscar en la lista: ').strip()
    # Compruebo si el nombre está en la lista
    if nombre_a_buscar in nombres: 
        print(f'¡Genial! El nombre "{nombre_a_buscar}" se encuentra en la lista')

    else: 
        print(f'Lo siento, el nombre "{nombre_a_buscar}" no se encuentra en la lista')
    
#if __name__ == "__main__":
    #buscar_nombres()

