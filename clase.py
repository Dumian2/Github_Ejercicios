class Personaje:
    def __init__(self, nombre, vida, fuerza, inteligencia, defensa, aguante): #atributos
        self.nombre = nombre
        self.vida= vida
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.aguante = aguante

    def atributos(self):
        print(self.nombre, ':' , sep=" ")    
        print(".Vida:", self.vida)
        print(".Fuerza:", self.fuerza)
        print(".Inteligencia:", self.inteligencia)
        print(".Defensa:", self.defensa)
        print(".Aguante:", self.aguante)

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0  
        print(self.nombre, " has muerto")  
            
    def daño(self, enemigo):
        if enemigo.defensa > self.fuerza:
            return 0
        else:
            return self.fuerza - enemigo.defensa
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, " ha realizado", daño, " puntos")
        if enemigo.esta_vivo():
            print("la vida de", enemigo.nombre, " es ", enemigo.vida)
        else:
            enemigo.morir()