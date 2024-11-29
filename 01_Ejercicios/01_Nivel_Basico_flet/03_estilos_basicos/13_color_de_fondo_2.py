import flet as ft

def main(page: ft.Page):
    page.title = "Color de fondo opción 2"
    page.bgcolor = '#FF5733'

    texto = ft.Text("El color de fondo será un valor exadecimal: #FF5733")

    page.add(texto)

ft.app(target=main)