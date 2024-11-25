import flet as ft

def main(page: ft.Page):
    page.title="Texto bold"
    
    linea = ft.Text("Este es un texto normal")
    linea_bold = ft.Text("Este es un texto en negritas", weight="bold")

    page.add(linea, linea_bold)


ft.app(target=main)