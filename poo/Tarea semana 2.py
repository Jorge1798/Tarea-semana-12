# Definimos la clase base para todos los personajes.
class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # Atributos comunes a todos los personajes
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        # Imprime los atributos del personaje
        print(f"\n== Atributos de {self.nombre} ==")
        print(f"· Fuerza: {self.fuerza}")
        print(f"· Inteligencia: {self.inteligencia}")
        print(f"· Defensa: {self.defensa}")
        print(f"· Vida: {self.vida}")

    def esta_vivo(self):
        # Retorna True si el personaje está vivo
        return self.vida > 0

    def recibir_daño(self, cantidad):
        # Disminuye la vida del personaje cuando recibe daño, sin bajar de 0
        self.vida -= cantidad
        self.vida = max(self.vida, 0)  # Evitar valores negativos
        print(f"{self.nombre} ha recibido {cantidad} de daño. Vida restante: {self.vida}")
        if not self.esta_vivo():
            print(f"💀 {self.nombre} ha muerto.")

    def calcular_daño(self, enemigo):
        # Calcula el daño causado al enemigo (puede ser modificado por clases hijas)
        return max(self.fuerza - enemigo.defensa, 0)

    def atacar(self, enemigo):
        # Realiza el ataque al enemigo
        daño = self.calcular_daño(enemigo)
        print(f"{self.nombre} ataca a {enemigo.nombre} causando {daño} de daño.")
        enemigo.recibir_daño(daño)


# Clase derivada: Guerrero
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        # Inicializamos atributos del padre y uno nuevo: espada
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada  # Multiplicador de daño

    def calcular_daño(self, enemigo):
        # Guerrero usa su espada para causar más daño
        return max((self.fuerza * self.espada) - enemigo.defensa, 0)

    def atributos(self):
        # Imprime atributos incluyendo el arma
        super().atributos()
        print(f"· Espada (nivel): {self.espada}")


# Clase derivada: Hechicero
class Hechicero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro_magico):
        # Inicializamos atributos del padre y uno nuevo: libro mágico
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro_magico = libro_magico  # Potencia mágica

    def calcular_daño(self, enemigo):
        # Hechicero usa inteligencia y su libro para calcular daño
        return max((self.inteligencia * self.libro_magico) - enemigo.defensa, 0)

    def atributos(self):
        # Imprime atributos incluyendo el libro mágico
        super().atributos()
        print(f"· Libro Mágico (nivel): {self.libro_magico}")


# Función que controla el combate entre dos personajes
def combate(personaje1, personaje2):
    turno = 1
    while personaje1.esta_vivo() and personaje2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        personaje1.atacar(personaje2)
        if personaje2.esta_vivo():
            personaje2.atacar(personaje1)
        turno += 1

    # Determinar el ganador
    print("\n>>> Resultado Final <<<")
    if personaje1.esta_vivo() and not personaje2.esta_vivo():
        print(f"🏆 {personaje1.nombre} ha ganado el combate.")
    elif personaje2.esta_vivo() and not personaje1.esta_vivo():
        print(f"🏆 {personaje2.nombre} ha ganado el combate.")
    else:
        print("🤝 ¡Ambos personajes han muerto! Es un empate.")


# Crear instancias de los personajes
g1 = Guerrero("Leonidas", fuerza=18, inteligencia=5, defensa=6, vida=100, espada=3)
m1 = Hechicero("Merlín", fuerza=4, inteligencia=20, defensa=4, vida=90, libro_magico=4)

# Mostrar atributos
g1.atributos()
m1.atributos()

# Iniciar combate
combate(g1, m1)

