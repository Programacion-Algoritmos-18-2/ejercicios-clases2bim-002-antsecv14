

#Importramos las clases que vamos a usar en nuestro run 
from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona
#Creamos un objeto de la clase MiArchivo
m = MiArchivo()
#Creamos un listaque almacene la informacion de MiArchivo
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)
# Utilizamos los objetos de la lista desde su posicion 1
lista = lista[1:]
lista_personas = []
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])

# Creamos un for para recorrer la lista y dentro del objeto almacenamos cada linea
for d in lista:
    # print(d)
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])
    #Agregamos a lista_personas cada el objeto q creamos
    lista_personas.append(p)

# Creamos un objeto tiopo OperacionesPersona
operaciones = OperacionesPersona(lista_personas)

#Imprimimos cada metodo que desarrollamos en nuestra clase OperacionesPersona
print("Promedio nota 1 : ", operaciones.obtener_promedio_n1())

print("Promedio nota 2 : ",operaciones.obtener_promedio_n2())

print("Estudiantes con su nota 1 menor a 15 : \n >",operaciones.obtener_listado_n1())

print("Estudiantes con su nota 2 menor a 15 : \n >",operaciones.obtener_listado_n2())

print("Estufiantes con iniciales de R o J : \n",operaciones.obtener_listado_personas_n("R","J"))
