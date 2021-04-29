class Operaciones:
    def __init__(self, nomb1, nomb2):
        self.nomb1=nomb1
        self.nomb2=nomb2
    def suma(self):
        print (self.nomb1+self.nomb2)
    def restas(self):
        print (self.nomb1-self.nomb2)
    def multiplicacion(self):
        print (self.nomb1*self.nomb2)
    def divicion(self):
        print (self.nomb1/self.nomb2)

obj = Operaciones(2,3)
obj.restas()
obj.suma()
obj.multiplicacion()
obj.divicion()