import flet as ft 

# Disabled es una propieda que permite crear margenes en elementos de entrada de datos, su valor por defecto es False, por lo que pinta por default en margen del elemento, si se pasa el valor explicito de True solo lo sobreará

def main(page: ft.Page):
    
    # Esta es una forma de agregar la propiedad disabled a un elemento, en este caso se agrega la propiedad elemento por elemento
    """"
    nombre = ft.TextField()
    apellido = ft.TextField()
    nombre.disabled = False
    apellido.disabled = False
    page.add(nombre,apellido)
    """

    # Esta forma permite agregar la propiedad disabled a un grupo de elementos
    nombre = ft.TextField()
    apellido = ft.TextField()
    columna = ft.Column(controls=[
        nombre,
        apellido
    ])
    columna.disabled = False
    page.add(columna)


ft.app(target=main)