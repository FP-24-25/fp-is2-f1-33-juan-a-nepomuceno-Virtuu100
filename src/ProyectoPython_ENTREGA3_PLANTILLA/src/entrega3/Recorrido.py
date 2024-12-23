'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from typing import Generic, TypeVar, Optional
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Grafo import Grafo
from abc import ABC, abstractmethod

V = TypeVar('V')
E = TypeVar('E')

class Recorrido(ABC,Generic[V,E]):
    
    def __init__(self,grafo:Grafo[V,E])->None:
        self._grafo: Grafo[V,E] = grafo
        self._tree: dict[V,tuple[Optional[V],float]] = {}
        self._path: list[V] = []     
           
    def path(self)->list[V]:
        return self._path
    
    def tree(self)->dict[V,tuple[Optional[V],float]]:
        return self._tree
    
    def path_to_origin(self,source:V)->list[V]:
        path: list[V] = []
        current: V = source
        while current is not None:
            path.append(current)
            predecessor, _ = self._tree.get(current, (None, 0))
            current = predecessor
        return list(reversed(path))
    
    def path_from_origin(self,source:V)->list[V]:
        ls:list[V] = []
        v:V = source
        ls.append(v)
        nxt:tuple[Optional[V],float] = self._tree[v]
        while nxt[0] is not None:
            v = nxt[0]
            ls.insert(0,v)
            nxt = self._tree[v]
        return ls 
    
    def path_weight(self,source:V)->float:
        return self._tree[source][1] 
    
    
    def origin(self,source:V)->V:
        path = self.path_to_origin(source)
        return path[0] if path else source
    
    def path_edges(self,source:V)->list[E]:
        path:list[V] = self.path_from_origin(source)
        ls:list[E] = []
        for i in range(len(path)-1):
            ls.append(self._grafo.edge(path[i], path[i+1]))
        return ls
    
    @abstractmethod
    def traverse(self,source:V)->None:
        # Recorrerá desde un vértice específico según un método de recorrido concreto
        pass
    
    def traverse_all(self)->None:
        # Realiza un recorridoo completo del grafo, visitando todos los vértices
        all_elements:set[V] = {v for v in self._grafo.vertex_set()}
        while len(all_elements) > 0:
            v:V = all_elements.pop()
            self.traverse(v)
            all_elements = all_elements - self._tree.keys()
            
    def groups(self)->dict[V,set[V]]:
        result: dict[V,set[V]] = {}
        for v in self._grafo.vertex_set():
            origin = self.origin(v)
            if origin not in result:
                result[origin] = set()
            result[origin].add(v)
        return result
    
    def groups_list(self)->list[set[V]]:
        return list(self.groups().values())
    
    def path_exist(self,source:V,target:V)->bool:
        return self.origin(source) == self.origin(target)

if __name__ == '__main__':
    pass