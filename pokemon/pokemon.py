from style import Style
from type import Type
from powers import power
class pokemon:
    def __init__(this,type=Style,element=Type,atack=int,defense=int,speed=int,life=int,powers=list)->None:
        this.type=type
        this.element=element
        this.atack=atack
        this.defense=defense
        this.speed=speed
        this.life=life
        this.powers=powers
    
    def GetPowers(this,index=int):
        return this.powers[index]
    def PushPowers(this,index=int,new=power):
        this.powers[index]=new

tipo_poder1=Type('planta','agua','fogo')
poder1=power(tipo_poder1,10,'bola de fogo')

tipo_poder2=Type('planta','agua','fogo')
poder2=power(tipo_poder2,20,'lanca-chamas')

poderes=[poder1,poder2]

tipo_pk=Type('planta','agua','fogo')
estilo_pk=Style('attack','defense')

pk=pokemon(estilo_pk,tipo_pk,10,10,10,10,poderes)

poder=pk.GetPowers(1)
print(poder.GetPow(),poder.GetAcuracy())

poder=pk.GetPowers(0)
print(poder.GetPow(),poder.GetAcuracy())