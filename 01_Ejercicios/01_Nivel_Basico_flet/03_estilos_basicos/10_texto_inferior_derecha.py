import flet as ft

def main(page: ft.Page):
    page.title= "Texto inferior derecha"
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.horizontal_alignment = ft.CrossAxisAlignment.END

    texto = ft.Text("Este texto se ubicará en la parte inferior derecha")

    page.add(texto)


ft.app(target=main)