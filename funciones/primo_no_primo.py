import time

# Creacion de algoritmo eficiente
def es_primo(x):
    # Si x es menor a 2 retorna false
    if x < 1:
        return False
    # creacion de variable raiz cuadrada, que calcula la raiz cuadrada de x, sin necesidad de importar la libreria math.
    raiz_cuadrada=(x**0.5) +1
    # Creacion del ciclo for que recorrera desde el 2 hasta x(excluyente) porque si incluyo al 11 en el bucle me va a dar x % i == 0 y entraria en el if dando como resultado TRUE y seria un error
    for i in range (2,int(raiz_cuadrada)): #Se  pone int porque si da un numero flotante el ciclo for no lo acepta   
        
        # Si entre a este if significa que el numero no es primo, porque me estaria dando de resto 0
        if x % i == 0:
            return False
    #Si no  tiene ningun numero mod == 0 entonces significa que el numero es primo 
    return True

def es_primo_malo(x):
        # Verificación de números negativos o menores a 1
    if x < 1:
        resultado = False
    else:
        resultado = True
    # vericacion de todos los numeros ( mas largo  que el anterior ejemplo)
    if resultado:
        for i in range(2, x):  # O(n) <-- ahora recorre todo el camino hasta x
            if x % i == 0:
                resultado = False
                
    return resultado

    # print(es_primo_malo(12))

    # === Función para medir tiempo de ejecución varias veces ===
    # === Sin la repetición las funciones me devolvían tanto el tiempo de inicio, como el final 0.0000000
    # === Agregué repeticiones al código para luego devidir el tiempo total en las repeticiones y scar el promedio
    # === No se si está bien hacer eso, pero de otra manera no podía obtener valores que no sean 0.000000
    # === Función para medir tiempo de ejecución varias veces ===
def medir_tiempo(funcion, dato, repeticiones=100):
    inicio = time.time() #<--Guarda el tiempo de inicio
    for _ in range(repeticiones):
        resultado = funcion(dato)
    fin = time.time() #<--Guarda el tiempo de fin
    tiempo_total = fin - inicio #<--calcula el tiempo tardado real (tiempo final menos tiempo final)
    tiempo_promedio = tiempo_total / repeticiones #<--Aca se hace un promedio del tiempo total, con la cantidad de repeticiones
    return resultado, tiempo_promedio #<--Retorna el valor ( Si es primo o no primo con True or False) y El tiempo promedio

def ejecucion_funcion(es_primo,es_primo_malo,datos):
    # === Configuración del ancho de columnas ===
    ancho_dato = 10
    ancho_resultado = 30
    ancho_tiempo = 30
    ancho_mejor = 50

    # === Imprimimos encabezado ===
    print(
        "Dato".ljust(ancho_dato) + "|" +
        "Resultado F1".ljust(ancho_resultado) + "|" +
        "Tiempo F1 (s)".ljust(ancho_tiempo) + "|" +
        "Resultado F2".ljust(ancho_resultado) + "|" +
        "Tiempo F2 (s)".ljust(ancho_tiempo) + "|" +
        "Mejor función".ljust(ancho_mejor)
    )
    print("-" * (ancho_dato + ancho_resultado * 2 + ancho_tiempo * 2 + ancho_mejor + 4))

    # === Ejecutar comparación ===
    for dato in datos: #<--Creacion del ciclo for, que se va a encargar de tirar todos los datos por consola
        primo, tiempo1 = medir_tiempo(es_primo, dato)#<-- Esto guardas el tiempo y 
        primo_malo, tiempo2 = medir_tiempo(es_primo_malo, dato)

        # Determinamos cuál función fue más rápida
        if tiempo1 < tiempo2: 
            mejor = "Función 1"
        elif tiempo2 < tiempo1:
            mejor = "Función 2"
        else:
            mejor = "Iguales"

        # Imprimimos resultados formateados
        print(
            str(dato).ljust(ancho_dato) + "|" + #<--Con (.ljust) lo que hacemos es justificar el texto a la izquierda, y agrega espacios en blanco segun el valor que  especifiquemos.  
            str(primo).ljust(ancho_resultado) + "|" +
            f"{tiempo1:.10f}".ljust(ancho_tiempo) + "|" + #{tiempo1:.10f} Lo que hace es agregar 10 decimales (lo que permite esta funcion es dar mas precision en el tiempo)
            str(primo_malo).ljust(ancho_resultado) + "|" +
            f"{tiempo2:.10f}".ljust(ancho_tiempo) + "|" +
            mejor.ljust(ancho_mejor) #<--Funcion mas rapida
        )

