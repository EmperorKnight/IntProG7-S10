class Estudiante():
    def __init__(self, nombre, apellidos, carrera, cif):
        self.first_name = nombre
        self.last_name = apellidos
        self.major = carrera
        self.cif = cif
    
    def __str__(self):
        return f" \nCIF: {self.cif}\nNombre completo: {self.first_name} {self.last_name}\nCarrera{self.major}\n "