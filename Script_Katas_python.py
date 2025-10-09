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
            # Hago que el número se multiplique por el numero -1 recurriendo a la propia función
            # Así la función recorre todos los numeros menores que el insertado
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
    # Creo la lista donde incluiré todos los strings
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
    # List convierte al formato listo el map que ha recorrido las variables
    return nueva_lista

ejercicio_7 (lista_de_tuplas)

'''
8. Escribe un programa que pida al usuario dos números e intente dividirlos.
Si el usuario ingresa un valor no numérico o intenta dividir por cero,
maneja esas excepciones de manera adecuada.
Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
'''
def dividir ():
    """
    Se le piden dos numeros al usuario para dividirlos
    Si se ingresa un valor no numérico se responde: ''ArithmeticError
    Si se intenta dividir entre 0 se responde: ''

    Input:
        num_1 (float)
        num_2 (float)

    Return:
        resultado (str f'texto' + {float}) 
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
    
# Comprobación realizada en un archivo.py incluido en el repositorio al necesitar inputs

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
    # filter mantiene solo los elementos que cumplen la condición de que el elemento no esté en la lista prohibida
    return list(filter(lambda elemento: elemento not in mascotas_prohibidas, mascotas))

#Compruebo el funcionamiento 
filtrar_mascotas (mascotas_varias)


'''
10. Escribe una función que reciba una lista de números y calcule su promedio.
Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.
'''
# Creo las listas para comprobar el resultado
numeritos = [6, 72, 14, 3, 12]
lista_de_nada = []

def promedio (lista):
    if len(lista) == 0: # En caso de que no haya datos, envío un mensaje
        promedio = 'La lista de números no contiene datos, por favor incluye algunos para calcular el promedio'

    else: 
        promedio = round(sum(lista) / len(lista), 2) #Hago la media (suma de elementos entre la cantidad de estos) y redondeo

    return promedio

# Compruebo el funcionamiento 
promedio (numeritos)
promedio (lista_de_nada)


'''
11. Escribe un programa que pida al usuario que introduzca su edad.
Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado
(por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.
'''
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
        if 0 <= edad_usuario <= 120:
            print(f'Genial, ya veo que tienes {edad_usuario} años')
        
        else:
            print('Error: por favor, inserta un número válido')
        
    except ValueError:
        # Caso 1: no se introduce un número, o este es 0 o negativo
        print('Error: por favor, inserta únicamente el numero de años que tienes.')

# Comprobación realizada en un archivo.py incluido en el repositorio al necesitar inputs


'''
12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra.
Usa la función map().
'''
def longitudes_palabras(frase):
    # Divido la cadena en palabras, examino la longitud de todas usando map y lo convierto en lista
    return list(map(len, frase.split()))

# Comprobación
print(longitudes_palabras('hola qué tal'))  

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
     # startswith() selecciona las cadenas que empiecen con la letra seleccionada
    # la lambada repite eso con toda la lista y filter evalua los true para que list los ponga en una nueva lista
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
    # list hace que se nos devuelva una lista
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
    De una cadena devuelve los elementos de longitud mayor que n

    Args (str): 
        cadena de palabras

    Return (list(str)):
        palabras con len>n
    """
    palabras = cadena.split() # Secciono las palabras según los espacios
    # La lambda recorre las palabras comparando su longitud con 'n' 
    # List convierte a una lista los valores que filter pasa por true 
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
def filtrar_estudiantes():
    # Lista de diccionarios con estudiantes
    estudiantes = [ #Pongo el dicc dentro de la función porque se inica que el programa debe crear la lista
        {"nombre": "Ana", "edad": 25, "calificación": 95},
        {"nombre": "Marta", "edad": 20, "calificación": 88},
        {"nombre": "Alvarito", "edad": 18, "calificación": 92},
        {"nombre": "Pau", "edad": 27, "calificación": 75},
    ]
    
    # Usamo filter para calificación >= 90
    sobresalientes = list(filter(lambda est: est["calificación"] >= 90, estudiantes))
    
    return sobresalientes


# Comprobación
print(filtrar_estudiantes())

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

