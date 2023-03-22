class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    def resultado(self):
        if self.nota < 5:
            print("El alumno ha reporbado")
        else:
            print("El alumno ha aprobado")


alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializar("Maria", 10)
alumno2.inicializar("Juan", 2)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()
