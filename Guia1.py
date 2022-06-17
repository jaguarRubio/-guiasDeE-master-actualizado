# 1. Hacer un programa para solicitar por teclado un número y luego devolver su
# valor elevado al cubo.
# Nota: no olvides que sólo contamos con las cuatro operaciones básicas.

numero=int(input('ingrese numero:'))
numero=numero*numero*numero
print(numero, '\nprograma finalizado')


# 2. Hacer un programa que permita ingresar el año actual y el año de la fecha de
# nacimiento de una persona y luego calcule y emita por pantalla su edad.
# Nota: no hay que tener en cuenta si la persona cumplió años o no,
# simplemente calcular.

annoActual=int(input('ingresa el año contemporáneo:'))
annoDeNacimiento=int(input('ingresa el año de la fecha de nacimiento:'))
print('la edad es:', annoActual-annoDeNacimiento, 'años aproximadamente.', '\nprograma finalizado')


# 3. Hacer un programa que permita ingresar los kilómetros existentes entre dos
# ciudades y la velocidad promedio de un vehículo. Calcular y emitir por pantalla
# el tiempo aproximado que demandará llegar de un punto a otro teniendo en
# cuenta los datos ingresados.

distancia=int(input('ingrese la distancia espacial en kilometros de las dos ciudades:'))
velocidadDelVehiculo=int(input('ingrese la velocidad del vehiculo en kilometros:'))
print('el vehiculo arrivara aproximadamente en:', distancia/velocidadDelVehiculo, 'horas', '\nprograma finalizado')

# 4. Una casa de computación paga a sus empleados un sueldo fijo de ARS15000
# más una comisión del 5% sobre el total facturado por cada empleado. Hacer un
# programa para ingresar el total facturado por un empleado y que luego calcule
# y emita por pantalla el sueldo total a cobrar por el mismo.

totalFacturado=int(input('ingresar el total facturado por empleado:'))
añadidoComision=totalFacturado*1.05
print('el sueldo final es:', añadidoComision, 'pesos', '\nprograma finalizado')

# 5. Hacer un programa para ingresar por teclado las tres notas de exámenes de un
# alumno y luego calcule y emita por pantalla el promedio final.

print('¿cuantas unidades presentes hay de notas?:')
cantidadNotas=int(input('cantidad:'))
contador=cantidadNotas
notasTotal=0
while contador>0:
   notas=int(input('ingrese los valores de las notas:'))
   notasTotal+=notas
   contador=contador-1
print('el promedio es:',notasTotal/cantidadNotas,'puntos')

# 6. Hacer un programa para ingresar por teclado los metros cuadrados totales de
# un predio y los metros cuadrados cubiertos; luego calcular y mostrar por
# pantalla el porcentaje de metros cuadrados cubiertos y el porcentaje de
# metros cuadrados descubiertos.

predioTotal=float(input('ingrese predio total en kilometros cuadrados:'))
predioCubierto=float(input('ingrese predio cubierto en kilometros cuadrados:'))
predioDescubierto=predioTotal-predioCubierto
porcentajeDePredioCubierto=predioCubierto*100/predioTotal
porcentajeDePredioDescubierto=predioDescubierto*100/predioTotal
print('el porcentaje del predio cubierto es:', '%'+str(porcentajeDePredioCubierto),'\ny del predio descubierto:', '%'+str(porcentajeDePredioDescubierto), '\nprograma finalizado')

# 7. Una importante cadena de delivery cuenta con una promoción por tiempo
# limitado en la que otorga un 15% de descuento sobre el total del valor de la
# compra realizada. Hacer un programa para solicitar el monto total y el mismo
# calcule y emita por pantalla el total a cobrar con el descuento aplicado.

monto=int(input('ingrese el monto:'))
print('el monto total, añadiendo descuento es:', '$'+str(monto*0.85),'\nprograma finalizado')

# 8. Una universidad desea conocer los porcentajes de mujeres y hombres en las
# carreras de ciencias exactas. Se solicita un programa para cargar la cantidad de
# mujeres y la cantidad de hombres y que el mismo calcule y emita por pantalla
# los porcentajes correspondientes.

masculinos=float(input('cantidad de masculinos:'))
femeninos=float(input('cantidad de femeninas:'))
print('el porcentaje de masculinos es:', '%'+str((masculinos*100)/(masculinos+femeninos)),'\ny la cantidad de femeninas es:', '%'+str((femeninos*100)/(femeninos+masculinos)),'\nprograma finalizado')

# 9. Hacer un programa que permita ingresar por teclado dos números y que luego
# muestre por pantalla la suma, la resta, la multiplicación y la división de dichos
# números. Se deben mostrar cuatro resultados en pantalla. Los números deben
# ser solicitados una única vez.

numero0=int(input('primer numero:'))
numero1=int(input('segundo numero:'))
print('suma:', numero0+numero1,'\nresta:', numero0-numero1, '\nmultiplicación:', numero0*numero1, '\ndivision:', numero0/numero1, '\nprograma finalizado')



