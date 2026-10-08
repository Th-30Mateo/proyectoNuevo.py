TIPOS_ANIMALES = ("perro", "gato", "ave", "otro")
mascotas = {}
turnos = {}
contador = 1
contador_turnos = 1

def generar_id_mascota():
    global contador
    nuevo_id = str(contador)
    if contador >= 9999:
        contador = 1
    else:
        contador += 1
    return nuevo_id

def alta_mascota():

    nombre = input("Nombre de la mascota: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío")
        return
    tipo = input("Ingrese el tipo de mascota (Perro, Gato, Ave, Otro): ").lower().strip()
    if tipo not in TIPOS_ANIMALES:
        print("Tipo inválido")
        return
    
    edad = input("Edad de la mascota: ").strip()
    if not edad:
        print("La edad no puede estar vacía")
        return
    for mascota in mascotas.values():
        if mascota["nombre"] == nombre and mascota["tipo"] == tipo:
            print("Esta mascota ya está registrada")
            return
    
    id_mascota = generar_id_mascota()
    mascotas[id_mascota] = {"nombre": nombre, "tipo": tipo, "edad": edad}
    print("Registro completo")
    print(f"ID asignado: {id_mascota}")
    print(f"Nombre: {nombre}, Tipo: {tipo}, Edad: {edad}")

def buscar_mascota():
    busqueda = input("Ingrese ID : ").strip()
    encontrado = False
    
    if busqueda in mascotas:
        print(mascotas[busqueda])
        encontrado = True
    else:
        for datos in mascotas.values():
            if datos["nombre"] == busqueda:
                print(datos)
                encontrado = True
                break
    
    if not encontrado:
        print("Mascota no encontrada")

def eliminar_mascota():
    id_mascota = input("Ingrese ID: ").strip()
    if id_mascota in mascotas:
        confirmar = input("Pulse Enter para confirmar la eliminación o cualquier tecla para cancelar: ")
        if confirmar == "":
            del mascotas[id_mascota]
            
            turnos_a_eliminar = [id_turno for id_turno, datos in turnos.items()
                                 if datos["mascota"] == id_mascota]
            for id_turno in turnos_a_eliminar:
                del turnos[id_turno]
            print("Mascota eliminada")
        else:
            print("Eliminación cancelada")
    else:
        print("Mascota no encontrada")

def editar_mascota():
    id_mascota = input("Ingrese ID: ").strip()
    if id_mascota in mascotas:
        while True:
            print("1. Editar nombre")
            print("2. Editar tipo")
            print("3. Editar edad")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                nuevo_nombre = input("Nuevo nombre: ").strip()
                if nuevo_nombre:
                    mascotas[id_mascota]["nombre"] = nuevo_nombre
                    print("Nombre actualizado")
                    print(f"ID: {id_mascota}, Nombre: {nuevo_nombre}, Tipo: {mascotas[id_mascota]['tipo']}, Edad: {mascotas[id_mascota]['edad']}")
                else:
                    print("El nombre no puede estar vacío")
            elif opcion == "2":
                nuevo_tipo = input("Ingrese el nuevo tipo (perro, gato, ave, otro): ").lower().strip()
                if nuevo_tipo in TIPOS_ANIMALES:
                    mascotas[id_mascota]["tipo"] = nuevo_tipo
                    print("Tipo actualizado")
                    print(f"ID: {id_mascota}, Nombre: {mascotas[id_mascota]['nombre']}, Tipo: {nuevo_tipo}, Edad: {mascotas[id_mascota]['edad']}")
                else:
                    print("Tipo inválido")
            elif opcion == "3":
                nueva_edad = input("Nueva edad: ").strip()
                if nueva_edad:
                    mascotas[id_mascota]["edad"] = nueva_edad
                    print("Edad actualizada")
                    print(f"ID: {id_mascota}, Nombre: {mascotas[id_mascota]['nombre']}, Tipo: {mascotas[id_mascota]['tipo']}, Edad: {nueva_edad}")
                else:
                    print("La edad no puede estar vacía")
            elif opcion == "4":
                break
            else:
                print("Opción inválida")
    else:
        print("Mascota no encontrada")

def generar_id_turno():
    global contador_turnos
    nuevo_id = str(contador_turnos)
    if contador_turnos >= 9999:
        contador_turnos = 1
    else:
        contador_turnos += 1
    return nuevo_id

def asignar_turno():
    id_mascota = input("Ingrese ID de la mascota: ").strip()
    if id_mascota in mascotas:
        fecha = input("Fecha (dia/mes/año): ").strip()
        if not fecha:
            print("La fecha no puede estar vacía")
            return
        
        motivo = input("Motivo de consulta: ").strip()
        if not motivo:
            print("El motivo no puede estar vacío")
            return
        
        id_turno = generar_id_turno()
        turnos[id_turno] = {
            "mascota": id_mascota,
            "fecha": fecha,
            "motivo": motivo
        }
        print("Turno asignado")
        print(f"ID de turno: {id_turno}")
    else:
        print("Mascota no encontrada")

def mostrar_turnos():
    print("\n--- TURNOS ---")
    if turnos:
        for id_turno, detalles in turnos.items():
            print(f"ID Turno: {id_turno}, ID Mascota: {detalles['mascota']}, "
                  f"Fecha: {detalles['fecha']}, Motivo: {detalles['motivo']}")
    else:
        print("No hay turnos asignados")
def menu():
    while True:
        print("\nSistema de Gestión de Veterinaria")
        print("1. Alta de Mascota ")
        print("2. Buscar Mascota ")
        print("3. Eliminar Mascota ")
        print("4. Editar Mascota ")
        print("5. Asignar Turno ")
        print("6. Mostrar Turnos ")
        print("7. Salir ")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            alta_mascota()
        elif opcion == "2":
            buscar_mascota()
        elif opcion == "3":
            eliminar_mascota()
        elif opcion == "4":
            editar_mascota()
        elif opcion == "5":
            asignar_turno()
        elif opcion == "6":
            mostrar_turnos()
        elif opcion == "7":
            print("Saliendo ...")
            print("/Grupo/ -10-")
            break
        else:
            print("Reintente nuevamente")
if __name__ == "__main__":
    menu()