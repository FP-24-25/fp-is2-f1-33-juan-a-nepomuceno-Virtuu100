'''
Created on 19 dic 2024

@author: alvar
'''
from dataclasses import dataclass


@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> 'RelacionGenAGen':
        if not -1 <= conexion <= 1:
            raise ValueError("El valor de conexión debe estar entre -1 y 1, ambos inclusive.")
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(linea: str) -> 'RelacionGenAGen':
        partes = linea.strip().split(',')
        if len(partes) != 3:
            raise ValueError("Formato de línea inválido. Debe ser: NombreGen1,NombreGen2,Conexion")
        nombre_gen1, nombre_gen2, conexion_str = partes
        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, float(conexion_str))

    @property
    def coexpresados(self) -> bool:
        return self.conexion > 0.75

    @property
    def antiexpresados(self) -> bool:
        return self.conexion < -0.75

    def __str__(self):
        return f"RelacionGenAGen(nombre_gen1='{self.nombre_gen1}', nombre_gen2='{self.nombre_gen2}', conexion={self.conexion})"


if __name__ == '__main__':
    archivo_relaciones = "C:/Users/alvar/git/fp-is2-f1-33-juan-a-nepomuceno-Virtuu100/src/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/red_genes.txt"
    with open(archivo_relaciones, 'r') as f:
        print("Prueba de RelacionGenAGen:")
        for linea in f:
            relacion = RelacionGenAGen.parse(linea)
            print(relacion)
            print(f"Coexpresados: {relacion.coexpresados}, Antiexpresados: {relacion.antiexpresados}")
