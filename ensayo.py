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
print('par máximo:',max,'cantidad de impares:',contadorImpar,'primo mínimo:', min)