# Inciso: Estas funciones las puedo guardar en def () para mantenerlas en el script y poder recurrir a ellas
# si fuera necesario, pero podrían funcionar en una sóla línea sin guardarse posteriormente
# esta por ejemplo sería:
#       lista_variada = ['cadena', 7, 3.2, 'cadenita', 32, 'cadenota', 5, 11] 
#       print(list(filter(lambda elemento: isinstance(elemento, int), lista_variada)))

'''
21. Crea una función que calcule el cubo de un número dado mediante una función lambda
'''
# Una funciones tan simples como esta (y alguna posterior) no la guardaré con def() para aligerar el código
# En otros casos puede resultarme útil tener las funciones guardadas y desarrolladas para usar posteriormente
cubo = lambda x: x ** 3
print(cubo(3))  # 27


'''
22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.
Usa la función reduce().
'''
lista_numerica = [1, 3, 6, 9]
# Reduce importada previamente
# La lambda multiplica los elementos y reduce repite este en todo el iterable
print(reduce(lambda x, y: x*y, lista_numerica))

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
ejercicio_24 = [10, 4, 3, 1]
# Reduce repite la resta de los dos primeros números con el siguiente de la lista
resultado = reduce(lambda x, y: x - y, ejercicio_24)
print(resultado)

'''
25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
'''
# En este caso al generar una def() podré usarlo con variables o cadenas directamente
ejercicio_25 = 'cadena para contar caracteres'
def contar_caracteres (cadena):
    """Cuenta los caracteres de una cadena

    Args:
        cadena (_type_): _description_
    """
    return len(cadena) #La función len() indica los caracteres que tiene una cadena 
#Comprobación con variable y cadena directamente
contar_caracteres (ejercicio_25)
contar_caracteres ('cinco')

'''
26. Crea una función lambda que calcule el resto de la división entre dos números dados.
'''
def calcular_resto (numero, numerito): # Con % recibo el resto de la dvisión
    return numero % numerito

# En una única línea
calcular_resto = lambda x, y: x % y

'''
27. Crea una función que calcule el promedio de una lista de números. 
'''
# Creo una lista para la comprobacion
ejercicio_27 = [3, 6, 9, 18]

def media (lista):
    return sum(lista) / len(lista) #Hago sumo los elementos de la lista y divido entre la cantidad de estos

# Comprobación
media (ejercicio_27)

'''
28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
'''
ejercicio_28 = [3, 6, 82, 5, 3, 82, 7] 
sin_duplis = [3, 6, 7] 

def primer_dupli (lista):
    """ Encuentra el primer duplicado unicamente 
    Args:
        lista (list): _description_
    
    Return: 
        primer_duplicado (___________________): primer elemento duplicado de la lista
    """
    vistos = [ ] # Creo una lista vacía donde se irán añadiendo los elementos
    
    for elemento in lista: # Recorro en orden la lista con el bucle
        if elemento in vistos: 
            return elemento # El primer elemento que se repite, la función lo devuelve
        vistos.append(elemento)
    
    return print ('No hay duplicados') # Respuesta en caso de que no haya duplicados

# Comprobación
primer_dupli (ejercicio_28)
primer_dupli (sin_duplis)

'''
29. Crea una función que convierta una variable en una cadena de texto y enmascare
todos los caracteres con el carácter '#', excepto los últimos cuatro.
'''
def ocultar_menos4(variable):
    """
    Convierte la variable en cadena y enmascara todos los caracteres con '#'
    excepto los últimos cuatro.
    """
    texto = str(variable)
    
    if len(texto) <= 4:
        return texto  # Como los últimos 4 caracteres no se enmascaran, devuelvo la variable tal cual
    
    else:
        return "#" * (len(texto) - 4) + texto[-4:] 
        # Convierto todo el texto -4 por #### y añado los últimos 4 últimos elementos del texto


# Compronación
print(ocultar_menos4(123456789))
print(ocultar_menos4("abcdefg"))
print(ocultar_menos4("123"))

'''
30. Crea una función que determine si dos palabras son anagramas, es decir,
si están formadas por las mismas letras pero en diferente orden.
'''
# Creo variables para comprobar el funcionamiento de la función
anagrama_1 = 'Lobos'
anagrama_2 = 'Bolos'
anagrama_falso = 'bingo'

