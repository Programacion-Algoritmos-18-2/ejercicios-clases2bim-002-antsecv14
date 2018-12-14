"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod, n1, n2):
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota1 = int(n1)
        self.nota2 = int(n2)
# Creamos los get y set de cada variable
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo

    def agregar_apellido(self):
        self.apellido = ape
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    def obtener_nota1(self):
        return self.nota1

    def agregar_nota1(self, n1):
        self.nota1 = int(n1)

    def obtener_nota2(self):
        return self.nota2

    def agregar_nota2(self, n2):
        self.nota2 = int(n2)


    def __str__(self):
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.obtener_nombre(), self.obtener_apellido(),\
                self.obtener_edad(), self.obtener_codigo(), self.obtener_nota1(), self.obtener_nota2())


class OperacionesPersona(object):
    """
    """
    
    def __init__(self, listado):
        """
        """
        self.lista_personas = listado
#Creamos el str para sobreescribir el metodo
    def __str__(self):
        """ """
        cadena = ""
        for n in self.lista_personas:
            cadena = "%s %s %s\n" % (cadena, n.obtener_nombre(),n.obtener_apellido())
        return cadena
#Dentro del siguiente metodo obtenemos el primedio de la nota 1 de cada estudiante
    def obtener_promedio_n1(self):
        suma_n1 = 0
        for n in self.lista_personas:
            suma_n1 = suma_n1 + n.obtener_nota1()
        resultado = suma_n1/len(self.lista_personas)
        return resultado
#Dentro de el siguiente metodo obtenemos el promedio d ela nota 2 de cada estudiante
    def obtener_promedio_n2(self):
        suma_n2 = 0
        for n in self.lista_personas:
            suma_n2 = suma_n2 + n.obtener_nota2()
        resultado2 = suma_n2/len(self.lista_personas)
        return resultado2
#Obtener listado_n1 sirve para obtener las notas 1 menores a 15
    def obtener_listado_n1(self):

        for n in self.lista_personas:
            if (n.obtener_nota1()<15):
                return n 
#Obtener_listado_n2 sirve para obtener las notas 2 menores a 15
    def obtener_listado_n2(self):

        for n in self.lista_personas:
            if (n.obtener_nota2()<15):
                return n
#Obtener_listado_personas_n sirve para obtener las notas menores a 15 y los estudiantes culla inicial de su nombre sea R o J
    def obtener_listado_personas_n(self,letra1, letra2):
        cadena = ""
        for n in self.lista_personas:

            if(n.obtener_nota1() < 15 and (n.obtener_nombre()[0] == letra1 or n.obtener_nombre()[0] == letra2) ):
                cadena =cadena + n.obtener_nombre() + "\n"

            if(n.obtener_nota2() < 15 and (n.obtener_nombre()[0] == letra1 or n.obtener_nombre()[0] == letra2) ):
                cadena = cadena + n.obtener_nombre()

        return cadena
            

