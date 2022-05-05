# 1. Hacer un programa que solicite el ingreso de un número y que luego emita un
# cartel por pantalla aclarando si el mismo es múltiplo de 5.

numero=int(input('ingrese numero:'))
if numero % 5 == 0:
   print('el numero es multiplo de 5')
else:
   print('el numero no es multiplo')
print('programa finalizado')

# 2. Hacer un programa que solicite el ingreso de dos números y luego calcular:
# a. La resta si el primero es mayor que el segundo.
# b. La suma si son iguales.
# c. El producto si el primero es menor.
# Se deberá emitir un cartel por pantalla con el resultado correspondiente.

numero1=int(input('ingrese el primer numero:'))
numero2=int(input('ingrese el segundo numero:'))
if numero1>numero2:
   resultado=numero1-numero2
elif numero1==numero2:
   resultado=numero1+numero2
elif numero1<numero2:
   resultado=numero1*numero2
else:
   print('invalido')
print(resultado, '\nprograma finalizado')

# 3. Hacer un programa para ingresar dos números. Si el segundo es distinto de
# cero, calcular la división del primero por el segundo y mostrar el resultado por
# pantalla; caso contrario, emitir un cartel aclarando que no se puede dividir por
# cero.

numero1=int(input('ingrese el primer numero:'))
numero2=int(input('ingrese el segundo numero:'))
if numero2!=0:
   print(numero1/numero2)
else:
   print('no se puede dividir por cero', '\nprograma finalizado')

# 4. Un importante negocio de desinfectante líquido realiza descuentos
# dependiendo de la cantidad de litros vendidos según la siguiente escala:
# a. Si vende menos de 100 litros, no hay descuento.
# b. Si vende entre 101 y 300 litros, el descuento es del 10%.
# c. Si vende entre 301 y 500 litros, el descuento es del 15%.
# d. Finalmente, si la venta es de más de 500 litros, el descuento es del 25%.
# Hacer un programa que solicite el ingreso del importe total de la venta y la
# cantidad de litros vendidos y calcule y emita el importe con el descuento
# aplicado.

importeFinal=int(input('ingrese el importe total:'))
litrosVendidos=int(input('ingrese los litros vendidos:'))
if litrosVendidos>500:
   importeFinal=importeFinal*0.75
elif litrosVendidos>300:
   importeFinal=importeFinal*0.85
elif litrosVendidos>100:
   importeFinal=importeFinal*0.90
else:
   importeFinal=importeFinal
print('El importe total es:', '$'+str(importeFinal), '\nprograma finalizado')

# 5. Hacer un programa que solicite el ingreso de las notas del primer parcial y del
# segundo parcial de una alumna de programación. El programa deberá analizar
# las notas y emitir la situación de la alumna según la siguiente escala:
# a. Si tiene 8 o más en ambos parciales, emitir “aprobación directa”.
# b. Si no tiene 8 o más en ambos pero tiene aprobados ambos parciales (se
# aprueba con 6 o más), emitir “rinde examen final”.
# c. Si tiene menos de 6 en alguno de los dos parciales, emitir “debe
# recuperar”.
# El programa debe emitir solo un cartel, el que corresponda.

parcial1=int(input('ingrese el primero:'))
parcial2=int(input('ingrese el segundo:'))
if parcial1<6 or parcial2<6:
   print('debe recuperar')
elif parcial1>=8 and parcial2>=8:
   print('aprobación directa')
elif parcial1>=6 and parcial2>=6:
   print('rinde examen final')
print('programa finalizado')

# 6. Hacer un programa para ingresar por teclado la longitud de los tres lados de un
# triángulo y que luego determine e informe con un cartel aclaratorio a qué tipo
# de triángulo corresponde:
# a. Equilátero: cuando los tres lados sean iguales.
# b. Isósceles: cuando dos de los tres lados sean iguales.
# c. Escaleno: cuando todos los lados sean distintos.

contador=3
listaDeterminadora=[]
while contador>0:
   lado=int(input('ingrese el lado:'))
   listaDeterminadora.append(lado)
   contador=contador-1
if listaDeterminadora[0] == listaDeterminadora[1] == listaDeterminadora[2]:
   print('Equilatero')
elif listaDeterminadora[0] == listaDeterminadora[1] or listaDeterminadora[1] == listaDeterminadora[2]:
   print('Isósceles')
elif listaDeterminadora[0] != listaDeterminadora[1] and listaDeterminadora[1] != listaDeterminadora[2]:
   print('Escaleno')
print('programa finalizado')

# 7. Hacer un programa para ingresar 4 números. Luego analizar e informar por
# pantalla si los mismos se encuentran ordenados de forma decreciente.

contador=4
listaDeterminadora=[]
while contador>0:
   numero=int(input('ingrese el valor:'))
   listaDeterminadora.append(numero)
   contador=contador-1
if listaDeterminadora[0] > listaDeterminadora[1] and listaDeterminadora[1] > listaDeterminadora[2] and listaDeterminadora[2] > listaDeterminadora[3]:
   print('están ordenados decrecientemente')
