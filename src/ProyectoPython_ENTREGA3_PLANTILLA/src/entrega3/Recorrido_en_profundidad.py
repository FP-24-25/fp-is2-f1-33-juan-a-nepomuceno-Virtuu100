'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from typing import TypeVar
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Recorrido import Recorrido
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Grafo import Grafo
from entrega2.tipos.Pila import Pila

V = TypeVar('V')
E = TypeVar('E')


class Recorrido_en_profundidad(Recorrido[V,E]):
    
    @staticmethod
    def of(grafo:Grafo[V,E])->Recorrido_en_profundidad[V,E]:
        return Recorrido_en_profundidad(grafo)
    
    def __init__(self,grafo:Grafo[V,E])->None:
        super().__init__(grafo)
            
    def traverse(self,source:V)->None:
        self._tree = {source: (None, 0)}
        self._path = []
        stack = Pila()
        stack.add(source)
        
        while not stack.is_empty:
            v = stack.remove()
            if v not in self._path:
                self._path.append(v)
                for neighbor in reversed(list(self._grafo.successors(v))):
                    if neighbor not in self._tree:
                        weight = self._grafo.edge_weight(v, neighbor)
                        self._tree[neighbor] = (v, self._tree[v][1] + weight)
                        stack.add(neighbor)
if __name__ == '__main__':
    pass