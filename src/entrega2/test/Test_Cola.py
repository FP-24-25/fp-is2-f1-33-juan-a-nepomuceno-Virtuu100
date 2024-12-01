'''
Created on 31 oct 2024

@author: alvar
'''

# entrega2/test/Test_Cola.py
from entrega2.tipos.Cola import Cola

def test_cola():
    print("TEST DE COLA:")
    print("\n################################################")
    print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
    cola = Cola.of()
    cola.add_all([23, 47, 1, 2, -3, 4, 5])
    print(f"Resultado de la cola: {cola}")

    print("\n################################################")
    print(f"Elementos eliminados utilizando remove_all: {cola.remove_all()}")

if __name__ == "__main__":
    test_cola()