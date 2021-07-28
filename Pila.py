import sys

class Pila:

    def __init__(self) -> None:

        self.pila = []

    # Castea el tipo del valor ingresado
    def cast_val(self, val):

        if val == 'true':
            val = True
        elif val == 'false':
            val = False
        else:
            try:
                val = int(val)
            except:
                return None

        return val

    # Empila el valor pasado en la instruccion, si existe.
    def push(self, instruccion):

        # Si es PUSH debe tener solo tamaño 2: PUSH <val>
        if not len(instruccion) == 2:
            print("No es válida la instrucción: " + str(instruccion))
            sys.exit(1)

        val = instruccion[1]
        cast_val = self.cast_val(val)

        if cast_val == None:
            print('ERROR: El valor debe ser entero o booleano. Valor: ' + val)
            sys.exit(1)

        self.pila.append(cast_val)

    # Desempila y descarta lo que esté en el tope de la pila
    def pop(self):

        self.pila.pop()

    # Toma el último elemento de la pila, pero no lo desempila
    def top(self):

        return self.pila[-1]

    # Toma los dos últimos elementos de la pila, pero no los desempila
    def top2(self):

        return self.pila[-2:]

    # Devuelve el tamaño de la pila
    def tam(self):

        return len(self.pila)
    
    # Imprime la pila
    def print_pila(self):

        print(self.pila)
    