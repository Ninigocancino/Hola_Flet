import flet as ft 

def main(page: ft.Page):

    page.title="Columnas centradas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    columna = ft.Column(
        controls=[
            ft.Text("Elemento uno de la columna centro"),
            ft.Text("Elemento 2 de la columna centro"),
            ft.Text("Elemento 3 de la columna centro")
        ]
    )

    page.add(columna)


ft.app(target=main)