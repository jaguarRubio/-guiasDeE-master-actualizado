# 1. Hacer un programa que solicite el ingreso de 10 números y que muestre el
# mayor de ellos por pantalla. Solo se debe emitir UN valor por pantalla.

maximo=0
for x in range(10):
   numero=int(input('ingrese el numero:'))
   if numero>maximo:
      maximo=numero
   else:
      None
print('el máximo es:',maximo) #optimización: usar el primer valor como prioridad.
print('programa finalizado')

# 2. Hacer un programa que solicite 20 números y calcule y emita por pantalla
# cuántos son positivos (mayores a cero). Se debe mostrar un solo valor: el
# conteo final.

contador=0
for x in range(20):
   numeros=int(input('ingrese el numero:'))
   if numeros > 0:
      contador=contador+1
   else:
      print(None)
print('conteo final:', contador)
print('programa finalizado')

# 3. Hacer un programa para mostrar los números del 1 al 10. No se debe realizar
# ningún pedido de datos.

for x in range(10):
   print(x+1)
print('programa finalizado')

# 4. Hacer un programa para mostrar los números del 10 al 1. No se debe realizar
# ningún pedido de datos.

for x in range(10, -1, -1):
   print(x)
print('programa finalizado')

# 5. Hacer un programa que muestre los números del 1 al 100 de 5 en 5. Ejemplo:
# 0, 5, 10, 15, 20.... 100.

for x in range(0, 101, 5):
   print(x)
print('programa finalizado')

# 6. Hacer un programa que solicite UN número y luego calcule y emita un cartel
# aclaratorio si el mismo es primo o no es primo.
# Nota: un numero es primo cuando es divisible únicamente por 1 y por sí
# mismo.

contador=0
numero=int(input('ingrese un numero:'))
for x in range(1, numero+1):
      if numero%x==0:
         contador=contador+1
if contador==2:
   print('el numero es primo')
else:
   print('no es primo')
print('programa finalizado')

# 7. Hacer un programa que solicite 10 números y luego mostrar por pantalla el
# máximo de ellos y la posición en la que fue ingresado.

maximo=0
for x in range(10):
   numeros=int(input('ingrese numeros:'))
   if numeros>maximo:
      maximo=numeros
      posicion=x+1
print('el numero más grande:', maximo,'\nla posición:', posicion, '\nprograma finalizado')

# 8. Hacer un programa que solicite 20 números y luego mostrar por pantalla el
# menor de ellos y la posición en la que fue encontrado.

p=0
m=0
for x in range(20):
   numeros=int(input('ingrese numeros:'))
   if x==0:
      m=numeros
      p=1
   else:
      if numeros<m:
         m=numeros
         p=x+1
print('el numero minimo:', m,'\nla posición:', p, '\nprograma finalizado')

# 9. Hacer un programa que solicite 20 edades y luego calcule el promedio de edad
# de aquellas personas mayores a 18 años.

contador=0
acumulador=0
for x in range(20):
   icosag=int(input('ingrese edad:'))
   if icosag>18:
      contador=contador+1
      acumulador+=icosag
promedio=acumulador/contador
print('el promedio es:', promedio)


# 10. Hacer un programa que solicite 20 números y luego emitir por pantalla el
# máximo de los números pares y el mínimo de los números impares.

banderaBlanca=False
banderaNegra=False
for x in range(20):
   numeros=int(input('ingrese numero:'))
   if numeros%2==0:
      if banderaBlanca==False:
         Mx = numeros
         banderaBlanca=True
      else:
         if Mx < numeros:
            Mx=numeros
   else:#significa que es impar
      if banderaNegra==False:
         Mn=numeros
         banderaNegra=True
      else:
         if Mn > numeros:
            Mn=numeros
print('los numeros pares maximo:', Mx,'\nimpares minimo:', Mn, '\nprograma finalizado')

# 11. Hacer un programa para ingresar 10 números y luego calcule y emita el mayor
# de los primos de la lista. En caso de no haber ningún número primo, deberá
# aclararlo con un cartel.

banderaPirata=False
for x in range(10):
   contador=0
   numero=int(input('ingrese numero:'))
   for z in range(1, numero+1):
      if numero%z==0:
         contador=contador+1
   if contador==2:
      if banderaPirata==False:
         Mx=numero
         banderaPirata=True
      else:
         if numero>Mx:
            Mx=numero
if banderaPirata==False:
   print('está vacia')
else:
   print('el mayor:', Mx)

