# 1. Hacer una función llamada “producto” que reciba dos números enteros y que
# devuelva el producto de ambos. Luego hacer un programa que pida el precio
# de un artículo y la cantidad vendida y muestre por pantalla el monto total a
# pagar. Usar la función.

def producto(nu1, nu2):
   re=nu1*nu2
   return re
na0=int(input('ingrese número:'))
na1=int(input('ingrese número:'))
print(producto(na0, na1))
print('-'*22)
def monto(preAr, canVe):
   montoTo=preAr*canVe
   return montoTo
precio=int(input('ingrese el precio del articulo:'))
vendido=int(input('ingrese la cantidad vendida del articulo:'))
print('el monto total es:','$'+str(monto(precio, vendido)),'\nprograma finalizado')

# 2. Hacer una función llamada “mayor” que reciba dos números enteros y
# devuelva el mayor de ellos o cero si son iguales.

def mayor(nu1, nu2):
   if nu1>nu2:
      return nu1
   elif nu2>nu1: return nu2
   else:
      return '0'
nu1=int(input('ingrese numero:'))
nu2=int(input('ingrese numero:'))
print(mayor(nu1, nu2))

# 3. Hacer una función llamada “par” que reciba un número entero y devuelva 1 si
# es par o cero si no lo es. Hacer un programa para ingresar 20 números y
# mostrar por pantalla cuántos son pares.

def par(nu0):
   if nu0%2==0:
      return True
   else:
      return False
n00=int(input('ingrese numero:'))
print(par(n00))
print('-'*22)
contadorPar=0
for g in range(20):
   valorSin=int(input('ingrese valor:'))
   if par(valorSin):
      contadorPar+=1
print(contadorPar)

# 4. Hacer una función llamada “primo” que reciba un número entero y devuelva 1
# si el número es primo o cero si no lo es. Hacer un programa para ingresar
# números. El lote corta cuando se ingresa un número cero. Informar el
# promedio teniendo en cuenta sólo los números primos.

def primo(va):
   contadorPri=0
   for f in range(1, va+1):
      if va%f==0:
         contadorPri+=1
   if contadorPri==2:
      return True
   else: #opcional
      return False
numeros=int(input('ingrese numero;'))
contadorGen=0
contadorPrim=0
while numeros!=0:
   contadorGen+=1
   if primo(numeros):
      contadorPrim+=1
   numeros=int(input('ingrese numero;'))
promedio=(contadorPrim*100)/contadorGen
print(promedio)

# 5. Hacer una función llamada “pagos” que reciba un monto (float) y una cantidad
# de pagos (entero) y devuelva el monto de cada pago. Hacer un programa para
# ingresar 10 ventas. Para cada venta se conoce el monto y la cantidad de pagos.
# El programa deberá mostrar la cantidad de pagos y el monto del pago para
# cada una de las ventas.

def pagos(mo, canPa):
   canMoPa=mo/canPa
   return canMoPa
for e in range(10):
   monto=float(input('ingrese monto:'))
   cantiDPag=int(input('ingrese cantidad de pagos:'))
   print(pagos(monto, cantiDPag))

# 6. Hacer una función que se llame “sumaResta” que reciba dos números y que
# devuelva la suma Y la resta del primer número con el segundo.
# Nota: recordemos que una función solo puede devolver UN valor por return.
# Cómo podríamos hacer para tener ambos resultados en el main?

def sumaResta(nu1, nu2):
   adiccion=nu1+nu2
   sustraccion=nu1-nu2
   return (adiccion, sustraccion)
nu0=int(input('ingrese numero:'))
nu1=int(input('ingrese numero:'))
print(sumaResta(nu0,nu1))

# 7. Hacer una función de tipo void (porque no va a devolver nada) llamada
# “positivoNegativoCero” que reciba un número por valor y una variable por
# referencia. Que analice el número y escriba variable recibida por referencia
# con:
# a. 1 si el número es positivo.
# b. -1 si el número es negativo.
# c. 0 si el número es cero.
# Hacer un programa main que permita ingresar 100 números y emitir por
# pantalla cuántos son positivos, cuántos negativos y cuántos cero.

def positivoNegativoCero(nu, vari):
   if nu>0:
      vari.append(nu)
   elif nu<0:
      vari.append(nu)
   else:
      vari.append(nu)

banderaNarnia=0
posi=0
nega=0
cero=0
for qu in range(10):    #100
   numeros=int(input('ingrese numero:'))
   oveja=[]
   banderaNarnia=positivoNegativoCero(numeros, oveja)  #here
   if oveja[0]>0:
      posi+=1
   elif oveja[0]<0:
      nega+=1
   else:
      cero+=1
print(cero, nega, posi)

# 8. Hacer un programa que permita ingresar una lista de números que corta
# cuando se ingresa un cero. A partir de dichos datos informar:
# a. El mayor de los números pares.
# b. La cantidad de números impares.
# c. El menor de los números primos.
# Hacer uso de las funciones anteriormente desarrolladas.

def parOimpar(nu):
    if nu%2==0:
        return nu
    else:
        return False
def parienteF(nu):
    contadorPrimo=0
    for g in range(1, nu+1):
       if nu%g==0:
          contadorPrimo+=1
    if contadorPrimo==2:
       return True
    else:
       return False

numero=int(input('ingrese numero:'))
max=0
contadorImpar=0
banderaPirata=False
while numero != 0:
    bp=parOimpar(numero)
    if bp:
       if bp>max:
          max=numero
    else:
       contadorImpar+=1
    
    primo=parienteF(numero)
    if primo:
       if not banderaPirata:
          min=numero
          banderaPirata=True
       else:
          if numero<min:
             min=numero
    numero=int(input('ingrese numero:'))
print('par máximo:',max,'cantidad de impares:',contadorImpar,'primo mínimo:', min,'\nprograma finalizado')
