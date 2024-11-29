import flet as ft

def main(page: ft.Page):
    page.title ="Color de fondo"
    page.bgcolor = ft.colors.GREY_600

    texto = ft.Text("El color de fondo será gris")

    page.add(texto)

ft.app(target=main)