'''
Created on 17 nov 2024

@author: belen
'''

from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Red_social import Red_social
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Usuario import Usuario
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Relacion import Relacion
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Recorrido_en_anchura import Recorrido_en_anchura
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.E_grafo import Traverse_type
if __name__ == '__main__':
    rrss: Red_social = Red_social.parse("C:/Users/alvar/git/fp-is2-f1-33-juan-a-nepomuceno-Virtuu100/src/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/usuarios.txt", "C:/Users/alvar/git/fp-is2-f1-33-juan-a-nepomuceno-Virtuu100/src/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/relaciones.txt")
    r:Recorrido_en_anchura[Usuario,Relacion] = Recorrido_en_anchura.of(rrss)
    r._grafo._traverse_type = Traverse_type.FORWARD
    source:Usuario = rrss.usuarios_dni['25143909I']
    
    r.traverse(source)
    
    target: Usuario =  rrss.usuarios_dni['87345530M']
    
    camino = r.path_to_origin(target)
    # Mostrar el resultado
    if target in camino:
        print(f"El camino más corto desde {source.dni} hasta {target.dni} es: {camino}")
        print(f"La distancia mínima es: {r.path_weight(target)} pasos.")
    else:
        print(f"No hay conexión directa entre {source.dni} y {target.dni}.")
    

    
    

    
    