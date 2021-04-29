class MRU:
    def __init__(self, v, t):
        self.v = v
        self.t = t
    def hallaE(self):
        print (self.v*self.t)

espacio = MRU(3,7)      
espacio.hallaE()