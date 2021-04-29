class Binomio_al_cuadrado :

    def __init__(self, numb1, numb2):
        self.numb1 = numb1
        self.numb2 = numb2

    def Halla_binomio(self):
        print(self.numb1**2+2*self.numb1*self.numb2+self.numb2**2)

obj = Binomio_al_cuadrado(2,2)
obj.Halla_binomio()
