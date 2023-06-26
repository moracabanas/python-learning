class Perro:
    def __init__(self, nombre, raza, edad=0):
        self.nombre = nombre + nombre
        self.raza = raza
        self.edad = edad

    def ladra(self):
        print(self.nombre, "dice 'Wooof!'")

    def saludar():
        print("Hola soy de la raza", self.raza)


perro1 = Perro("Rex", "Chihuahua")

perro1.saludar()  # TODO why Perro.saludar() takes 0 positional arguments but 1 was given
