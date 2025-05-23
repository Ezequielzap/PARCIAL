#

                    #PARAMETROS FORMALES
def cacular_promedio(lista:list,valor:int)->bool:

    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    promedio = suma / len(lista)

    if promedio > valor:
        respuesta = True
    else:
        respuesta = False
    return respuesta

entrada = [10,20,30,40]
valor = 24

#invoco a la funcion      #PARAMETROS ACTUALES
llamada = cacular_promedio(entrada,valor)

if llamada:
    print("el promedio es mayor que el valor")
else:
    print("el promedio no es mayor que el valor")