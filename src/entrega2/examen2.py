'''
Created on 21 nov 2024

@author: alvar
'''
from __future__ import annotations
from typing import TypeVar
from entrega2.tipos.Agregado_lineal import Agregado_lineal

E = TypeVar('E')

class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        self.capacidad = capacidad

    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    def is_full(self) -> bool:
        return len(self._elements) >= self.capacidad

    @staticmethod
    def of(capacidad: int) -> ColaConLimite[E]:
        return ColaConLimite(capacidad)

# Ejemplos
if __name__ == "__main__":
    cola: ColaConLimite[str] = ColaConLimite.of(3)
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")

    try:
        cola.add("Tarea 4")  
    except OverflowError as e:
        print(e) 

    print(cola.remove()) 

def test_cola_con_limite():
    # Prueba de creación y capacidad
    cola: ColaConLimite[str] = ColaConLimite.of(3)
    assert cola.capacidad == 3
    assert cola.size == 0
    assert cola.is_empty is True
    assert cola.is_full() is False

    # Prueba de add y is_full
    cola.add("Tarea 1")
    cola.add("Tarea 2")
    cola.add("Tarea 3")
    assert cola.size == 3
    assert cola.is_empty is False
    assert cola.is_full() is True

    # Prueba de OverflowError
    try:
        cola.add("Tarea 4")
        assert False, "Debería haber lanzado OverflowError"
    except OverflowError as e:
        assert str(e) == "La cola está llena."

    # Prueba de add_all
    cola = ColaConLimite.of(5)
    cola.add_all(["A", "B", "C"])
    assert cola.size == 3
    assert cola.elements == ["A", "B", "C"]

    # Prueba de remove_all
    removed = cola.remove_all()
    assert removed == ["A", "B", "C"]
    assert cola.is_empty is True

    # Prueba de elementos
    cola.add_all(["X", "Y", "Z"])
    assert cola.elements == ["X", "Y", "Z"]

def test_agregado_lineal_methods():
    agregado = ColaConLimite(5)
    
    # Prueba de add_all y size
    agregado.add_all(["A", "B", "C", "D", "E"])
    assert agregado.size == 5
    assert agregado.is_empty is False

    # Prueba de remove_all
    removed = agregado.remove_all()
    assert removed == ["A", "B", "C", "D", "E"]
    assert agregado.is_empty is True

    # Prueba de filter
    agregado.add_all([1, 2, 3, 4, 5])
    assert agregado.filter(lambda x: x % 2 == 0) == [2, 4]
    assert agregado.filter(lambda x: x > 3) == [4, 5]
    assert agregado.filter(lambda x: x < 0) == []

    # Prueba de find
    assert agregado.find(lambda x: x > 3) == 4
    assert agregado.find(lambda x: x % 2 == 0) == 2
    assert agregado.find(lambda x: x > 5) is None

if __name__ == "__main__":
    test_cola_con_limite()
    test_agregado_lineal_methods()
    print("Todas las pruebas pasaron exitosamente!")
