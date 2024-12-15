'''
Created on 17 nov 2024

@author: belen
'''
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Red_social import Red_social

if __name__ == '__main__':
    rrss: Red_social = Red_social.parse("C:/Users/alvar/git/fp-is2-f1-33-juan-a-nepomuceno-Virtuu100/src/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/usuarios.txt", "C:/Users/alvar/git/fp-is2-f1-33-juan-a-nepomuceno-Virtuu100/src/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/relaciones.txt")

    sep = '\n'
    print("************** Nº Predecesores de cada vértice")
    print(sep.join(f'{v} -- {len(rrss.predecessors(v))}'  for v in rrss.vertex_set()))

    print("\n************** Nº Vecinos de cada vértice")
    print(sep.join(f'{v} -- {len(rrss.neighbors(v))}'  for v in rrss.vertex_set()))
    