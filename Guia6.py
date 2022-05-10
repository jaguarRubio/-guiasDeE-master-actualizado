# 1. Se dispone de una lista de 10 grupos de números enteros separados entre ellos
# por ceros. Se pide determinar e informar:
# a. El número de grupo con mayor porcentaje de números impares
# positivos respecto al total de números que forman el grupo.
# b. Para cada grupo, el último número primo y en qué orden apareció en
# ese grupo. Si en un grupo no hubiera números primos, informarlo con
# un cartel aclaratorio.
# c. Informar cuántos grupos están formados por todos números ordenados
# de mayor a menor.

maximoGrupo=0
for x in range(10):#10
   numero=int(input('ingrese numero:'))
   contadorImparPositivo=0
   contadorTotal=0
   banderaDePrimo=False
   posicionDelPrimo=0
   ordenamientoDelGrupo=0
   banderaDelOrden=False
   while numero!=0:
      contadorTotal=contadorTotal+1
      posicionDelPrimo=posicionDelPrimo+1
      if not numero%2==0 and numero>0:
         contadorImparPositivo=contadorImparPositivo+1
      contadorDePrimo=0
      for g in range(1, numero+1):
         if numero%g==0:
            contadorDePrimo=contadorDePrimo+1
      if contadorDePrimo==2:
         cadenaDePrimo=numero
         banderaDePrimo=True
         posicionPrimo=posicionDelPrimo
      numero=int(input('ingrese numero:'))
      if not banderaDelOrden:
         grande=numero
         banderaDelOrden=True
      else:
         if grande>numero:
            grande=numero
            ordenamientoDelGrupo=ordenamientoDelGrupo+1

   porcentajeImparMayorGrupo=(contadorImparPositivo*100)/contadorTotal
   if porcentajeImparMayorGrupo>maximoGrupo:
      maximoGrupo=porcentajeImparMayorGrupo
      posicionDelGrupo=x+1

      
      
   if banderaDePrimo:
      print('el último numero primo es:',cadenaDePrimo, '\nsu posicion:',posicionPrimo)
   else:
      print('no hay un número primo presente.')
print('el grupo:', posicionDelGrupo,'con el mayor porcentaje de impares positivos:',maximoGrupo,'\nla cantidad de grupos ordenados:', ordenamientoDelGrupo)

# 2. Una compañía de electricidad necesita calcular anualmente el consumo que ha
# registrado cada uno de sus usuarios y el monto pagado por cada uno de ellos.
# Para ello tiene un lote de registros por cada uno de los usuarios con los
# siguientes datos:
# • Zona (numérico entero).
# • Número de cliente (número de cuatro dígitos no correlativos).
# • Cantidad de kilovatios consumidos en el periodo.
# El lote se encuentra agrupado (no ordenado) por zona y finaliza con un registro
# con zona igual a cero.
# Se pide generar un listado con el siguiente formato:
# Zona: XX
# Cantidad de usuarios de la zona: XX
# Total facturado en la zona: XX
#
# Zona: XX
# Cantidad de usuarios de la zona: XX
# Total facturado en la zona: XX
# El precio es escalonado según la siguiente escala:
# • $ 0.10 por kv por los primeros 100 kv de consumo.
# • $ 0.12 por kv por el consumo de 101 a 200 kvs.
# • $ 0.15 por kv por el consumo de 201 kvs en adelante.

zona=int(input('ingrese la zona:'))
numeroDeCliente=int(input('ingrese el número de cliente:'))
cantidadDeKvConsumidos=int(input('ingrese la cantidad de kilovatios consumidos:'))
while zona!=0:
   zonaActual=zona
   cantidadDeUsuarios=0
   totalAcumuladoFacturadoPorZona=0
   while zonaActual==zona:
      cantidadDeUsuarios+=1
      if cantidadDeKvConsumidos>200:
         montoDeFactura=cantidadDeKvConsumidos*0.15
      elif cantidadDeKvConsumidos>100:
         montoDeFactura=cantidadDeKvConsumidos*0.12
      else:
         montoDeFactura=cantidadDeKvConsumidos*0.10
      totalAcumuladoFacturadoPorZona+=montoDeFactura
      zona=int(input('ingrese la zona:'))
      numeroDeCliente=int(input('ingrese el número de cliente:'))
      cantidadDeKvConsumidos=int(input('ingrese la cantidad de kilovatios consumidos:'))
   print('zona:',zonaActual,'\ncantidad de usuarios:', cantidadDeUsuarios,'\ntotal facturado por zona:', totalAcumuladoFacturadoPorZona)
print('programa finalizado')

