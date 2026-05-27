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
        if disponibles == 0:
            print("Lo sentimos, no quedan sitios disponibles")
    elif opcion == 2:
        print(f"\n--- Registrar entrada de vehiculo ")
    else:
        print("Opción invalida")