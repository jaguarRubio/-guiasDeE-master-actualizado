# m = 44

# for h in range(m):
#     print(' ' * (m-h), 'M' * (2*h+1))

# cannon=[0]*5
# print(cannon)

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
   print('zona:',zonaActual,'\ncantidad de usuarios:', cantidadDeUsuarios,'\ntotal facturado por zona:', totalAcumuladoFacturadoPorZona, '\n')
print('programa finalizado')