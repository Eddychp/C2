class Persona:
    nombre = ''
    edad =""
    altura = ""
    universidad = ''
    Ep = ""

     
    def Nombres(self):
        print (self.nombre)
    def Saber_edad(self):
        print (self.edad)
    def Saber_altura (self):
        print (self.altura)     
    def Centro_de_Est(self):
        print (self.universidad)
    def Escuela_prof (self):
        print (self.Ep)
     
mateo = Persona()
mateo.nombre = ('Mateo')
mateo.edad = ("20 años")
mateo.altura = ("1.66m")
mateo.universidad = ('Universidad Nacional del Altiplano')
mateo.Ep = ("Ingenieria de Minas")

mateo.Nombres()
mateo.Saber_edad()
mateo.Saber_altura()
mateo.Centro_de_Est()
mateo.Escuela_prof()