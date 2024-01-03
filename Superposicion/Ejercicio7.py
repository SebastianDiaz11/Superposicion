"""
7. Definir una funcion superposicion() que tome dos listas y devuelva TRUE si tienen al menos 1 miembro en comun 
o devuelva FALSE de lo contrario.
Escribir la funcion usando el bucle for anidado.
"""

def superposicion(lista1,lista2):

#Manera con el bucle for anidado
    for elem in lista1:
        for elem2 in lista2:
            if elem == elem2:
                return True
    return False

print(superposicion([1,2,3],[3,4,5]))
print(superposicion([1,2,3],[4,5,6]))



#Manera simplificada sin el bucle for anidado

"""   
    for elem in lista1:
        if elem in lista2:
            return True
        
    return False

print(superposicion([1,2,3],[3,4,5]))
print(superposicion([1,2,3],[4,5,6]))
"""