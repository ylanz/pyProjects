class Persona():
    nombre = ""
    apellido = ""
    nrocedula = 0
    sueldo = 0

    def __init__(self, pnombre, ppellido, psueldo = 0.0):
        self.nombre = pnombre
        self.sueldo = psueldo

    def datosPersona(self):
        print("Yo me llamo: ", self.nombre)
    
    def sueldoAnual(self):
        print("Sueldo Anual: ", self.sueldo * 12)

