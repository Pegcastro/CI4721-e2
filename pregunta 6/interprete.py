from operaciones import op_enteros, op_booleanas, op_unarias, op_iguales, op_igual, op_booleana, op_entero, op_unaria
from Pila import Pila
from id import rvalue, lvalue, assign
import sys    

def main():

    # Agarra el último argumento: El nombre del archivo
    try:
        filename = sys.argv[1]

    except:
        print('RECUERDE: El formato debe ser python interprete.py <filename>')
        sys.exit(1)

    # Abre y lee el archivo de texto
    try:
        file = open(filename)
        lines = file.readlines()

    except FileNotFoundError:
        print('ERROR: El archivo ' + filename + ' no se ha encontrado')
        sys.exit(1)

    etiquetas = {}
    ids = {}
    instrucciones = []

    # Creacion de arreglo de instrucciones con sus respectivas entradas
    for linea in range(len(lines)):
        
        instruccion = lines[linea].replace('\n', '').split(' ')
        for index in range(len(instruccion)):
            if instruccion[index] == '':
                del instruccion[index]                   

        if len(instruccion) > 0:
            # Si hay una etiqueta, la guarda en el diccionario y rehace la instruccion
            if instruccion[0].endswith(':'):
                etiquetas[instruccion[0][:-1]] = linea
                instruccion = instruccion[1:]
        else:
            print("WTF?")
            sys.exit(1)
        
        instrucciones.append(instruccion)

    linea = 0
    pila = Pila()

    # Recorrido del arreglo de instrucciones
    while linea < len(instrucciones):
       
        instruccion = instrucciones[linea]
        if len(instruccion) > 0:
            print("Instruccion: " +  str(instruccion))
            arg1 = instruccion[0]

            # Opciones del intérprete
            if arg1 == 'EXIT':
                sys.exit(0)
            if arg1 == 'PUSH':
                pila.push(instruccion)
            if arg1 == 'POP':
                pila.pop()
            if arg1 in op_enteros:
                op_entero(instruccion, pila)
            if arg1 in op_booleanas:
                op_booleana(instruccion, pila)
            if arg1 in op_unarias:
                op_unaria(instruccion, pila)
            if arg1 in op_iguales:
                op_igual(instruccion, pila)
            if arg1 == "RVALUE":
                rvalue(instruccion, ids, pila)
            if arg1 == "LVALUE":
                lvalue(instruccion, pila)
            if arg1 == "ASSIGN":
                assign(pila, ids)
            if arg1 == "GOTO":
                if len(instruccion) != 2:
                    print("ERROR: Instruccion inválida. Instruccion: " + instruccion)
                else:
                    etiqueta = instruccion[1]
                    # Ver si existe esa etiqueta
                    if not etiqueta in etiquetas:
                        print("ERROR: La etiqueta suministrada no existe. Etiqueta: " + etiqueta)
                    else: 
                        linea = etiquetas[etiqueta] - 1
            if arg1 == "GOFALSE":
                if len(instruccion) != 2:
                    print("ERROR: Instruccion inválida. Instruccion: " + instruccion)
                elif pila.tam() < 1:
                    print("ERROR: No hay suficientes elementos en la pila")
                elif not isinstance(pila.top(), bool):
                    print("ERROR: El valor en el tope de la pila no es booleano. Valor del tope: " + str(pila.top()))
                else:
                    if pila.top() == False:
                        etiqueta = instruccion[1]
                        # Ver si existe esa etiqueta
                        if not etiqueta in etiquetas:
                            print("ERROR: La etiqueta suministrada no existe. Etiqueta: " + etiqueta)
                        else:
                            linea = etiquetas[etiqueta] - 1 
            if arg1 == "GOTRUE":
                if len(instruccion) != 2:
                    print("ERROR: Instrucción inválida. Instruccion: " + instruccion)
                elif pila.tam() < 1:
                    print("ERROR: No hay suficientes elementos en la pila")
                elif not isinstance(pila.top(), bool):
                    print("ERROR: El valor en el tope de la pila no es booleano. Valor del tope: " + str(pila.top()))
                else:
                    if pila.top() == True:
                        etiqueta = instruccion[1]
                        # Ver si existe esa etiqueta
                        if not etiqueta in etiquetas:
                            print("ERROR: La etiqueta suministrada no existe. Etiqueta: " + etiqueta)
                        else:
                            linea = etiquetas[etiqueta] - 1
            if arg1 == "READ":
                if len(instruccion) != 2:
                    print("ERROR: Instruccion inválida: " + instruccion)
                else:
                    id = instruccion[1]
                    valor = input("Introduzca el valor del ID: " + id)
                    cast_valor = pila.cast_val(valor)
                    if (cast_valor == None):
                        print("ERROR: El valor debe ser entero o booleano. Valor: " + valor)
                    else: 
                        ids[id] = cast_valor
            if arg1 == "PRINT":
                if len(instruccion) != 2:
                    print("ERROR: Instruccion inválida: " + instruccion)
                else: 
                    id = instruccion[1]

                    if not id in ids or ids[id] == None:
                        print("El ID otorgado no ha sido asignado o no tiene valor asigando. ID: " + id)
                    else:
                        print("Identificador: " + str(ids[id]))
            if arg1 == "RESET":
                pila.pila = []
                ids = {}
                etiquetas = {}

            print(pila.pila)

            linea += 1
        else:
            print("Fin")
            sys.exit(1)


if __name__ == '__main__':
    main()