from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona

# Creamos el objeto para mi archivo
m = MiArchivo()
# Creamos una lista que almacene las lineas de mi archivo
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

sum_n1 = 0
sum_n2 = 0
lista = lista[1:]

# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])

#En el siguiente for almacenamos cada linea en el objeto y vemos q cada nota sea menor a 15
for d in lista:
    # print(d)
    #sum_n1 = sum_n1 + int(d[4])

    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])
    sum_n1 = sum_n1 + p.obtener_nota1()
    sum_n2 = sum_n2 + p.obtener_nota2()
    
    if (p.obtener_nota1()<15 or p.obtener_nota2()<15) :
    	print(p.obtener_nombre())

# Finalmente promediamos las sumas que hicimos en el for
resultado = sum_n1/len(lista)
resultado2 = sum_n2/len(lista)

print(resultado)
print(resultado2)

