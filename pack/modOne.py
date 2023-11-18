def tables():
    rangeInit = int(input("Ingresa en que tabla iniciarás: "))
    rangeEnd = int(input("Ingresa en que tabla acabarás: "))

    tableInit = int(input("Ingresa de que número empezará la tabla: "))
    tableFinal = int(input("Ingresa hasta que número acabará: "))

    for i in range(rangeInit, rangeEnd+1):
        for j in range(tableInit, tableFinal+1):
            result = i * j
            print(f" {i} X {j} = {result}")