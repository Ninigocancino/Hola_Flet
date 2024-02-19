import flet as ft

#Forma habitual con la que podríamos crear un formulario:

"""
def main(page):

    nombre = ft.TextField(label="Nombre", autofocus=True)
    apellido = ft.TextField(label="Apellido")
    saludo = ft.Column()

    def btn_click(e):
        saludo.controls.append(ft.Text(f"Hola, {nombre.value} {apellido.value}!"))
        nombre.value = ""
        apellido.value = ""
        page.update()
        nombre.focus()

    page.add(
        nombre,
        apellido,
        ft.ElevatedButton("Di hola!", on_click=btn_click),
        saludo,
    )
"""

#En esta forma reescribiremos el programa para usar referencias:
def main(page):

    nombre = ft.Ref[ft.TextField]()
    apellido = ft.Ref[ft.TextField]()
    saludo = ft.Ref[ft.Column]()

    def btn_click(e):
        saludo.current.controls.append(ft.Text(f"Hola, {nombre.value} {apellido.value}!"))
        nombre.value = ""
        apellido.value = ""
        page.update()
        nombre.focus()

    page.add(
        ft.TextField(ref=nombre, label="Nombre", autofocus=True),
        ft.TextField(ref=apellido,label="Apellido"),
        ft.ElevatedButton("Dí hola,hola", on_click=btn_click),
        ft.Column(ref=saludo),
    )

ft.app(target=main)