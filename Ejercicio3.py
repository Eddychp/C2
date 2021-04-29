class PanelSolar:
    color = ''
    medidas = ''
    estadoActual=""

     
    def ScoloR(self):
        print (self.color)
         
    def Smedidas(self):
        print (self.medidas)
    def Sestado(self):
        print (self.estadoActual)
     
obj = PanelSolar()
obj.color = ('negro')
obj.medidas = ('4*3')
obj.estadoActual = ("sin funcionamineto")
obj.ScoloR()
obj.Smedidas()
obj.Sestado()