import flet as ft 

def main(page: ft.Page):
    page.title = "Mi primer app con texto"
    texto = ft.Text("Encabezado 01 creado en Flet")

    page.add(texto)

ft.app(target=main)