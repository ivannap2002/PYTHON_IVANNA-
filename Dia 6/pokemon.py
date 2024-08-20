class pokemon:
    # atributos están definidos en el constructor 
    nombre = None
    tipo = None
    vida = None
    evolucion = None
    ataque = None

    def __init__(self, nombre, tipo, vida=100, evolucion=1):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.evolucion = evolucion  # 1 o 2 o 3
        self.ataque = []

    def setAtaque(self, ataque):
        self.ataque.append(ataque)

    def atacar(self, i):
        return(f"{self.nombre} ataco con {self.ataque[i]}")

    def defenderse(self):
        return(f"{self.nombre} se defendio")

if __name__ == "__main__":
    picachu = pokemon(tipo="ELECTRICO", nombre="PICACHU", vida=200)
    chariza = pokemon(tipo="FUEGO", nombre="CHARIZA", vida=300, evolucion=3)

    # Agregando ataques
    chariza.setAtaque("ELECTRICO")
    picachu.setAtaque("FUEGO")
    picachu.setAtaque("RAFAGA")
    picachu.setAtaque("FUEGO")


    print(picachu.atacar(0))

    print(chariza.defenderse())