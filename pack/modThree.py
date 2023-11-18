def cToF():
    
    op = int(input("1. Celsius a Fahrenheit | 2. Fahrenheit a Celsuis: "))
    
    if op == 1:
        celsius = float(input("Ingresa los grados Celsuis para convertirlos a Fahrenheit: "))
        celResult = (celsius * 9/5) + 32
        celResult = round(celResult, 2)
        print(f"El resultado es {celResult} grados Fahrenheit")
    
    elif op == 2:
        far = float(input("Ingresa los grados Fahrenheit para convertirlos a Celsius: "))
        farResult = (far - 32) * 5/9
        farResult = round(farResult, 2)
        print(f"El resultado es {farResult} grados Celsius")
    
    else:
        print("Esa opcion no existe")