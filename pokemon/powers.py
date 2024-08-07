from type import Type

class power:
    def __init__(this,element=Type,pow=int,name=str) -> None:
        this.element=element
        this.pow=pow
        this.acuracy=101-pow
    
    def PutAcuracy(this,value=0)->None:
        this.acuracy+=value
    def GetAcuracy(this):
        return this.acuracy
    
    def PutPow(this,value=0)->None:
        this.pow+=value
    def GetPow(this):
        return this.pow
    
    def GetElement(this):
        return this.element