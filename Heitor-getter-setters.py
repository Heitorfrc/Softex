'''
Crie uma classe e insira nela, no mínimo, dois atributos, os quais devem ter um método acessor (get) e um método modificador 
(set) para cada. Defina um objeto para cada atributo e elabore um construtor para criar alguma regra.
'''

#o exemplo pede GET e SET, que utilizei, porém em Py @property é mais apropriado


def effectiveness(self) :
    if self == "psychic" :
        print("It's super effective!")
    else :
        print("It's not very effective...")

class pokemon :
    def __init__(self, name, type, lvl=15) :
        self.name = name
        self.type = type
        self._lvl = lvl
    # getter
    def get_lvl(self) :
        return self._lvl
    # setter
    def set_lvl(self, newlvl) :
        if newlvl > 0 and newlvl < 99 :
            self._lvl = newlvl
        

p1 = pokemon("Abra", "psychic")
p2 = pokemon("Nidorino", "poison")

print(p1.name, p1.type, p1._lvl)
effectiveness(p1.type)
print(p2.name, p2.type, p2._lvl)
effectiveness(p2.type)