from servicios import GestorEstudiantes


def mostrar_menu():
    print("\n=== GESTION DE ESTUDIANTES ===")
    print("1. Crear estudiante")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("0. Salir")


def leer_texto(mensaje):
    return input(mensaje).strip()


def main():
    gestor = GestorEstudiantes("data/estudiantes.json")

    while True:
        mostrar_menu()
        opcion = leer_texto("Seleccione una opción: ")

        if opcion == "1":
            nombre = leer_texto("Nombre: ")
            carnet = leer_texto("Carnet: ")
            email = leer_texto("Email: ")
            ok, mensaje = gestor.crear(nombre, carnet, email)
            print(mensaje)

        elif opcion == "2":
            estudiantes = gestor.listar()
            if not estudiantes:
                print("No hay estudiantes.")
            else:
                for e in estudiantes:
                    print(e)

        elif opcion == "3":
            texto = leer_texto("Buscar: ")
            resultado = gestor.buscar(texto)
            if not resultado:
                print("No se encontraron resultados.")
            else:
                for e in resultado:
                    print(e)

        elif opcion == "4":
            id_estudiante = int(leer_texto("Id: "))
            nombre = leer_texto("Nuevo nombre (dejar vacío para no cambiar): ") or None
            carnet = leer_texto("Nuevo carnet (dejar vacío para no cambiar): ") or None
            email = leer_texto("Nuevo email (dejar vacío para no cambiar): ") or None
            ok, mensaje = gestor.actualizar(id_estudiante, nombre, carnet, email)
            print(mensaje)

        elif opcion == "5":
            id_estudiante = int(leer_texto("Id: "))
            ok, mensaje = gestor.eliminar(id_estudiante)
            print(mensaje)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
