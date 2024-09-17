def convertir_moneda(monto, tipo_cambio, de_pesos_a_dolares=True):
    if de_pesos_a_dolares:
        return monto / tipo_cambio
    else:
        return monto * tipo_cambio

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def puede_conducir(edad, tiene_licencia):
    if edad >= 18 and tiene_licencia:
        return "Puedes conducir."
    elif edad >= 18 and not tiene_licencia:
        return "No puedes conducir porque no tienes licencia."
    else:
        return "No puedes conducir porque eres menor de edad."

def menu():
    print("Menú de opciones:")
    print("1. Conversión de moneda (Pesos ↔ Dólares)")
    print("2. Calcular el área de un triángulo")
    print("3. Determinar si un número es par o impar")
    print("4. Determinar si puedes conducir")
    print("5. Salir")

while True:
    menu()
    opcion = int(input("\nElige una opción (1-5): "))

    if opcion == 1:
        monto = float(input("Ingresa el monto: "))
        tipo_cambio = float(input("Ingresa el tipo de cambio (pesos a dólares): "))
        de_pesos_a_dolares = input("¿Deseas convertir de pesos a dólares? (s/n): ").lower() == 's'
        resultado = convertir_moneda(monto, tipo_cambio, de_pesos_a_dolares)
        if de_pesos_a_dolares:
            print(f"{monto} pesos son {resultado:.2f} dólares.")
        else:
            print(f"{monto} dólares son {resultado:.2f} pesos.")
    
    elif opcion == 2:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es {area:.2f}.")
    
    elif opcion == 3:
        numero = int(input("Ingresa un número: "))
        resultado = es_par_o_impar(numero)
        print(f"El número {numero} es {resultado}.")
    
    elif opcion == 4:
        edad = int(input("Ingresa tu edad: "))
        tiene_licencia = input("¿Tienes licencia? (s/n): ").lower() == 's'
        resultado = puede_conducir(edad, tiene_licencia)
        print(resultado)
    
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    
