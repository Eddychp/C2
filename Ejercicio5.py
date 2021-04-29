class OperacionesCombinadas :
    def __init__(self, numb1, numb2, numb3):
        self.numb1 = numb1
        self.numb2 = numb2
        self.numb3 = numb3
    def Halla(self):
        print(self.numb1**self.numb2/self.numb3)

obj =OperacionesCombinadas(2,2,2)
obj.Halla()

