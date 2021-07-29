# Arreglos para saber si la instruccion entrante es binaria o unaria.
op_booleanas = ['AND', 'OR']
op_iguales = ['EQ', 'NEQ']
op_enteros = ['ADD', 'SUB', 'MUL', 'DIV', 'LT', 'LE', 'GT', 'GE']
op_unarias = ['UMINUS', 'NOT']

def op_igual(instruccion, pila):

    comando = instruccion[0]

    # Si es binaria necesito, por lo menos, dos elementos de la pila
    if pila.tam() < 2:
        print("ERROR: Se necesitan dos elementos. Falta de elementos en la pila")
        return
    
    # Los dos últimos valores en la pila deben tener los mismos tipos. Sin desempilar
    pen, ult = pila.top2()

    if not (type(pen) ==  type(ult)):
        print("Los valores a operar deben ser del mismo tipo. Valor 1: " + str(pen) + ". Valor 2: " + str(ult))
        return

    # Ahora sí se desempilan.
    pila.pop()
    pila.pop()

    if comando == "EQ":
        resultado = pen == ult
        pila.pila.append(resultado)
    elif comando == "NEQ":
        resultado = pen != ult
        pila.pila.append(resultado)

# Ejecuta las operaciones unarias
def op_unaria(instruccion, pila):

    comando = instruccion[0]

    # Si es binaria necesito, por lo menos, dos elementos de la pila
    if pila.tam() < 1:
        print("ERROR: Se necesita un elemento de la pila. Falta de elementos en la pila")
        return
    
    # Toma el último valor de la pila. Pero no lo desempila
    ult = pila.top()
    
    if comando == "UMINUS":
        if not (type(ult) == int ):
            print("El valor a operar debe ser entero. Valor: " + str(ult))
            return
        
        # Ahora sí, lo desempila
        pila.pop()

        resultado = ult * (-1)
        pila.pila.append(resultado)
            
    elif comando == "NOT":
        if not (type(ult) == bool ):
            print("El valor a operar debe ser booleano. Valor: " + str(ult))
            return

            # Ahora sí, lo desempila
        pila.pop()

        resultado = not ult
        pila.pila.append(resultado)

# Ejecuta las operaciones binarias con enteros
def op_entero(instruccion, pila):

    comando = instruccion[0]

    # Si es binaria necesito, por lo menos, dos elementos de la pila
    if pila.tam() < 2:
        print("ERROR: Se necesitan dos elementos. Falta de elementos en la pila")
        return
    
    # Los dos últimos valores en la pila deben ser enteros. Sin desempilar
    pen, ult = pila.top2()

    if not (type(pen) == int and type(ult) == int ):
        print("Los valores a operar deben ser enteros. Valor 1: " + str(pen) + ". Valor 2: " + str(ult))
        return

    # Ahora sí se desempilan.
    pila.pop()
    pila.pop()

    # Ejecuta la operacion específica
    if comando == "ADD":
        resultado = ult + pen
        pila.pila.append(resultado)
    if comando == "SUB":
        resultado = ult - pen
        pila.pila.append(resultado)
    if comando == "MUL":
        resultado = ult * pen
        pila.pila.append(resultado)
    if comando == "DIV":
        try:
            resultado = ult // pen
            pila.pila.append(resultado)
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
            pila.pila.append(pen)
            pila.pila.append(ult)
            return
    if comando == "LT":
        resultado = ult < pen
        pila.pila.append(resultado)
    if comando == "GT":
        resultado = ult > pen
        pila.pila.append(resultado)
    if comando == "LE":
        resultado = ult <= pen
        pila.pila.append(resultado)
    if comando == "GE":
        resultado = ult >= pen
        pila.pila.append(resultado)

# Ejecuta las operaciones binarias con booleanos
def op_booleana(instruccion, pila):

    comando = instruccion[0]

    # Si es binaria necesito, por lo menos, dos elementos de la pila
    if pila.tam() < 2:
        print("ERROR: Falta de elementos en la pila. Se necesitan dos elementos")
        return
    
    # Los dos últimos valores en la pila deben ser enteros. Sin desempilar
    pen, ult = pila.top2()

    if not (type(pen) == bool and type(ult) == bool ):
        print("Los valores a operar deben ser booleanos. Valor 1: " + str(pen) + ". Valor 2: " + str(ult))
        return
    
    # Ahora sí se desempilan.
    pila.pop()
    pila.pop()

    # Ejecuta la operacion específica
    if comando == "AND":
        resultado = pen and ult
        pila.pila.append(resultado)
    if comando == "OR":
        resultado = pen or ult
        pila.pila.append(resultado)