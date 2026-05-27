print("Gestión de Eco-Camping 'Bosque Vivo")
capacidad_maxima = 15
sitios_ocupados = 0
ejecutando = True
while ejecutando:
    print("n\=== MENÚ DE CONTROL DE REGISTROS ===")
    print("1.- Ver sitios disponibles")
    print("2.- Registro de entrada de vehiculos")
    print("3.- Registro de salida de vehiculos")
    print("4.- Estado actual del camping")
    print("5.- Salir")
    try:
        opcion = int(input("Seleccione una opción (1-5): "))
    except ValueError:
        print("Opción no válida")
        continue
    if opcion == 1:
        disponibles = capacidad_maxima - sitios_ocupados
        print(f"\n[INFO] Sitios libres actualmente: {disponibles}")
    elif opcion == 2:
        sitios_libres = capacidad_maxima - sitios_ocupados
        if disponibles == 0:
            print("Lo sentimos, no quedan sitios disponibles")
        else:
            try:
                ingreso = int(input("¿Cuántos sitios reservará?"))
                if ingreso <= 0:
                    print("Error, la cantidad a registrar debe ser mayor a 0")
                elif ingreso > sitios_libres:
                    print(f"Solo hay disponibles {sitios_libres} sitios")  
                else:
                    sitios_ocupados += ingreso
                    print(f"Ingreso registrado, se han reservado {ingreso} sitios")
            except ValueError:
                print("Error, valor no válido")
    else:
        print("Opción invalida")