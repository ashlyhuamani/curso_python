#crear una clase de alumnos con los atributos que usted crear por
# conviniente luego instancia a 4 alumnos

    class Alumno:
    def __init__(self, nombre,edad,email,dni,programa_estudio="APSTI"):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.dni = dni
        self.programa_estudio=programa_estudio
    metodos
    def escribir(self):
        print("estoy escribiendo")
    def tarea(self):
        print("haciendo la tarea de:",nombre_docente)
    def terminar_tarea(self):
        print(terminando tarea anterior)

    maricielo=alumno("maricielo",75869321,14,"yo@gmail")
    maricielo.tarea("alicia")
    maricielo.terminar_tarea()
    maricielo.tarea("alvarez")


    maricielo=alumno("maricielo",75869321,14,"yo@gmail")
    print(maricielo.programa_estudio)
    mercedes=alumno("meche",56376454,15,"tu@gmail.com","enfermera")
    print(mercedes.programa_estudio)

