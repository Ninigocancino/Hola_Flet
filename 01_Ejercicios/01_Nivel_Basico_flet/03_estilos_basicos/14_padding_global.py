import flet as ft 

def main(page: ft.Page):
    page.title = "Padding global"
    page.padding = 50

    texto = ft.Text("Texto con padding")

    page.add(texto)

ft.app(target=main)