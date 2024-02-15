import flet as ft

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

ft.app(target=main)