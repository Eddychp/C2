class Carro:

    color =""
    modelo = ""
    Vmaxima = ""
    medidas = ""
    capacidad_de_pasageros =""
    def El_color(self):
        print (self.color)
    def El_modelo(self):
        print (self.modelo)
    def La_velo_max (self):
        print (self.Vmaxima)
    def La_medidas (self):
        print (self.medidas)
    def La_capacidad (self):
        print (self.capacidad_de_pasageros)

obj =  Carro()
obj.color =("El color es negro")
obj.modelo = ("Renaul logan 2008")
obj.Vmaxima = ("190 kh")
obj.medidas = ("1.73*260")
obj.capacidad_de_pasageros = ("4 personas")
obj.El_color()
obj.El_modelo()
obj.La_velo_max()
obj.La_medidas()
obj.La_capacidad()



