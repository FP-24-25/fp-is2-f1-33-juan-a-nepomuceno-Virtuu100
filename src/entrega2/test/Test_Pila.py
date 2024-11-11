'''
Created on 31 oct 2024

@author: alvar
'''

# entrega2/test/Test_Pila.py
from entrega2.tipos.Pila import Pila

def test_pila():
    print("TEST DE PILA:")
    print("\n################################################")
    print("Creación de una pila vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
    pila = Pila.of()
    pila.add_all([23, 47, 1, 2, -3, 4, 5])
    print(f"Resultado de la pila: {pila}")

    print("\n################################################")
    print(f"Elementos eliminados utilizando remove_all: {pila.remove_all()}")

if __name__ == "__main__":
    test_pila()