# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
temp_1=float(input('Ingrese la primera temperatura:\n'))
temp_2=float(input('Ingrese la segunda temperatura:\n'))
temp_3=float(input('Ingrese la tercera temperatura:\n'))


if (temp_1 > temp_2) and (temp_1 > temp_3):
    print ('La primera temperatura ingresada, {}, es la maxima temperatura'.format(temp_1))
elif (temp_2 > temp_1) and (temp_2 > temp_3):
    print ('La segunda temperatura ingresada, {}, es la maxima temperatura'.format(temp_2))
elif (temp_3 > temp_1) and (temp_3 > temp_2):
    print ('La tercera temperatura ingresada, {}, es la maxima temperatura'.format(temp_3))
else:
    print ('Las tres temperaturas son iguales')


if (temp_1 < temp_2) and (temp_1 < temp_3):
    print ('La primera temperatura ingresada, {}, es la minima temperatura'.format(temp_1))
elif (temp_2 < temp_1) and (temp_2 < temp_3):
    print ('La segunda temperatura ingresada, {}, es la minima temperatura'.format(temp_2))
elif (temp_3 < temp_1) and (temp_3 < temp_2):
    print ('La tercera temperatura ingresada, {}, es la minima temperatura'.format(temp_3))
else:
    print ('Las tres temperaturas son iguales')

promedio = (temp_1 + temp_2 + temp_3) / 3

print ('El promedio de las temperaturas ingresadas es {}'.format(promedio))
