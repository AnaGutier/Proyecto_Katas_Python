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
#Genero una la lista de calificaciones de un grupo imaginario y establezco la nota del aprobado
calificaciones = [5, 3, 7.2, 8.9, 10, 2, 1.5, 4, 6.3, 7, 5.2]

def media_aprobada_o_no (calificaciones, nota_aprobado = 5):
    """Esta funcion hace la media de las calificaciones y las compara con la nota mínima para aprobar
    para así detreminar si globalmente se aprueba o no al grupo.
    
    Args:
        (list): lista de calificaciones.
        (int, float): valor por defecto 5 (posible añadir otro), nota con la que se aprueba.

    Returns: 
        (tuple): media de calificaciones y si se aprueba o no globalmente (media, estado)
    """
    # Calculo la media redondeado a 2 decimales
    media_global = round(sum (calificaciones) / len (calificaciones), 2)
    # Creo el estado aprobado o suspenso en función de la media global
    if media_global >= nota_aprobado:
        estado = 'aprobado'
    else:
        estado = 'suspenso'
    # El return así escrito devuelve automáticamente una tupla
    return media_global, estado  

# Compruebo el funcionamiento
media_aprobada_o_no (calificaciones)

# Pruebo ahora que la nota de aprobado podría cambiarse
media_aprobada_o_no (calificaciones, 7)


'''
6. Escribe una función que calcule el factorial de un número de manera recursiva.
'''
def factorial (numero):
    """Función recursiva que calcula el factorial de un número

    Args:
        numero (int)

    Return: 
        factorial (int)
    """
    # Como el factorial de 0 es por definición 1, agrego este caso concreto
    if numero == 0: 
       numero_factorial = 1
    
    else:
           numero_factorial = numero * factorial (numero - 1)
     
    return numero_factorial

# Compruebo el funcionamiento
factorial (5)


'''
7. Genera una función que convierta una lista de tuplas a una lista de strings.
Usa la función map().
'''
# Genero una lista de tuplas para la comrpobación
lista_de_tuplas = [('primera', 'tupla'), ('otra', 'más', 'aquí'), ('y', 3, 54)]

def tupla_a_lista(listita):
    """
    Convierte una lista de tuplas a lista de strings

    Args:
        listita (list): lista con tuplas

    Return:
        lista de strings (list)
    """
    lista_de_strings = []

    for elemento in listita:
        pasar_elementos_a_str = map(str, elemento)
        unir_cadenas = " ".join(pasar_elementos_a_str)
        lista_de_strings.append(unir_cadenas)

    return lista_de_strings

# Compruebo el funcionamiento
tupla_a_lista(lista_de_tuplas)

# Podría realizarse con una lambda
def ejercicio_7 (listita):
    
    nueva_lista = list(map(lambda elemento: " ".join(map(str, elemento)), listita))

    return nueva_lista

ejercicio_7 (lista_de_tuplas)

'''
8. Escribe un programa que pida al usuario dos números e intente dividirlos.
Si el usuario ingresa un valor no numérico o intenta dividir por cero,
maneja esas excepciones de manera adecuada.
Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
'''




'''
9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España.
La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
Usa la función filter()
'''
# Creo una lista de mascotas
mascotas_varias = ["Cabra", "Perro", "Tigre", "Vaca", "Serpiente Pitón", "Gato", "Cocodrilo", "Oso"]

def filtrar_mascotas(mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # filter mantiene solo los elementos que cumplen la condición
    return list(filter(lambda elemento: elemento not in mascotas_prohibidas, mascotas))

#Compruebo el funcionamiento 
filtrar_mascotas (mascotas_varias)


'''
10. Escribe una función que reciba una lista de números y calcule su promedio.
Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
'''
numeritos = [6, 72, 14, 3, 12]
lista_de_nada = []

def promedio (lista):
    if len(lista) == 0: 
        promedio = 'La lista de números no contiene datos, por favor incluye algunos para calcular el promedio'

    else: 
        promedio = round(sum(lista) / len(lista), 2) #Redondeo el resultado para evitar decimales innecesarios

    return promedio

# Compruebo el funcionamiento 
promedio (numeritos)
promedio (lista_de_nada)


'''
11. Escribe un programa que pida al usuario que introduzca su edad.
Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado
(por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
'''



'''
12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra.
Usa la función map().
'''



'''
13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
Las letras no pueden estar repetidas. Usa la función map(). 
'''
# Genero una lista de palabras
caracteres = 'frasecita'

def letras_mayus_minus(conjunto):
    """
    Devuelve una lista de tuplas con cada letra en mayúsculas y minúsculas sin repetir letras.

    Args:
        conjunto (str) = conjunto de caracteres

    Return: 
        (list)
    """
    # Creo un conjunto para evitar duplicados
    letras = set(conjunto)
    
    # Uso map() para transformar cada letra en una tupla
    resultado = list(map(lambda c: (c.upper(), c.lower()), letras))
    
    return resultado

# Compronación
letras_mayus_minus(caracteres)
letras_mayus_minus('cualquiera')

'''
14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico.
Usa la función filter().
'''
# Genero una lista de palabras 
palabras = ["correr", "programar", "casco", "portada", "juego", "pecera"]

def palabras_por_letra(lista, letra):
    """
    Retorna las palabras que comienzan con una letra específica.
    
    """
    return list(filter(lambda palabra: palabra.startswith(letra), lista))

# Comprobación
palabras_por_letra(palabras, 'p')
palabras_por_letra(palabras, 'c') 

'''
15. Crea una función lambda que sume 3 a cada número de una lista dada.
'''
# Creo una lista de números para la comprobación
numeros = [1, 2, 3, 4, 5]
def sumar_3 (numeros):
    nueva_lista = list(map(lambda x: x + 3, numeros))
    return nueva_lista
# Compruebo el funcionamiento
sumar_3 (numeros)

# En una sola línea
nueva_lista = list(map(lambda x: x + 3, numeros))
print(nueva_lista)

'''
16. Escribe una función que tome una cadena de texto y un número entero n como parámetros
y devuelva una lista de todas las palabras que sean más largas que n.
Usa la función filter().
'''
# Genero una cadena para la comprobación
frase = "Tengo un perro de pelo largo"

def palabras_mas_largas(cadena, n):
    """
    De una lista de strings devuelve las de longitud mayor que n.

    Args (str): 
        cadena de palabras

    Return (list(str)):
        palabras con len>n
    """
    palabras = cadena.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))


