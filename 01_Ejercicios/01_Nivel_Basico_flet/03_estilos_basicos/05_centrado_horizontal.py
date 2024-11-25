import flet as ft 

def main(page: ft.Page):

    page.title="Alinear texto al centro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    texto_centrado = ft.Text("Este texto se alinea al centro")

    page.add(texto_centrado)

ft.app(target=main)