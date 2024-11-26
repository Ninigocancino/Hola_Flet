import flet as ft 

def main(page: ft.Page):
    page.title="Texto centro-derecha"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.END

    texto = ft.Text("Este texto se ubicará al centro y a la derecha")

    page.add(texto)


ft.app(target=main)