import flet as ft

def main(page: ft.Page):
    page.title = "Texto en formato cursiva"

    cursiva = ft.Text("Este es un texto en curiva", italic=True)

    page.add(cursiva)

ft.app(target=main)