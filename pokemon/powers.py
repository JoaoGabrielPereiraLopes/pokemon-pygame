from type import Type

class power:
    def __init__(self, element=Type, pow=int, name=str) -> None:
        self.element = element
        self.pow = pow
        self.acuracy = 101 - pow
        self.name = name  # Adicionando o atributo name
    
    def PutAcuracy(self, value=0) -> None:
        self.acuracy += value
    
    def GetAcuracy(self):
        return self.acuracy
    
    def GetName(self):
        return self.name

    def PutPow(self, value=0) -> None:
        self.pow += value
    
    def GetPow(self):
        return self.pow
    
    def GetElement(self):
        return self.element
