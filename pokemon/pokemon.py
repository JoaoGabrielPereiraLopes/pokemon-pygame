from style import Style
from type import Type
from powers import power

class pokemon:
    def __init__(self, type=Style, element=Type, atack=int, defense=int, speed=int, life=int, powers=list) -> None:
        self.type = type
        self.element = element
        self.atack = atack
        self.defense = defense
        self.speed = speed
        self.life = life
        self.powers = powers
    
    def GetPowers(self, index=int):
        return self.powers[index]
    
    def PushPowers(self, new=power):
        self.powers.append(new)
    
    def GetElement(self) -> Type:
        return self.element
    
    def GetAtack(self):
        return self.atack
    
    def PushAtack(self, value):
        self.atack = value
    
    def GetDefense(self):
        return self.defense
    
    def PushDefense(self, value):
        self.defense = value

    def GetSpeed(self):
        return self.speed
    
    def PushSpeed(self, value):
        self.speed = value

    def GetLife(self):
        return self.life
    
    def PushLife(self, value):
        self.life = value
    
# Instanciação e Uso
tipo_poder1 = Type('planta', 'agua', 'fogo')
poder1 = power(tipo_poder1, 10, 'bola de fogo')

tipo_poder2 = Type('planta', 'agua', 'fogo')
poder2 = power(tipo_poder2, 20, 'lanca-chamas')

poderes = [poder1, poder2]

tipo_pk = Type('planta', 'agua', 'fogo')
estilo_pk = Style('attack', 'defense')

pk = pokemon(estilo_pk, tipo_pk, 10, 10, 10, 10, poderes)

# Exibir Poderes
for i in range(len(pk.powers)):
    poder = pk.GetPowers(i)
    print(poder.GetPow(), poder.GetAcuracy())

# Gravando os valores no arquivo
with open('primeiro.pk', 'w') as aberto:
    aberto.write(f"Ataque: {pk.GetAtack()}\n")
    aberto.write(f"Defesa: {pk.GetDefense()}\n")
    aberto.write(f"Elemento: {pk.GetElement().GetName()}\n")
    aberto.write(f"Vida: {pk.GetLife()}\n")
    for x in pk.powers:
        aberto.write(f"Nome: {x.GetName()}\n")
        aberto.write(f"Elemento: {x.GetElement().GetName()}\n")
        aberto.write(f"Poder: {x.GetPow()}\n")
        aberto.write(f"Acurácia: {x.GetAcuracy()}\n")
    aberto.write(f"Velocidade: {pk.GetSpeed()}\n")