def evaluar_anagramas (palabra_1, palabra_2):
    """ Compara cadenas de texto para saber si son anagramas
    Args:
        palabra_1, palabra_2 (str): cadenas de texto
    Return:
        (bool): True si son anagramas, False si no lo son
    """
    # Convierto las palabras en sets de letras
    # Incluyo .lower() para que no se identifiquen como diferentes una misma letra en mayúsculas y minúsculas
    # En un set el orden de los elementos no importa, así podemos comparar las letras indistintamente
    if (set(palabra_1.lower())) == set(palabra_2.lower()):
        print (f'{palabra_1} y {palabra_2} son anagramas')
    else: 
        print (f'{palabra_1} y {palabra_2} no son anagramas')   

# Compruebo el funcionamiento 
evaluar_anagramas (anagrama_1, anagrama_2)
evaluar_anagramas (anagrama_1, anagrama_falso)

'''
31. Crea una función que solicite al usuario ingresar una lista de nombres y luego
solicite un nombre para buscar en esa lista. Si el nombre está en la lista,
se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.
'''
def buscar_nombres():
    """ 
    Pide al usuario una lista de nombres y luego un nombre para buscarlo en esa misma lista:
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

'''
32. Crea una función que tome un nombre completo y una lista de empleados,
busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista,
de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
'''
mis_empleados = [
    {'nombre': 'Ana Gutiérrez', 'puesto': 'Analista de datos'},
    {'nombre': 'Paula López', 'puesto': 'Comunicadora'},
    {'nombre': 'Alvarito Castro', 'puesto': 'Matemático'}
]

def buscar_puesto(nombre_completo, lista_de_empleados):
    """
    Busca el nombre completo en la lista de empleados y devuelve el puesto.
    Si no se encuentra, devuelve un mensaje indicando que no trabaja aquí.

    Args:
        nombre_completo (str): nombre del empleado/a
        lista_de_empleados (dicc): grupo de empleados

    Reurn:
        Si el nombre es correcto (str): f'El puesto de {nombre_completo} es {puesto}')
        Si no lo es (str): f'{nombre_completo} no trabaja aquí.'
    """
    for emp in lista_de_empleados:
        if emp['nombre'] == nombre_completo:
            return f'El puesto de {nombre_completo} es {emp['puesto']}'
    
    return f'{nombre_completo} no trabaja aquí.'

# Comprabación
buscar_puesto ('Paula López', mis_empleados)
buscar_puesto ('Jaimito', mis_empleados)

'''
33. Crea una función lambda que sume elementos correspondientes de dos listas dadas
'''
# De nuevo no guardo la función como def y la uso con la lambda sólo en esta variable
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))
# La lambda suma los elementos y map lo repite uno tras otro. List hace que se devuelva una lista

# Comprobación
print(sumar_listas([1, 2, 3], [4, 5, 6])) 

'''
34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol.

Código a seguir:
    1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
    2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
    3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
    6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.

Caso de uso:
    1. Crear un árbol.
    2. Hacer crecer el tronco del árbol una unidad.
    3. Añadir una nueva rama al árbol.
    4. Hacer crecer todas las ramas del árbol una unidad.
    5. Añadir dos nuevas ramas al árbol.
    6. Retirar la rama situada en la posición 2.
    7. Obtener información sobre el árbol.
'''
class Arbol: #Creo la clase
    """
    Clase que representa a un arbol, con tronco y ramas.

    Métodos disponibles: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol
    """
    def __init__(self, tronco = 1.0, ramas=None):
         """ 
        Método constructor
        Args:
            tronco (float): número de metros que tiene el tronco del árbol (por defecto 1.0)
            ramas (lsit): lsita de ramas y longitud de estas (lista vacía por defecto)
        """
         self.tronco = float(tronco)
         self.ramas = list(ramas) if ramas is not None else []

    def crecer_tronco(self, cantidad = 1.0):
        """
        Método que hace crecer el tronco en `cantidad` (por defecto 1) y devuelve la nueva longitud del tronco.
         Args:
            centidad (float) = cantidad que crece el tronco 
         Return: 
            self.tronco (float) = nueva longitud del tronco
        """
        self.tronco += float(cantidad)
        return self.tronco

    def nueva_rama(self, longitud = 1.0):
        """
        Método que añade una nueva rama con longitud `longitud` (por defecto 1) y devuelve el número actual de ramas.
         Args:
            longitud (float) = nueva rama de longitud indicada o 1 por defecto
         Return: 
            len(self.ramas) (float) = nueva cantidad de ramas
        """
        self.ramas.append(float(longitud)) # El append añade la nueva rama a la lista
        return len(self.ramas)

    def crecer_ramas(self, cantidad = 1.0):
        """
        Método para hacer crecer todas las ramas en la cantidad indicada (por defecto 1) y devuelve la lista actualizada de longitudes de ramas.
        Args:
            cantidad (float) = cantidad que crecen las ramas
         Return: 
            self.ramas (list) = nueva lista con las diferentes ramas
        """
        self.ramas = [r + float(cantidad) for r in self.ramas] #Itero la lista para sumar a todas las ramas la longitud nevesaria
        return self.ramas

    def quitar_rama(self, posicion):
        """
        Método que quita la rama en la posición indicada (1-based) y devuelve la longitud de la rama eliminada.
        Si la posicion no es válida, lanza IndexError.
        Args:
            posicion (int) = posición de la rama a eliminar en la lista
         Return: 
            rama_eliminada (list) = nueva lista con las diferentes ramas
        """
        indice = posicion - 1
        if indice < 0 or indice >= len(self.ramas): #Para el caso de que se intente quitar una rama en posición no válida
            raise IndexError(f'Posición fuera de rango. Debe estar entre 1 y {len(self.ramas)}.') 
        rama_eliminada = self.ramas.pop(indice) # Si no hay problemas, el pop saca la rama de la lista
        return rama_eliminada 

    def info_arbol(self):
        """
        Se devuelve un diccionario con la información del árbol:
         - tronco: longitud del tronco
         - numero_ramas: cantidad de ramas
         - longitudes_ramas: lista de longitudes de cada rama

        Además se devuelve una versión en string en la clave 'descripcion'.
        """
        info = {
            'tronco': self.tronco,
            'numero_ramas': len(self.ramas),
            'longitudes_ramas': list(self.ramas)
        } # Así genero el diccionario con toda la información, lo mantengo porque podría ser interesante trabajar con este formato posteriormente
        descripcion = (f'El tronco mide {self.tronco} unidades, '
                       f'tiene {len(self.ramas)} rama(s) con longitudes {self.ramas}.') # Pongo una cadena con toda la información para que sea más legible, mantenieno el dicc por lo comentado anteriormente
        info['descripcion'] = descripcion 
        return info


# Uso de ejemplo 
# 1. Crear un árbol.
arbolito = Arbol()  # Creo el árbol por defecto: con tronco=1.0 y ramas=[]

# 2. Hacer crecer el tronco del árbol una unidad. 
arbolito.crecer_tronco() # No añado variable porque por defecto indiqué que creciera 1 

# 3. Añadir una nueva rama al árbol.
arbolito.nueva_rama() # No añado variable porque por defecto indiqué añadir 1 rama

# 4. Hacer crecer todas las ramas del árbol una unidad.
arbolito.crecer_ramas() # No añado variable porque por defecto indiqué que crecieran 1 

# 5. Añadir dos nuevas ramas al árbol.
arbolito.nueva_rama(2)

# 6. Retirar la rama situada en la posición 2.
eliminada = arbolito.quitar_rama(2)
print(f'Yo he quitado la rama de longitud: {eliminada}')

# 7. Obtener información sobre el árbol.
info = arbolito.info_arbol()
print('Información final del árbol:')
print(info['descripcion'])
# Si quiero el diccionario podría pedirlo con:
print(info)


'''
36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

Código a seguir:
    1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
    2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
    3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.Lanzará un error en caso de no poder hacerse.
    4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

Caso de uso:
    1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    2. Agregar 20 unidades de saldo de "Bob".
    3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
    4. Retirar 50 unidades de saldo a "Alicia".
'''
class UsuarioBanco: # Creo la clase
    """
    Clase que representa a un usuario de un banco con nombre, saldo y cuenta corriente.
    
    Métodos disponibles: retirar_dinero , transferir_dinero , agregar_dinero
    """
    def __init__(self, nombre, saldo = 0.0, cuenta_corriente = False):
        """ 
        Método constructor
        Args:
            nombre (str): nombre del usuario
            saldo (float): cantidad de dinero inicial (por defecto 0.0)
            cuenta_corriente (bool): indica si tiene cuenta corriente (True o False, por defecto False)
        """
        self.nombre = str(nombre)
        self.saldo = float(saldo)
        self.cuenta_corriente = bool(cuenta_corriente)

    def retirar_dinero(self, cantidad):
        """
        Método que retira dinero del saldo del usuario.
        Si no hay saldo suficiente o no tiene cuenta corriente, lanza un error.
        Args:
            cantidad (float): dinero a retirar
        Return:
            self.saldo (float): saldo restante tras la operación
        """
        if not self.cuenta_corriente:
            raise ValueError(f'El usuario {self.nombre} no tiene cuenta corriente')
        if cantidad > self.saldo:
            raise ValueError(f'Saldo insuficiente para retirar {cantidad}')
        self.saldo -= float(cantidad)
        return self.saldo

    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Método que transfiere dinero desde otro usuario hacia este usuario.
        Si no hay saldo suficiente en el otro usuario o no tiene cuenta corriente, lanza un error.
        Args:
            otro_usuario (UsuarioBanco): usuario desde el que se transfiere
            cantidad (float): dinero a transferir
        Return:
            self.saldo (float): nuevo saldo del usuario que recibe la transferencia
        """
        if not otro_usuario.cuenta_corriente:
            raise ValueError(f'El usuario {otro_usuario.nombre} no tiene cuenta corriente')
        if cantidad > otro_usuario.saldo:
            raise ValueError(f'El usuario {otro_usuario.nombre} no tiene saldo suficiente')
        otro_usuario.saldo -= float(cantidad)
        self.saldo += float(cantidad)
        return self.saldo

    def agregar_dinero(self, cantidad):
        """
        Método que agrega dinero al saldo del usuario.
        Args:
            cantidad (float): dinero a añadir
        Return:
            self.saldo (float): nuevo saldo tras la operación
        """
        if not self.cuenta_corriente:
            raise ValueError(f'El usuario {self.nombre} no tiene cuenta corriente')
        self.saldo += float(cantidad)
        return self.saldo

