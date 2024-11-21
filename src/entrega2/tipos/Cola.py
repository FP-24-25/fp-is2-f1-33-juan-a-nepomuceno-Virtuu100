'''
Created on 31 oct 2024

@author: alvar
'''
# entrega2/tipos/Cola.py
from __future__ import annotations
from typing import TypeVar
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')

class Cola(Agregado_lineal[E]):
    @staticmethod
    def of() -> Cola[E]:
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __str__(self):
        return f"Cola({self._elements})"