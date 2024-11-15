'''
Created on 31 oct 2024

@author: alvar
'''
# entrega2/tipos/Lista_ordenada_sin_repeticion.py
from __future__ import annotations
from typing import Generic, TypeVar, Callable
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada_sin_repeticion(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self.__order = order

    @staticmethod
    def of(order: Callable[[E], R]) -> Lista_ordenada_sin_repeticion[E, R]:
        return Lista_ordenada_sin_repeticion(order)

    def __index_order(self, e: E) -> int:
        for i, elem in enumerate(self._elements):
            if self.__order(e) < self.__order(elem):
                return i
        return len(self._elements)

    def add(self, e: E) -> None:
        if e not in self._elements:
            index = self.__index_order(e)
            self._elements.insert(index, e)

    def __str__(self):
        return f"ListaOrdenadaSinRepeticion({self._elements})"