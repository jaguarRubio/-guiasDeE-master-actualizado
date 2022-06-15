# 1. Hacer un programa que solicite 50 números enteros y los guarde en un vector.
# Luego recorrer el vector y determinar e informar cuál es la suma de los valores
# del mismo.
# Nota: usar dos ciclos: uno para guardar los números en el vector y otro para
# recorrerlo y leerlo.

import numpy as np

vec=[]
acumulador=0
for elemento in range(5):#50
    ingresar=int(input('ingrese valor:'))
    vec.append(ingresar)
vector=np.array(vec)
for x in range(5):#50
    acumulador+=vector[x]
print('la acumulación total de elementos:', acumulador)
#print(acumulador, vector,':vector', vec,':lista')#ignorar

# 2. Hacer un programa que solicite 50 números enteros y los guarde en un vector.
# Luego recorrer todos los elementos del vector y determinar cuál es el valor
# máximo y su posición dentro del vector.

vec2=[]
maximo2=0
for elemento in range(5):#50
    ingresar=int(input('ingrese valor:'))
    vec2.append(ingresar)
for x in range(5):#50
    vector2=np.append(vec2,vec2[x])
    if vector2[x]>maximo2:
        maximo2=vector2[x]
        posicion=x+1
print('el maximo elemento:', maximo2,'en la posición:', posicion)

# 3. Hacer un programa que solicite 100 números enteros y los guarde en un
# vector. Luego recorrer ese vector para calcular el promedio. Mostrar por
# pantalla los valores del vector que son mayores al promedio calculado.

vec3=[]
acumulador2=0
for elemento in range(10):#100
    ingresar=int(input('ingrese valor:'))
    vec3.append(ingresar)
for x in range(10):#100
    vector3=np.append(vec3,vec3[x])
    acumulador2+=vector3[x]
promedio=acumulador2/10#100
print('promedio:',promedio,'valores mayores al promedio:', vector[vector>promedio])#filtro

# 4. Dada una lista de 10 números enteros, cargarlos en un vector. Luego,
# determinar e informar si el vector está ordenado en forma creciente. Por
# ejemplo el vector con los valores 1, 3, 5, 7 y 9 está ordenado; el vector 1, 5, 3, 7
# y 9 no lo está.

vec4=[]
for elemento in range(5):#10
    ingresar=int(input('ingrese valor:'))
    vec4.append(ingresar)
vector4=np.array(vec4)
maximo4=vector4[0]
banderaPirata=True
for x in range(5):
    if vector4[x]>=maximo4:
        maximo4=vector4[x]
    else:
        banderaPirata=False
if banderaPirata:
    print('sí está ordenado')
else:
    print('no está ordenado')

# 5. Hacer un programa que solicite una serie de valores de tipo char (caracteres).
# Se entiende por carácter a cada elemento que se obtiene de presionar una
# tecla. Por ejemplo el valor “25” tiene dos caracteres (si quisiéramos guardarlo
# en variables enteras nos alcanza con una, pero si queremos guardarlo en
# variables char, necesitaremos dos); la frase “maxi programa” tiene 13 (se
# incluye el espacio como un carácter).
# La cantidad de valores será como máximo 50, pero el programa puede cortar
# antes si se ingresa el carácter “.” (punto). Una vez cargado el vector de char,
# recorrerlo y reemplazar todas las apariciones de la letra “a” por la letra “e”,
# por ejemplo:
# Vector char original: “Hola muchachada cómo están”.
# Vector char modificado: “Hole muchechede cómo esten”
# Finalmente, mostrar el resultado en pantalla.
# Nota: necesitaremos un vector char de 50, pero no lo cargaremos con un For.

klista=[]
contador=0
while contador<50:#50
    ingresado=input('')[0]
    if ingresado=='.':
        break
    klista.append(ingresado)
    contador+=1
for x in range(len(klista)):
    if klista[x]=='a' or klista[x]=='A':
        klista[x]='e'
vector5=np.array(klista)
print(vector5)