# Caso de uso

# 1. Creo los dos usuarios
Alicia = UsuarioBanco('Alicia', saldo = 100, cuenta_corriente = True) #Creo a Alicia con 100
Bob = UsuarioBanco('Bob', saldo = 50, cuenta_corriente = True) #Creo a Bob con 50

# 2. Agrego 20 unidades de saldo de Bob
Bob.agregar_dinero(20)
print(f'Bob ahora tiene {Bob.saldo}')

# 3. Hago una transferencia de 80 unidades desde Bob a Alicia
Alicia.transferir_dinero(Bob, 80)
print(f'Alicia ahora tiene {Alicia.saldo} y Bob tiene {Bob.saldo}')

# 4. Retiro 50 unidades de saldo a Alicia
Alicia.retirar_dinero(50)
print(f'Alicia ahora tiene {Alicia.saldo}')

'''
37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras,
reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto.

Código a seguir:
    1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto.
    Tiene que devolver un diccionario.
    2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva.
    Tiene que devolver el texto con el remplazo de palabras.
    3. Crear una función eliminar_palabra para eliminar una palabra del texto.
    Tiene que devolver el texto con la palabra eliminada.
    4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar")
    y un número de argumentos variable según la opción indicada.

Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto
'''
# Primero defino la función para contar las palabras
def contar_palabras(texto):
    """
    Función que cuenta cuántas veces aparece cada palabra en el texto.
    Args:
        texto (str): texto de entrada
    Return:
        dict: diccionario con palabras como claves y número de apariciones como valores
    """
    # Divido el texto en palabras separadas por espacios
    palabras = texto.split()
    conteo = {} # Genero el diccionario
    # Recorro cada palabra y voy sumando en el diccionario
    for palabra in palabras:
        palabra = palabra.strip('.,!?;:').lower() # Quito signos básicos y todo paso a minúsculas para sistematizarlo
        if palabra in conteo: # Hago el conteo de palabras y
            conteo[palabra] += 1 # Las sumo si se repiten
        else:
            conteo[palabra] = 1 # Si sólo salen una vez, saldrá 1 como numero de apariciones 
    return conteo