# Comprobación
print(palabras_mas_largas(frase, 4))


'''
17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
Por ejemplo, [5,7,2] corresponde al número quinientos setenta y dos (572).
Usa la función reduce().
'''
# Creo la lista para la comprobación
numeros_separados = [3, 2, 1, 7]

# Primero importo la función reduce
from functools import reduce

def juntar_numeros (lista): 
    """ Une en uno sólo los números de una lista

    Args:
        lista (list): lista de números separados

    Return:
        numero unido (int)
    """
    
    return reduce(lambda x,y:x*10 + y, lista)
#De esta forma se coje el dígito de la lsita y se multiplica *10 sumando así el siguiente, resultando unidos

juntar_numeros (numeros_separados)



'''
18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación)
y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. 
sa la función filter().
'''



'''
19. Crea una función lambda que filtre los números impares de una lista dada.
'''
# Creo la lista para la comrpobación
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def impares (numeros): 
    numeros_impares = list(filter(lambda x: x % 2 != 0, numeros))
    # La lambda identidica los números pares o impares en función de la división
    #filter selecciona los que cimplen la condición y con list se pasan al formato lista
    return numeros_impares

#Comprobación
impares (numeros)

'''
20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
filter()
'''
# Creo la lista para la comprobación
lista_variada = ['cadena', 7, 3.2, 'cadenita', 32, 'cadenota', 5, 11] 

def seleccionar_int (lista):
    """ Selecciona los valores int de la lista y crea una nueva con estos

    Args:
        lista (lista de int y str): Lista de elementos int y str
    Return:
        lsita_int (list): lsita de sólo int
    """
    #isinstance evalua si el elemento es int, si es true filter lo acepta para pasarlo a la lista
    return list(filter(lambda elemento: isinstance(elemento, int), lista))

seleccionar_int (lista_variada)


'''
21. Crea una función que calcule el cubo de un número dado mediante una función lambda
'''


'''
22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.
Usa la función reduce().
'''
lista_numerica = [1, 3, 6, 9]
def producto_total (lista_numeros):
    """Multiplica todos los numeros de una lsita entre sí

    Args:
        lista_numeros (lsit): lista sólo con números
    Return:
        producto (int, float): un único número
    """
    # Reduce importada previamente
    # La lambda multiplica los elementos y reduce repite este en todo el iterable
    return reduce(lambda x, y: x*y, lista_numeros) 
producto_total (lista_numerica)

'''
23. Concatena una lista de palabras.Usa la función reduce().
'''
lista_de_palabras = ['voy','a', 'concatenar', 'esto']

def concatenar_palabras (lista_a_concatenar):
    """ De una lista de cadenas devuelve una cadena única con espacios entre estas
    Args:
        lista_a_concatenar (list): lista de str
    Return:
        lista_concatenada (str): cadena unida
    """
    lista_concatenada = reduce(lambda x, y: str(x) + ' ' + str(y), lista_a_concatenar)
    # Cambio el tipo de los elementos de la lsita a str y unos uno con un espacio de por medio
    return lista_concatenada

# Comprobación
concatenar_palabras(lista_de_palabras)

'''
24. Calcula la diferencia total en los valores de una lista. Usa la función reduce().
'''
list = [3, 5, 7, 4, 2, 10]
#La lambda calcula la difernecia entre los primeros valores de la lista y reduce lo repite en todos los elementos existentes
print (reduce (lambda x, y: x - y, list))

'''
25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
'''
variable_cadena = 'cadena de texto cualquiera'

def contar_caracteres (cadena):
    """Cuenta los caracteres de una cadena

    Args:
        cadena (_type_): _description_
    """
    return len(cadena) #La función len() indica los caracteres que tiene una cadena 

#Comprobación con variable y cadena directamente
contar_caracteres ('cinco')
contar_caracteres (variable_cadena) 

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
