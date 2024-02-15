import flet as ft 

# Disabled es una propieda que permite crear margenes en elementos de entrada de datos, su valor por defecto es False, por lo que pinta por default en margen del elemento, si se pasa el valor explicito de True solo lo sobreará

def main(page: ft.Page):

    nombre = ft.TextField()
    apellido = ft.TextField()
    nombre.disabled = False
    apellido.disabled = False
    page.add(nombre,apellido)

ft.app(target=main)