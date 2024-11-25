import flet as ft 

def main(page: ft.Page):
    page.title="Alinear texto a la derecha"
    
    page.horizontal_alignment = ft.CrossAxisAlignment.END

    texto = ft.Text("Este texto se alineará a la derecha")

    page.add(texto)


ft.app(target=main)