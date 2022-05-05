# 1. Hacer un programa para ingresar un número y luego se emita por pantalla un
# cartel aclaratorio si “Es mayor a 10” o “No es mayor a 10”.

numero=int(input('ingresa el numero:'))
if numero>10:
   print('Es mayor a 10')
else:
   print('No es mayor a 10')
print('\nprograma finalizado')

# 2. Hacer un programa para ingresar dos números distintos y luego se muestre por
# pantalla el menor de ellos.
# Nota: no te olvides del ambiente ideal. Qué es eso? Mirá:
# https://youtu.be/TTvnrL1KUZM?t=931

numero1=int(input('ingresa el primer numero:'))
numero2=int(input('ingresa el segundo numero:'))
if numero1 == numero2:
   print('debian ser distintos')
elif numero2<numero1:
   print(numero2,'es menor')
elif numero1<numero2:
   print(numero1,'es menor')
else:
   print('invalido')
print('\nprograma finalizado')

# 3. Hacer un programa para ingresar dos números y que luego emita por pantalla
# el mayor de ellos o un cartel aclaratorio “Son iguales” en el caso de que así sea.
# Nota: los números pueden ser iguales.

numero3=int(input('ingresa el primer numero:'))
numero4=int(input('ingresa el segundo numero:'))
if numero3 == numero4:
   print('son iguales')
elif numero3>numero4:
   print(numero3,'es mayor')
elif numero4>numero3:
   print(numero4,'es mayor')
else:
   print('invalido')
print('\nprograma finalizado')

# 4. Hacer un programa para ingresar un número y luego se emita un cartel por
# pantalla “Positivo” si el número es mayor a cero, “Negativo” si el número es
# menor a cero o “Cero” si el número es igual a cero.
# Nota: requiere más de in IF! Repasá cómo se escribirían:
# https://youtu.be/TTvnrL1KUZM?t=1180

numero5=int(input('ingresa el primer numero:'))
if numero5 > 0:
   print('positivo')
elif numero5 < 0:
   print('negativo')
else:
   print('cero')
print('\nprograma finalizado')

# 5. Hacer un programa para ingresar un número y mostrar por pantalla un cartel
# aclaratorio si el mismo es PAR o IMPAR.
# Nota: leé sobre el operador “Resto”. En el próximo video lo explicaremos!

# numero6=int(input('ingrese numero:'))
if numero6 % 2 == 0:
   print('el numero es par')
else:
   print('el numero es impar')
print('\nprograma finalizado')

# 6. Una casa de video juegos otorga un descuento dependiendo del importe de la
# compra realizada según los siguientes valores:
# • Si el importe es menor a ARS 1000, no hay descuento.
# • Si el importe es ARS 1000 o más pero menor a ARS 5000, aplica un
# descuento del 10%.
# • Si el importe es ARS 5000 o más, aplica un descuento del 18%.
# Hacer un programa para ingresar un importe de venta y luego muestre por
# pantalla el importe final con el descuento que corresponda.

importe=float(input('ingrese el importe de compra:'))
if importe>5000:
   importeTotal=importe*0.82
elif importe>1000 and importe<5000:
   importeTotal=importe*0.90
else:
   importeTotal=importe
print('el importe total es:', importeTotal)

# 7. Hacer un programa para ingresar cuatro números distintos y luego mostrar por
# pantalla el mayor de ellos.

numero7=float(input('numero1:'))
numero8=float(input('numero2:'))
numero9=float(input('numero3:'))
numero10=float(input('numero4:'))
if numero7>numero8 and numero7>numero9 and numero7 > 10:
   print('numero1',numero7)
elif numero8>numero9 and numero8>numero10:
   print('numero2',numero8)
elif numero9>numero10:
   print('numero3',numero9)
else:
   print('numero4',numero10)
print('programa finalizado')

# 8. Hacer un programa para ingresar cuatro números distintos y luego mostrar por
# pantalla el menor de ellos.

numero11=float(input('numero1:'))
numero12=float(input('numero2:'))
numero13=float(input('numero3:'))
numero14=float(input('numero4:'))
if numero11<numero12 and numero11<numero13 and numero11<14:
   print('numero1',numero11)
elif numero12<numero13 and numero12<numero14:
   print('numero2',numero12)
elif numero13<numero14:
   print('numero3',numero13)
else:
   print('numero4',numero14)
print('programa finalizado')

# 9. Hacer un programa para ingresar cinco números distintos y luego mostrar por
# pantalla el mayor y el menor de ellos.


numero15=float(input('primer numero:'))
numero16=float(input('segundo numero:'))
numero17=float(input('tercer numero:'))
numero18=float(input('cuarto numero:'))
numero19=float(input('quinto numero:'))
if numero15<numero16:
   minimo=numero15
else:
   minimo=numero16
if numero17<minimo:
   minimo=numero17
if numero18<minimo:
   minimo=numero18
if numero19<minimo:
   minimo=numero19
if numero15>numero16:
   maximo=numero15
else:
   maximo=numero16
if numero17>maximo:
   maximo=numero17
if numero18>maximo:
   maximo=numero18
if numero19>maximo:
   maximo=numero19
print('el minimo es:',minimo,'\ny el maximo es:',maximo,'\nprograma finalizado')

# 10. Hacer un programa para ingresar cuatro números y luego mostrar por pantalla
# cuáles son mayores a 100.
cuatro=4
listaVacia=[]
posicion=1
while cuatro > 0:
   numeros=int(input('ingrese el valor:'))
   if numeros>100:
      listaVacia.append(posicion)
      listaVacia.append(numeros)
   posicion=posicion+1
   cuatro=cuatro-1
print('estos son mayores a 100:',listaVacia)

# 11. Hacer un programa para ingresar cuatro números y luego mostrar por pantalla
# cuántos son menores a 100.

cantidad=0
contador=4
while contador>0:
   numeros=int(input('ingrese el numero:'))
   if numeros>100:
      cantidad=cantidad+1
   contador=contador-1
print('la cantidad son:', cantidad)

# 12. Hacer un programa para ingresar un valor que estará expresado en minutos. Si
# los minutos superan los 60, pasar el valor a horas, de lo contrario dejarlo en
# minutos. Mostrar el resultado en pantalla aclarando si se muestran minutos u
# horas.

valor=int(input('ingrese el valor:'))
horas=0
if valor<60:
   print('minutos presentes:', valor)
else:
   while valor>60:
      horas=horas+1
      valor=valor-60
   print('horas totales:',horas)
print('programa finalizado')

