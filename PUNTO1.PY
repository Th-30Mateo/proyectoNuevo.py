def suma(a, b):
    return a+b
def resta(a, b):
    return a - b
def multi(a, b):
    return a * b
def divi(a, b):
    if a or b !=0:
        return a / b

while True:
    print("1 para Sumar")
    print("2 para Restar")
    print("3 para Multiplicar")
    print("4 para Dividir")
    print("0 para -SALIR-")
    opcion = input("Ingrese una opcion:  ")
    if opcion =="0" :
        print("Gracias por usar nuestro programa. Adios :D")
        break
    elif opcion == "1":
        a = int(input("Ingrese el primer numero:  "))
        b = int(input("Ingrese el segundo numero:  "))
        print("El resultado es = ",suma(a, b))
    elif opcion == "2":
        a = int(input("Ingrese el primer numero:  "))
        b = int(input("Ingrese el segundo numero:  "))
        print("El resultado es = ", resta(a, b))
    elif opcion =="3":
        a = int(input("Ingrese el primer numero:  "))
        b = int(input("Ingrese el segundo numero:  "))
        print("El resultado es = ", multi(a,b))
    elif opcion =="4":
        while True:
            a = int(input("Ingrese el primer numero:  "))
            b = int(input("Ingrese el segundo numero:  "))
            if b == 0:
                print("No se puede dividir por 0, ingrese otro numero")
            else:
                print("El resultado es = ", divi(a,b))
                break
    else:
        print("Opcion incorrecta ingrese un numero entre 1 y 4 o -0- para SALIR")