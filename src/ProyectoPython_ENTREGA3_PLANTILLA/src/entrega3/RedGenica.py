'''
Created on 19 dic 2024

@author: alvar
'''
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Gen import Gen
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.RelacionGenAGen import RelacionGenAGen


class RedGenica:
    def __init__(self, genes: list[Gen], relaciones: list[RelacionGenAGen]):
        self.genes = genes
        self.relaciones = relaciones
        self.genes_por_nombre = {gen.nombre: gen for gen in genes}

    @staticmethod
    def parse(archivo_genes: str, archivo_relaciones: str) -> 'RedGenica':
        with open(archivo_genes, 'r') as f_genes:
            genes = [Gen.parse(linea) for linea in f_genes]
        with open(archivo_relaciones, 'r') as f_relaciones:
            relaciones = [RelacionGenAGen.parse(linea) for linea in f_relaciones]
        return RedGenica(genes, relaciones)

    def __str__(self):
        vertices = "\n".join(str(gen) for gen in self.genes)
        aristas = "\n".join(str(relacion) for relacion in self.relaciones)
        return f"Vertices:\n{vertices}\n\nAristas:\n{aristas}"


if __name__ == '__main__':
    # Pruebas rápidas
    try:
        archivo_genes = "C:/Users/alvar/git/fp-is2-f1-33-juan-a-nepomuceno-Virtuu100/src/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/genes.txt"
        archivo_relaciones = "C:/Users/alvar/git/fp-is2-f1-33-juan-a-nepomuceno-Virtuu100/src/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/red_genes.txt"

        red_genica = RedGenica.parse(archivo_genes, archivo_relaciones)
        print("Prueba de RedGenica:")
        print(red_genica)
    except FileNotFoundError as e:
        print(f"No se encontró el archivo: {e}")
    except Exception as e:
        print(f"Error durante la prueba: {e}")

