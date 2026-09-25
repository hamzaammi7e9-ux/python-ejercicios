### EXERCICI LITRES

def exerciciLitres():
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")
        litres = 0.0
        
        if opcion == "1":
                total = calculFactura(litres)
                print(f"El total de la factura es: {total:.2f} €")
        elif opcion == "2":
            try:
                litres = float(input("Ingrese el número de litros: "))
                if litres < 0:
                        print("Error: El número de litros no puede ser negativo.")
                elif litres is None:
                        print("Error: No has introducido ningún valor.")
                else:
                        print(f"Litros introducidos: {litres}")
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        elif opcion == "3":
            print("Saliendo del programa.")
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
 
def mostrarMenu():
    print("\n=== Menú Càlcul de Factura ===")
    print("1. Calcular factura")
    print("2. Introducir litros")
    print("3. Salir")
    
def calculFactura(litres):
    quota_fixa = 6
    quota_variable = 0 
    
    if litres in range(50, 200):
        quota_variable = 0.1
    else:    
        quota_variable = 0.3   
    
    total = quota_fixa + (litres * quota_variable)
    
    return total

exerciciLitres()
    
    
    
 ### EXERCICI LITRES
   
    
    
