import random
cantNumeros = {1:0,2:0,3:0,4:0,5:0,6:0}
tiradas = 0
print("¿Quieres tirar dado?")
while True:
    print("1 para tirar DADO.")
    print("0 para salir y mostrar resultado.")
    dado=input("Seleccione una opcion:  ")
    if dado =="0":
        print("--- Resultados finales ---")
        print(f"  |Total de tiradas = {tiradas}|")
        for cara, numero in cantNumeros.items():
            print(f"El numero {cara} salió -{numero}- veces")
        print("-Gracias por jugar!! Adios-")
        print("/Grupo/ -10-")
        break
    elif dado =="1":
        tiradas +=  1
        tiradaDado = random.randint(1,6)
        cantNumeros[tiradaDado] +=1
        print(f"Ha salido el NUMERO: {tiradaDado}")
    else:
        print("Opcion incorrecta vuelva a elegir!!! ")
        continue