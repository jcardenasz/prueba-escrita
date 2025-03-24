import random

class Peticion:
    def __init__(self, avance, PAPA, PBM):
        self.avance = avance
        self.PAPA = PAPA
        self.PBM = PBM
        self.calificacion = 0

    def calcularCalificacion(self):
        peso_papa = 0.5
        peso_pbm = 0.5
        pbm_normalizado = 100 - self.PBM 
        self.calificacion = ((self.PAPA *20)* peso_papa) + (pbm_normalizado * peso_pbm)

def clasificarOrdenar(peticiones):
    listaA = []
    listaB = []

    for p in peticiones:
        p.calcularCalificacion()  
        if p.avance >= 80:
            listaA.append(p)
        else:
            listaB.append(p)

    listaA.sort(key=lambda x: x.calificacion, reverse=True)
    listaB.sort(key=lambda x: x.calificacion, reverse=True)

    return listaA, listaB

peticiones = [
    Peticion(
        random.randint(1, 100), 
        round(random.uniform(3.0, 5.0), 2),  
        random.randint(0, 100)
    ) for _ in range(100)
]

listaA, listaB = clasificarOrdenar(peticiones)

print("Grupo A (avance >= 80%):")
for p in listaA:
    print(f"Avance: {p.avance}, PAPA: {p.PAPA}, PBM: {p.PBM}, Calificación: {p.calificacion:.2f}")

print("\nGrupo B (avance < 80%):")
for p in listaB:
    print(f"Avance: {p.avance}, PAPA: {p.PAPA}, PBM: {p.PBM}, Calificación: {p.calificacion:.2f}")
