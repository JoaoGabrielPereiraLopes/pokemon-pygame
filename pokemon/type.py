class Type():
    def __init__(this,vantagem=str,desvantagem=str,name=str)->None:
        this.vantagem=vantagem
        this.desvantagem=vantagem
        this.name=name
    def Get(this)->list:
        return [this.vantagem,this.desvantagem,this.name]
    def GetDesvantagem(this)->str:
        return this.desvantagem
    def GetVantagem(this)->str:
        return this.vantagem
    def GetName(this)->str:
        return this.name