else:
   print('no están ordenados decrecientemente')
print('programa finalizado.')

# 8. El negocio de desinfectante antes mencionado vende además detergente
# suelto, y los precios se aplican según la siguiente escala:
# a. 25 ARS por litro los primeros 50 litros.
# b. 20 ARS por litro si la venta es de 51 a 200 litros.
# c. 15 ARS por litro si la venta es de 201 a 500 litros.
# d. 10 ARS por litro si la venta es de más de 500 litros.
# Además, si paga en efectivo, tiene un adicional del 10% sobre el importe final.
# Hacer un programa que solicite la cantidad de litros vendidos y el tipo de pago
# (ingresará 1 si paga en efectivo y 0 con cualquier otro medio de pago) y calcule
# y emita por pantalla el monto final a abonar por el cliente.

litrosVendidos=int(input('ingrese la cantidad de litros vendidos:'))
if litrosVendidos>500:
   importeFinal=litrosVendidos*10
elif litrosVendidos>200:
   importeFinal=litrosVendidos*15
elif litrosVendidos>50:
   importeFinal=litrosVendidos*20
else:
   importeFinal=litrosVendidos*25
tipoDePago=int(input('01:efectivo\n02:no efectivo.\ningrese tipo de pago:'))
if tipoDePago==1:
   importeFinal=importeFinal*1.10
elif tipoDePago==2:
   importeFinal=importeFinal
else:
   print('numero invalido')
print('El importe total es:', '$'+str(importeFinal), '\nprograma finalizado')

# 9. Una importante marca de computadoras permite elegir cierta configuración del
# equipo a comprar. Para ello existe la siguiente escala de precios:
#        i5 (1)    i7 (2)   i9 (3)
# 8 RAM (1) USD 800 USD 900 USD 1200
# 16 RAM (2) USD 900 USD 1000 USD 1400
# 32 RAM (3) USD 1000 USD 1400 USD 2000
# Además, el equipo viene con un disco que permite almacenar 500 GB de
# información y que se puede ampliar a 1 TB si así lo desea, lo cual tiene un costo
# adicional de USD 300.
# Hacer un programa que solicite la opción de procesador, la opción de memoria
# RAM, y si extiende el disco o no (ingresa 1 para extender y 0 para no extender)
# y calcule y emita por pantalla el monto de la máquina seleccionada.
# Nota: si no entendés nada de compus, procesadores y eso, mirá:
# https://youtu.be/Bm3X8eHVv-s

diccionario={
        'i5': {'ram1':'$800', 'ram2':'$900', 'ram3':'$1200'},
        'i7': {'ram1':'$900', 'ram2':'$1000', 'ram3':'$1400'},
        'i9': {'ram1':'$1000', 'ram2':'$1400', 'ram3':'$2000'},
    }
print('procesador:"i5", "i7", "i9"')
ingresarTargeta=input('ingrese procesador:')
print(diccionario[ingresarTargeta].items())
ingresarRAM=input('ingrese el numero de RAM:')
guardarSeleccion=diccionario[ingresarTargeta][ingresarRAM]
print(diccionario[ingresarTargeta][ingresarRAM], '\ningrese la opcion 0:no extender, 1:extender. Si extiende el disco a un terabyte o no:')
discoExtension=int(input('extensión:'))
guardarSeleccion=int(guardarSeleccion.replace('$', ''))
if discoExtension==1:
   guardarSeleccion=guardarSeleccion+300
   print('el total es:','$'+str(guardarSeleccion))
elif discoExtension==0:
   print('el total es:', guardarSeleccion)
else:
   print(None)
print('programa finalizado')

# 10. Hacer un programa que solicite cuatro números y emitir un cartel aclaratorio si
# son todos iguales entre sí, caso contrario, no emitir nada.

numeros1=int(input('ingrese el 1 numero:'))
numeros2=int(input('ingrese el 2 numero:'))
numeros3=int(input('ingrese el 3 numero:'))
numeros4=int(input('ingrese el 4 numero:'))
if numeros1 == numeros2 and numeros2 == numeros3 and numeros3 == numeros4:
   print('son todos iguales entre sí')
else:
   print(None)
print('programa finalizado')

# 11. Hacer un programa para ingresar tres números y luego mostrarlos ordenados
# de menor a mayor.

numeros=input('ingresa los numeros:')
numeros=numeros.split(' ')
numeros=list(map(int, numeros))
numeros.sort()
print(numeros)

# 12. Hacer un programa para ingresar tres números y emitir un cartel aclaratorio si
# la suma de los dos primeros es mayor al producto del segundo con el tercero.

contador=3
lit=[]
while contador>0:
   num=int(input('ingrese los numeros'))
   lit.append(num)
   contador=contador-1
parche1=lit[0]+lit[1]
parche2=lit[1]*lit[2]#no puedo creer que haya tenido que recurrir a los parches.. alternativas
if parche1>parche2:
   print('la suma de los dos primeros elementos de la lista es mayor que el producto del segundo elemento de la lista con el tercero.')
else:
   print(None)
print('programa finalizado')

