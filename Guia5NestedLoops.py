# 1. Hacer un programa para mostrar los números del 1 al 10. No se debe realizar
# ningún pedido de datos. USANDO WHILE.

diez=1
while diez<=10:
   print(diez)
   diez=diez+1
print('programa finalizado')

# 2. Hacer un programa para mostrar los números del 10 al 1. No se debe realizar
# ningún pedido de datos. USANDO WHILE.

diez=10
while diez>0:
   print(diez)
   diez=diez-1
print('programa finalizado')

# 3. Hacer un programa que solicite la edad de un grupo de personas. El programa
# deberá pedir edades hasta que se ingrese una edad menor a 18 años. Deberá
# mostrar por pantalla cuántas personas mayores se registraron.

contador=0
personas=int(input('ingrese edad:'))
while personas>18:
   personas=int(input('ingrese edad:'))
   contador=contador+1
print('cantidad:', contador, '\nprograma finalizado')

# 4. Hacer un programa que solicite dos números y luego muestre los números
# entre el menor y el mayor de ellos. Acordate, usando While.

numero0=int(input('ingrese el primer numero:'))
numero1=int(input('ingrese el segundo numero:'))
if numero0>numero1:
   Grande=numero0
   Pequenno=numero1
else:
   Grande=numero1
   Pequenno=numero0
while Grande>Pequenno:
   Pequenno=Pequenno+1
   print(Pequenno)
print('programa finalizado')

# 5. Hacer un programa que muestre los números del 1 al 100 de 5 en 5. Ejemplo:
# 0, 5, 10, 15, 20.... 100. Usando While.

caja=0
while caja<=100:
   print(caja)
   caja=caja+5
print('programa finalizado')

# 6. Hacer un programa que solicite UN número y luego calcule y emita un cartel
# aclaratorio si el mismo es primo o no es primo.
# Nota: usando While. Ya lo hicimos con FOR, ahora con While.

numero=int(input('ingresar numero:'))
b=1
contador=0
while b<=numero:
   if numero%b==0:
      contador+=1
   b=b+1
print(b, '\n', contador)#innecesario
if contador==2:
   print('el numero es primo')
else:
   print('no es primo')
print('programa finalizado')

# 7. Hacer un programa que solicite una lista de números que corta cuando se
# ingresa un cero y luego mostrar por pantalla el máximo de ellos y la posición
# en la que fue ingresado.

Pscon=1
banderaPirata=1
banderaNarnia=False
while banderaPirata!=0:
   numeros=int(input('ingrese numero:'))
   if numeros == 0:
      banderaPirata=0
   else:
      if banderaNarnia==False:
         Mx=numeros
         PscGuardada=1
         banderaNarnia=True
      else:
         Pscon+=1
         if numeros>Mx:
            Mx=numeros
            PscGuardada=Pscon
print('valor maximo:', Mx, '\nposición:', PscGuardada)

# 8. Hacer un programa que solicite una lista de números que corta cuando se
# ingresa un cero y luego mostrar por pantalla el menor y el segundo menor.

banderaPirata=False
banderaBlanca=False
numeros=int(input('ingrese numero:'))
while numeros!=0:
   if not banderaPirata:
      priMin=numeros
      banderaPirata=True
   else:
      if not banderaBlanca:
         segMin=numeros
         banderaBlanca=True
      else:
         if numeros<priMin:
            efimero=priMin
            segMin=priMin
            priMin=numeros
         else:
            if numeros<segMin:
               segMin=numeros
   numeros=int(input('ingrese numero:'))
print('el numero mínimo es:',priMin,'\nel siguiente es:',segMin, '\nprograma finalizado')


# 9. Realizar el nuevamente el ejercicio 8 pero ahora debe devolver además la
# posición en la que fue encontrado cada uno de los mínimos.

banderaPirata=False
banderaBlanca=False
cajaBlanca=0
cajaPirata=0
posicionBlanco=0
posicionPirata=0
numeros=int(input('ingrese numero:'))
while numeros!=0:
   cajaBlanca=cajaBlanca+1
   cajaPirata=cajaPirata+1
   if not banderaPirata:
      priMin=numeros
      banderaPirata=True
      posicionPirata=cajaPirata
   else:
      if not banderaBlanca:
         segMin=numeros
         banderaBlanca=True
         posicionBlanco=cajaBlanca
      else:
         if numeros<priMin:
            efimero=priMin
            segMin=priMin
            priMin=numeros
            banderaPirata=cajaPirata
         else:
            if numeros<segMin:
               segMin=numeros
               banderaBlanca=cajaBlanca
   numeros=int(input('ingrese numero:'))
print('el numero mínimo es:',priMin,'\nsu posición:',posicionPirata,'\nel siguiente es:',segMin,'\nsu posicion',posicionBlanco,'\nprograma finalizado')

# 10. Hacer un programa que solicite una lista de números que corta cuando se
# ingresa un cero y luego emitir por pantalla el máximo de los números
# negativos y el mínimo de los números positivos.

numeros=int(input('ingrese numero:'))
banderaPirata=False
banderaBlanca=False
while numeros!=0:
   if numeros<0:
      if not banderaPirata:
         Mmn=numeros
         banderaPirata=True
      else:
         if Mmn>numeros:
            Mmn=numeros
   else:
      if not banderaBlanca:
         Mnp=numeros
         banderaBlanca:True
      else:
         if Mnp<numeros:
            Mnp=numeros
   numeros=int(input('ingrese numero:'))
print('el mínimo positivo es:',Mnp,'\nel maximo negativo es:',Mmn,'\nprograma finalizado')


# 11. Hacer un programa para ingresar una lista de números que corta cuando se
# ingresa un cero y luego mostrar: la cantidad de números primos, la cantidad de
# números pares, la cantidad de positivos y la cantidad de negativos.

numeros=int(input('ingrese numero:'))
cantidadDePositivos=0
cantidadDeNegativos=0
cantidadDePares=0
cantidadDePrimos=0
while numeros!=0:
   if numeros>0:
      cantidadDePositivos=cantidadDePositivos+1
   else:
      if numeros<0:
         cantidadDeNegativos=cantidadDeNegativos+1
   if numeros%2==0:
      cantidadDePares=cantidadDePares+1
   contadorPara=0
   for x in range(1,numeros+1):
      if contadorPara==2:
         cantidadDePrimos=cantidadDePrimos+1
   numeros=int(input('ingrese numero:'))
print('la cantidad de numeros positivos:',cantidadDePositivos,'\nla cantidad de numeros negativos:',cantidadDeNegativos,'\nla cantidad de pares:',cantidadDePares,'\nla cantidad de primos:',cantidadDePrimos,'\nprograma finalizado')