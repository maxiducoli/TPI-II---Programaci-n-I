
# Importamos las librerias  
from funciones.primo_no_primo import es_primo as primo, es_primo_malo as primo_malo, ejecucion_funcion as analisis
# Creamos una lista con numeros primos
primos=[10009,10037,10039,10093,10099,1043,21,1323,213,332,1323,123,4,2,56,8765,798]
# Menu
def menu():
    print("\n-- TPI I - PROGRAMACION 1 --\n")
    print("\n-- MENU PRINCIPAL --")
    print("PRESIONE 1 PARA CALCULAR EL TIEMPO DE LAS OPERACIONES: ")
    print("PRESIONE 2 PARA SALIR DE LA OPERACION: ")
# Main
def main():
    opciones ="" # <--Creamos una variable vacia, para almacenar la opción seleccionada 
    # Bucle
    while True:
        menu() 
        opciones = input("ELIGE UNA OPCION: ") 
        if opciones == "1":
            analisis(primo,primo_malo,primos) # <--Llamada a la funcion análisis
        elif opciones == "2": 
            print("Hasta luego!") # <--Mensaje de salida
            break # <--Quiebre del bucle
        else:
            print("Ingrese un valor entre 1 y 2 ")
        

if __name__=="__main__": # <--Bloque Principal
    main()


