'''
Created on 17 nov 2024

@author: belen
'''
from __future__ import annotations
from dataclasses import dataclass



@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int

    __xx_num: int = 0
    @staticmethod
    def of(interacciones: int, dias_activa: int) -> 'Relacion':
        Relacion.__xx_num += 1  # Increment the unique identifier
        return Relacion(Relacion.__xx_num, interacciones, dias_activa)

    def __str__(self):
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones})"
if __name__ == '__main__':
    relacion = Relacion.of(10, 5)
    print(relacion)