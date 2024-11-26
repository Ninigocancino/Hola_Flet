import flet as ft

def main(page: ft.Page):
    page.title = "Texto inferior"

    page.vertical_alignment = ft.MainAxisAlignment.END

    texto = ft.Text("Este texto se colocará en la parte inferior")

    page.add(texto)


ft.app(target=main)