# 3. Hacer un programa para ingresar los valores de los pesos de distintas
# encomiendas que se deben enviar a distintos clientes y que finaliza cuando se
# ingresa un peso negativo. Se deben agrupar las encomiendas en camiones que
# pueden transportar hasta 200 kilos en total.
# Por ejemplo:
# 10, 20, 140, 70, 100, 40, 10, 50, 80, 90, 30, 40, 50, -10.
# Camión 1. Camión 2 Camión 3 Camión 4 Camión 5
# Se pide determinar e informar:
# a. El número de camión y peso total de encomiendas (Camión 1: 170kg,
# Camión 2: 170kg, etc.).
# b. El número de camión que transporta mayor cantidad de encomiendas
# (en el ejemplo anterior sería el camión 3 con 4 encomiendas).
# c. La cantidad de camiones que se terminaron cargando.

camionesCantidad=0
maximo=0
peso=int(input('ingrese el peso:'))
while peso>0:
   camionesCantidad=camionesCantidad+1
   acumuladorDePeso=0
   encomienda=0
   while peso+acumuladorDePeso<=200 and peso>0:
      acumuladorDePeso+=peso
      encomienda=encomienda+1
      peso=int(input('ingrese el peso:'))
   print('numero de camion:', camionesCantidad, '\ntotal de peso de encomiendas:', acumuladorDePeso)

   if encomienda>maximo:
      maximo=encomienda
      camionMaximo=camionesCantidad
print('\ncamion que transporta más encomiendas:',camionMaximo,'\ncantidad de encomiendas:',maximo,'\ncamiones totales usados:', camionesCantidad,'\nprograma finalizado')

# 4. Una compañía de turismo aventura registró los paquetes vendidos durante la
# última temporada vacacional. Para cada venta se ingresó:
# • Número de paquete (4 dígitos no correlativos).
# • Cantidad de personas incluidas.
# • Precio por persona.
# • Horas totales de actividades.
# • Tipo de aventura (“M”, Montaña. “T”, Trekking. “R”, Rafting. “B”, Bicicleta.
# “C”, Canopy. “E”, Escalar. “K”, Sky. “S”, Snowboard. “J”, Jumping. “P”,
# Parapente).
# El lote se encuentra no ordenado y agrupado por tipo de aventura y corta con
# número de paquete cero. En el lote no se ingresan registros cuyo tipo de aventura
# no se haya vendido.
# A partir de dichos datos, se solicita informar:
# a. La cantidad de paquetes vendidos de cada tipo de aventura..
# b. La cantidad total de personas que disfrutaron de las aventuras durante la
# temporada.
# c. El total recaudado por cada venta.
# d. La venta con mayor importe de cada tipo de aventura.
# e. El paquete con menos horas incurridlas y en qué tipo de actividad fue.

nuPa=int(input('ingrese número de paquete:'))
canPeI=int(input('ingrese número de cantidad de personas incluidas:'))
prePoPe=int(input('ingrese número de precio por persona:'))
hoTo=int(input('ingrese número horas totales:'))
tiAv=input('ingrese tipo de aventura:')

minAv=tiAv
min=hoTo
canPeTo=0

while nuPa!=0:
   tiAvAc=tiAv
   miTa=0
#   toRePoCaAv=0 (mi error)
   caPeAv=0
   while tiAvAc==tiAv:
      caPeAv+=1
      canPeTo+=canPeI
      toReCaVe=canPeI*prePoPe
      print('el total recaudado por cada venta:',toReCaVe)
      if toReCaVe>miTa:
         miTa=toReCaVe
      if hoTo<min:
         min=hoTo
         minAv=tiAvAc
   print('cantidad de personas en la aventura:',caPeAv)
   print('venta con mayor importe de aventura:', miTa)
print('cantidad de personas totales en la temporada:',canPeTo)
print('aventura con menor horas incurridas:', minAv,'con:',min,'horas')

# 5. Una empresa registró las compras realizadas a sus distintos proveedores durante
# todo el año anterior. Para cadacompra se registraron los siguientes datos:
# • Número de proveedor (número de cuatro cifras no correlativo).
# • Día (1 a 31).
# • Mes (1 a 12).
# • Tipo de Factura (Responsable inscripto: "A",Consumidor Final: "B", o
# Monotributo: "C").
# • Número de Producto (número no correlativo).
# • Cantidad comprada.
# • Precio unitario del producto.
# Este lote finaliza con un registro con número de proveedor igual a 0.
# Los registros están agrupados por número de proveedor. En el lote anterior no
# aparecen
# registros de los proveedores a los que que no se les hayan realizado compras.
# Se pide determinar e informar:
# a. El monto máximo registrado en una sola compra por cada proveedor y el
# número de proveedor al que se le compró.
# b. La inversión total de todo el año discriminada por tipo de factura.
# c. La compra con menor monto registrada durante el mes de Agosto junto al
# número de producto comprado.
# d. La cantidad de compras que se realizaron a cada proveedor.
# e. El número de producto con mayor cantidad comprada en una sola compra y
# en qué proveedor se compró.