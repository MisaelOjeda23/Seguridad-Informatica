def kAndM():
    
    op = int(input("1. De Kilometros a Millas | 2. De Millas a Kilometros"))
    
    if op == 1:
        
        km = float(input("Ingresa la distancia en kilómetros: "))
        miles = km * 0.621371
    
        print(f"{km} kilómetros son aproximadamente {miles} millas")
        
    elif op == 2:
        
        miles = float(input("Ingresa la distancia en millas: "))
        km = miles / 0.621371
        
        print(f"{miles} millas son aproximadamente {km} kilómetros")
    
    else:
        print("ESA OPCION NO EXISTE")
    