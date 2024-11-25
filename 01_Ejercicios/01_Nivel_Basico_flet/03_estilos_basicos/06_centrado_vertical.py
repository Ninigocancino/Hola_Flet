import flet as ft

def main(page: ft.Page):

    page.title="Texto centrado verticalmente"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    texto_centrado = ft.Text("Este texto se centrará verticalmente")

    page.add(texto_centrado)


ft.app(target=main)