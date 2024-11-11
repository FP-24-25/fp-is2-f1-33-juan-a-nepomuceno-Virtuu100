'''
Created on 31 oct 2024

@author: alvar
'''
# entrega2/tipos/Pila.py
from __future__ import annotations
from typing import Generic, TypeVar
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')

class Pila(Agregado_lineal[E]):
    @staticmethod
    def of() -> Pila[E]:
        return Pila()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)

    def __str__(self):
        return f"Pila({self._elements})"