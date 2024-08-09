class Type:
    def __init__(self, vantagem=str, desvantagem=str, name=str) -> None:
        self.vantagem = vantagem
        self.desvantagem = desvantagem
        self.name = name
    
    def Get(self) -> list:
        return [self.vantagem, self.desvantagem, self.name]
    
    def GetDesvantagem(self) -> str:
        return self.desvantagem
    
    def GetVantagem(self) -> str:
        return self.vantagem
    
    def GetName(self) -> str:
        return self.name
