import flet as ft 

def main(page: ft.Page):

    page.title="Alinear texto al centro"

    linea = ft.Text("Este texto se alinea al centro")

    page.add(linea)

ft.app(target=main)