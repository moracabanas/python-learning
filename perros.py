class Perro():

  def __init__(self, nombre, raza, edad):
    self.nombre = nombre
    self.raza = raza
    self.edad = edad
  def ladra(self):
    print(self.nombre, "dice 'Wooof!'")
    
perro1 = Perro("Rex", "Chihuahua", 2)

perro1.ladra()