# 6. Dada una lista de 10 números, cargarlos en un vector. Luego detectar si en el
# vector hay algún elemento repetido. De haberlo, indicarlo con un cartel
# aclaratorio “Hay repetidos”, de lo contrario indicar “No hay repetidos”.
# Pista: usar ciclos combinados.

mlista=[]
for z in range(10):
    ingresad0=int(input('ingrese numero:'))
    mlista.append(ingresad0)
banderaBlanca=False

vector6=np.array(mlista)
for g in range(10):
    contador=0
    r=vector6[g]
    for h in range(10):
        if vector6[h]==r:
            contador+=1
    if contador>=2:
        banderaBlanca=True
if banderaBlanca:
    print('hay repetidos')
else:
    print('no hay repetidos')

# 7. Una empresa comercializa 15 tipos de artículos y por cada venta realizada
# genera un registro con los siguientes datos:
# • Número de artículo (1 a 15).
# • Cantidad vendida.
# Puede haber varios registros para el mismo artículo y el último se indica
# número de artículo igual a cero.
# Se pide determinar e informar:
# a. El número de artículo que más se vendió en total.
# b. Los números de artículos que no registraron ventas.
# c. La cantidad de unidades vendidas para el artículo número 10.
# Nota: tener en cuenta el concepto de “registro” y el planteo de estructura
# principal separado de consignas (ver videos de ciclos combinados y ejercicios
# resueltos de ciclos combinados).

vector7=np.zeros(15)
maximo=0
banderaGuante=False
jlista=[]
numeroDeArticulo=int(input('ingrese numero de articulo(1-15),(0 concluir):'))
cantidadVendida=int(input('ingrese cantidad vendida:'))
while numeroDeArticulo!=0:
    vector7[numeroDeArticulo-1]+=cantidadVendida
    numeroDeArticulo=int(input('ingrese numero de articulo(1-15),(0 concluir):'))
    if numeroDeArticulo==0:
        break
    cantidadVendida=int(input('ingrese cantidad vendida:'))
for g in range(15):
    if vector7[g]>maximo:
        numero=g+1
        maximo=vector7[g]
    if vector7[g]==0:
        banderaGuante=True
        jlista.append(g+1)
    
print(vector7,'\nel nº de articulo más vendido:',numero,'con:',maximo,'ventas')
if banderaGuante:
    print('el nº de articulo sin venta alguna:', jlista)
else:
    print('no hay nº de articulos sin ventas.')
print('la cantidad de unidades vendidas del articulo nº 10 son:',vector7[10-1])
    
# 8. Se ingresa una lista de 20 números en un vector. Se pide ordenar dichos
# números en forma decreciente (de mayor a menor). Mostrar el listado
# ordenado informando también la posición original de cada número en el
# vector.
# Pista: usar ciclos combinados.

# #valido
# hlista=[]
# for p in range(9):
#     ingresado=int(input('ingrese número:'))
#     hlista.append(ingresado)
# vector8=np.array(hlista)
# ordenado=(-np.sort(-vector8))
# print(vector8,'\n', ordenado)
# #hace uso de vectores puros.

hlista=[]
for ch in range(20):
    ingresado=int(input('ingrese número:'))
    hlista.append(ingresado)
posicionHlista=[]
for la in range(20):
    posicionHlista.append(la+1)
# for che in range(6):######ignorar
#     print(hlista[che],' - ',posicionHlista[che])######ignorar
for uq in range(20):
    for wa in range(20-1):
        if hlista[wa]<hlista[wa+1]:
            auxiliar=hlista[wa+1]
            hlista[wa+1]=hlista[wa]
            hlista[wa]=auxiliar
            auxiliar=posicionHlista[wa+1]
            posicionHlista[wa+1]=posicionHlista[wa]
            posicionHlista[wa]=auxiliar

# vector8=np.array(hlista)
# ordenado=(-np.sort(-vector8))
for che in range(20):
    print(hlista[che],' - ',posicionHlista[che])
#aplica listas que no son vectores per se (en el mod. numpy se usa en casos especiales de operaciones)
#ignorar mis notas en el margen del CLI.