# Defino la función para reemplazar palabras
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Función que reemplaza una palabra por otra en el texto.
    Args:
        texto (str): texto de entrada
        palabra_original (str): palabra que quiero reemplazar
        palabra_nueva (str): palabra por la que se reemplaza
    Return:
        str: texto con el reemplazo hecho
    """
    # Uso replace para cambiar todas las ocurrencias
    return texto.replace(palabra_original, palabra_nueva)


# Defino la función para eliminar palabras
def eliminar_palabra(texto, palabra_eliminar):
    """
    Función que elimina una palabra específica del texto.
    Args:
        texto (str): texto de entrada
        palabra_eliminar (str): palabra que quiero eliminar
    Return:
        (str): texto con la palabra eliminada
    """
    palabras = texto.split()
    palabra_eliminar_norm = palabra_eliminar.strip('.,!?;:').lower()
    nuevas_palabras = []
    # Recorro las palabras originales; comparo cada palabra en lower
    # y sólo añado a nuevas_palabras la que NO coincida con la palabra a eliminar.
    for p in palabras:
        p_norm = p.strip('.,!?;:').lower()
        if p_norm == palabra_eliminar_norm:
            # ignoro la palabra introducida (la elimino)
            continue
        else:
            # Conservo la palabra tal cual (con su puntuación)
            nuevas_palabras.append(p)
    # Uno las palabras otra vez en un texto
    return ' '.join(nuevas_palabras)


# Creo la función principal que llama a las anteriores
def procesar_texto(texto, opcion, *args):
    """
    Función que procesa un texto según la opción indicada: contar, reemplazar o eliminar.
    Args:
        texto (str): texto de entrada
        opcion (str): tipo de operación ("contar", "reemplazar" o "eliminar")
        *args: argumentos adicionales dependiendo de la opción
    Return:
        resultado variable: diccionario o texto modificado
    """
    if opcion == 'contar':
        return contar_palabras(texto)
    elif opcion == 'reemplazar':
        if len(args) != 2: # Lanzo un error si no se insertan los valores necesarios
            raise ValueError('Para reemplazar necesito palabra_original y palabra_nueva')
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == 'eliminar':
        if len(args) != 1:
            raise ValueError('Para eliminar necesito palabra_eliminar') # De nuevo un error si no se inserta lo necesario
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError('Opción no válida. Usa "contar", "reemplazar" o "eliminar".')


# Caso de uso
mi_texto = 'Hola, buen día. Hoy es un día soleado. Que el día sea soledao me hace feliz.'

# 1. Contar palabras
print('Contar palabras:')
print(procesar_texto(mi_texto, 'contar'))

# 2. Reemplazar palabra
print('Reemplazar palabra:')
print(procesar_texto(mi_texto, 'reemplazar', 'feliz', 'bailar'))

# 3. Eliminar palabra
print('Eliminar palabra:')
print(procesar_texto(mi_texto, 'eliminar', 'Hola'))


'''
38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario
'''
# Importo datetime para trabajar con horas
import datetime

def momento_del_dia():
    """
    Determina si es de día, tarde o noche según la hora insertada o en su defecto la actual del sistema.
    """
    try:
        # Pido al usuario la hora y convierto el input en un número entero de hora
        hora_usuario = input("Introduce la hora en formato 24h (HH:MM): ")
        hora_actual = int(hora_usuario.split(":")[0])

        # Clasificamos según las franjas horarias
        if 7 <= hora_actual < 16:
            print('Es de día')
        elif 16 <= hora_actual < 21:
            print('Es por la tarde')
        else:
            print('Es de noche')

    except ValueError: # En caso de que no se introduzca bien la hora, aparece este error
        print("Error: Debes introducir la hora en formato correcto (HH:MM).")

# Realizo las comprobaciones en otro archivo .py 

'''
39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente
'''

def determinar_nota (cali_num):
    """ 
    Introduciendo una calificación numérica, establece por rangos la calificación como 'insuficiente', 'bien', 'muy bien' o 'sobresaliente'
    Args:
        cali_num (float): calificación numérica
    Return: 
        calificación (str): puede ser 'insuficiente', 'bien', 'muy bien' o 'sobresaliente'
    """
    # Enlazo condicionales con los rangos de las diferentes calificaciones
    if cali_num <= 69:
        print ('La calificación es: insuficiente')

    elif 70 <= cali_num <= 79:
        print ('La calificación es: bien')

    elif 80 <= cali_num <= 89:
        print ('La calificación es: muy bien')
    
    elif 90 <= cali_num <= 100: 
        print ('La calificación es: sobresaliente')

# Comprobación
determinar_nota (32)
determinar_nota (83)
determinar_nota (96.2)

'''
40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

'''
#Importo math porque al trabajar con operaciones matemáticas (usar el número pi, por ejemplo) resulta útil
import math 

def calcular_area(figura, datos):
    """
    Calcula el área de una figura geométrica.
    
    Args:
        figura (str): puede ser 'rectángulo', 'circulo' o 'triangulo'.
        datos (tuple): valores necesarios para el cálculo:
            - rectángulo: (base, altura)
            - circulo: (radio,)
            - triangulo: (base, altura)
    
    Returns:
        float: área de la figura
    """
    # Al ser diferentes figuras, genero con un condicional un caso con la fórmula para el área de cada una 
    if figura.lower() == 'rectángulo':
        base, altura = datos
        return base * altura
    
    elif figura.lower() == 'circulo':
        (radio,) = datos   # la coma indica que es una tupla de un solo valor
        return math.pi * (radio ** 2)
    
    elif figura.lower() == 'triangulo':
        base, altura = datos
        return (base * altura) / 2
    
    else: # En caso de que se intente calcular otra figura, lanzo un error
        raise ValueError('Figura no reconocida. Debes introucir los datos para: "rectángulo", "circulo" o "triangulo".')

# Comprobación
print(calcular_area('rectángulo', (13, 2)))   
print(calcular_area('circulo', (8,)))        
print(calcular_area('triangulo', (9, 1)))   

'''
41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente:
    1. Solicita al usuario que ingrese el precio original de un artículo.
    2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
    3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
    4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido
    (es decir, mayor a cero). Por ejemplo, descuento de 15€.
    5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
    6. Recuerda utilizar estructuras de control de flujo como if, elif y else
    para llevar a cabo estas acciones en tu programa de Python.
''' 
def calcular_precio_final():
    try:
        # Prenunto el precio original
        precio_original = float(input('Introduce el precio original del artículo (€): '))

        # Pregunto por el cupón
        tiene_cupon = input('¿Tienes un cupón de descuento? (si/no): ').strip().lower()

        # Si tiene cupón, pido su valor
        if tiene_cupon in ('sí', 'si'):
            valor_cupon = float(input('Introduce el valor del cupón (__€): '))
            
            # Verifico que el cupón sea válido
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon
                if precio_final < 0:  # Evitamos precios negativos
                    precio_final = 0
                print(f'Has aplicado un descuento de {valor_cupon}€. El precio final es: {precio_final:}€')
            else:
                print('El valor del cupón no es válido. No se aplicará descuento.')
                print(f'El precio final es: {precio_original}€')

        elif tiene_cupon == 'no':
            # No hay cupón
            print(f'El precio final es: {precio_original}€')

        else: 
            # En caso de que se introduzca algo que no sea si o no
            print('Respuesta no válida. Debes responder "sí" o "no".')

    except ValueError:
            # En caso de que se introduzca un valor no válido
        print('Error: Debes introducir números válidos para el precio o el cupón.')

# Realizo las comprobaciones en otro archivo .py 
