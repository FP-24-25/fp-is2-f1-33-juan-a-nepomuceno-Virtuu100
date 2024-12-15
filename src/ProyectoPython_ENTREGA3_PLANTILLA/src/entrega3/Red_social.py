'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.E_grafo import E_grafo, Graph_type, Traverse_type
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Usuario import Usuario
from ProyectoPython_ENTREGA3_PLANTILLA.src.entrega3.Relacion import Relacion
from ProyectoPython_ENTREGA3_PLANTILLA.src.resources.File import lineas_de_fichero, absolute_path

# Esta clase se debe ejecutar (ver el main abajo del todo)

class Red_social(E_grafo[Usuario, Relacion]):
    
    def __init__(self,graph_type:Graph_type,traverse_type:Traverse_type)->None:
        super().__init__(graph_type, lambda r: r.interacciones, traverse_type)
        self.__usuarios_dni:dict[str,Usuario] = {}
        
    
    @staticmethod
    def of(graph_type, traverse_type) -> Red_social: # TODO: Hay que añadir los parámetros de entrada
        return Red_social(Graph_type, Traverse_type)#he cambiado de minuscula a mayuscula porque si no daba error
    
    @staticmethod
    def parse(f1:str, f2:str, graph_type:Graph_type = Graph_type.UNDIRECTED, traverse_type: Traverse_type = Traverse_type.BACK) -> Red_social:
        red = Red_social.of(graph_type, traverse_type)
        
        # Parse usuarios file
        for linea in lineas_de_fichero(absolute_path(f1)):
            usuario = Usuario.parse(linea)
            red.add_vertex(usuario)
            red.__usuarios_dni[usuario.dni] = usuario
        
        # Parse relaciones file
        for linea in lineas_de_fichero(absolute_path(f2)):
            partes = linea.strip().split(',')
            if len(partes) != 4:
                raise ValueError(f"Formato inválido en línea de relaciones: {linea}")
            
            dni1, dni2, interacciones, dias_activa = partes
            usuario1 = red.__usuarios_dni[dni1]
            usuario2 = red.__usuarios_dni[dni2]
            relacion = Relacion.of(int(interacciones), int(dias_activa))
    
            red.add_edge(usuario1, usuario2, relacion)
        
        return red
    @property
    def usuarios_dni(self)->dict[str,Usuario]:
        return self.__usuarios_dni

        

if __name__ == '__main__':
    rrss: Red_social = Red_social.parse("C:/Users/alvar/git/fp-is2-f1-33-juan-a-nepomuceno-Virtuu100/src/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/usuarios.txt", "C:/Users/alvar/git/fp-is2-f1-33-juan-a-nepomuceno-Virtuu100/src/ProyectoPython_ENTREGA3_PLANTILLA/src/resources/relaciones.txt")
    print(rrss.plot_graph())