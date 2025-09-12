# En este archivo se encuentran enunciados y resoluciones del proyecto de lógica: Katas Python

''' 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva
 un diccionario con las frecuencias de cada letra en la cadena.
 Los espacios no deben ser considerados.
'''
# Creo una función con un parámetro, la cadena de texto a introducir
def str_a_dict_frecuencias (cadena: str) -> dict[str, int]:
    """Esta función 

    Args:
        cadena (str): cadena de texto que queremos transformar

    Returns: 
        dicc: diccionario con las frecuencias de cada letra de la cadena

    Nota: no tiene en cuenta los espacios
    """
    #  creo el diccionario donde se agruparán las frecuencias
    frecuencias_cadena = {}
    
    # Con un bucle se inspecciona cada caracter y se cuenta las veces que aparece (su frecuencia)
    for caracter in cadena:
        if caracter != " ":  # Se ignoran los espacios
            if caracter in frecuencias_cadena:
                frecuencias_cadena[caracter] += 1
            else:
                frecuencias_cadena[caracter] = 1
    # El return será el resultado deseado que quiero que la función devuelva
    return frecuencias_cadena


# Compruebo el funcionamiento 
str_a_dict_frecuencias ('cadenita de prueba')

'''
2. Dada una lista de números, obtén una nueva lista con el doble de cada valor.
Usa la función map()
'''
# Creo una lista de números de la que partir
lista_inicial = [1,4,7,32,6]

# Creo una función que multiplique por 2 un número
def multiplicar_por_2 (numero):
    """Multiplicar *2

    Args:
        numero (int, float)
    
    Returns:
        numero multiplicado (float)

    """
    return numero*2
 
# La función map toma una función y un iterable, la función será multiplicar*2 y el interable la lista inicial
lista_2 = list(map(multiplicar_por_2, lista_inicial))
#incluyo list(map(...)) porque si no la función map no devuelve la lista como tal

# Compruebo el funcionamiento
print (lista_2)

# Al ser una función tan simple puedo optimizarlo haciendo una lambda 
ejercicio_2 = list(map(lambda numero: numero*2, lista_inicial))

print (ejercicio_2)


'''
3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
'''
# Creo una lista de palabras
lista_palabras = ['precepto', 'previo', 'permiso', 'expresso', 'precocinado','perfecto']

# La palabra objetivo será 'pre'
def lista_palabras_incluidas (lista, palabra_objetivo):

    """ Esta función coge una lista de palabras y selecciona aquellas en las que
    se encuentre la palabra objetivo incluida, las devuelve en otra lista

    Args:
        lista (list)
        palabra_objetivo (str)

    Returns: 
        lista de palabras que contienen la objetivo (list)
    """
    # Creo la lista que incluirá las palabras que contienen la palabra objetivo
    palabras_continentes = []

    for palabra in lista: # Hago que la función pase por todas las palabras de la lista insertada
        if palabra_objetivo in palabra: palabras_continentes.append(palabra) 
            # Y así incluya las que contengan la palabra objetivo
        else: pass # Las que no la incluyan no entrarán en la nueva lista que crea la función

    return palabras_continentes 

# Compruebo el funcionamiento
lista_palabras_incluidas (lista_palabras, 'pre')

# Al ser una función simple puedo optimizarlo usando una lambda y filter
ejercicio_3 = list(filter(lambda palabra:'pre' in palabra, lista_palabras))

print(ejercicio_3)


'''
4. Genera una función que calcule la diferencia entre los valores de dos listas.
Usa la función map()
'''
# Genero dos listas

lista_valores_1 = [1, 5, 7, 9, 13]

lista_valores_2 = [3, 9, 11, 2, 4]

# Creo la función que calculará la diferencia entre los valores de las listas
# Quiero restar cada valor y que map lo repita en los iterables
def resta (x, y):
    """_ Calcula la diferencia entre los valores de dos listas
        Args:
            lista 1 (int,float)
            lista 2 (int, float)

        Returns: 
            Diferencia (int, float)
    """
    # hago resta de valor 1 de cada lista y hago map 
    return  x - y

# Compruebo el funcionamiento
print(list(map(resta, lista_valores_1, lista_valores_2)))

# Al ser una función tan simple puedo mejorarlo haciendo una lambda

ejercicio_4 = list(map(lambda x, y : x-y, lista_valores_1, lista_valores_2))

print (ejercicio_4)


'''
5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5.
La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado.
Si es así, el estado será "aprobado", de lo contrario, será "suspenso".
La función debe devolver una tupla que contenga la media y el estado.
'''


'''

'''



'''

'''


'''

'''




'''

'''



'''

'''



'''

'''



'''

'''



'''

'''


'''

'''


'''

'''


'''

'''



'''

'''



'''

'''



'''

'''



'''

'''



'''

'''


'''

'''



'''

'''



'''

'''


'''

'''




'''

'''


'''

'''

import os
