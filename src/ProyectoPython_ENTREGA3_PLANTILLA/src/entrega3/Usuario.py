'''
Created on 17 nov 2024

@author: belen
'''

from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
import re


@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> 'Usuario':
        if not re.match(r'^\d{8}[A-Z]$', dni):
            raise ValueError("DNI inválido. Debe tener 8 dígitos seguidos de una letra mayúscula.")
        
        if fecha_nacimiento >= date.today():
            raise ValueError("La fecha de nacimiento debe ser anterior a la fecha actual.")
        
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)
    
    @staticmethod
    def parse(linea: str) -> 'Usuario':
        partes = linea.split(',')
        if len(partes) != 4:
            raise ValueError("Formato de línea inválido. Debe ser: DNI,Nombre,Apellidos,YYYY-MM-DD")
        
        dni, nombre, apellidos, fecha_str = partes
        fecha_nacimiento = date.fromisoformat(fecha_str)
        
        return Usuario.of(dni, nombre, apellidos, fecha_nacimiento)

    def __str__(self):
        return f"{self.dni} - {self.nombre}"
        

if __name__ == '__main__':
    linea:str = "45718832U,Carlos,Lopez,1984-01-14"
    usuario: Usuario = Usuario.parse(linea)
    print(usuario)