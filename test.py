superlist = ['/portal/productos-persona/seguros-vehiculos/seguro-auto-flexible','/portal/productos-persona/seguros-vehiculos/seguroxkm','/portal/productos-persona/seguros-de-vida-y-accidentes/enfermedades-protegidas']

for item in superlist:
    split = item.split('/')
    print(split[-1])
