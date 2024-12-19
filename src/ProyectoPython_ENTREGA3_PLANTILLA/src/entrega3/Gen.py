'''
Created on 19 dic 2024

@author: alvar
'''
from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> 'Gen':
        if not nombre or not tipo or not loc_cromosoma:
            raise ValueError("Nombre, tipo y localización del cromosoma no pueden estar vacíos.")
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual que cero.")
        if not re.match(r'^\d+[pq]\d+(\.\d+)?$', loc_cromosoma):
            raise ValueError("Formato de localización del cromosoma inválido. Debe ser como '17p13.1'.")
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)

    @staticmethod
    def parse(linea: str) -> 'Gen':
        partes = linea.strip().split(',')
        if len(partes) != 4:
            raise ValueError("Formato de línea inválido. Debe ser: Nombre,Tipo,NumMutaciones,LocCromosoma")
        nombre, tipo, num_mutaciones_str, loc_cromosoma = partes
        return Gen.of(nombre, tipo, int(num_mutaciones_str), loc_cromosoma)

    def __str__(self):
        return f"{self.nombre}: ({self.tipo},{self.num_mutaciones},{self.loc_cromosoma})"
    
if __name__ == '__main__':
    archivo_genes = "C:/Users/alvar/git/fp-is2-f1-33-juan-a-nepomuceno-Virtuu100/src/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/genes.txt"
    with open(archivo_genes, 'r') as f:
        primera_linea = f.readline().strip()
        gen = Gen.parse(primera_linea)
        print(gen)