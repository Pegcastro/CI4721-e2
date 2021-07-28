# Empila el contenido del identificador otorgado
def rvalue(instruccion, ids, pila):

    if (len(instruccion) < 2):
        print("Instruccion inválida. Falta de ID: " + instruccion)

    # Agarro el id de la instruccion
    id = instruccion[1]

    if not id in ids:
        print("El ID otorgado para rvalue no tiene valor previamente asignado")
        return

    pila.pila.append(ids[id])

# Empila la dirección del identificador otorgado
def lvalue(instruccion, pila):

    if (len(instruccion) < 2):
        print("Instruccion inválida. Falta de ID. Instruccion: " + instruccion)
        return
    elif (len(instruccion) > 2):
        print("Instrución inválida. Solo es necesario el nombre del ID. Instruccion: " + instruccion)
        return

    id = instruccion[1]

    # Nota: Necesito algo que me pueda diferenciar la "direccion" del "contenido". Así que usará una dupla.
    pila.pila.append((id,"lvalue"))

def assign(pila, ids):

    if(pila.tam()) < 2:
        print("No hay suficientes elementos para la asignacion en la pila: " + pila.pila)
        return
    
    # Verificacion de tipos para los dos ultimos valores de la pila
    rvalue, lvalue = pila.top2()

    if not isinstance(lvalue, tuple):
        print("No se ha asignado un lvalue en el tope de la pila. Valor tomado: " + str(lvalue))
        return
    
    # Ahora si se desempila
    pila.pop()
    pila.pop()

    # Se asigna el nuevo valor
    ids[lvalue[0]] = rvalue
