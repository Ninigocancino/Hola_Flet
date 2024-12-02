import flet as ft

def main(page: ft.Page):
    page.title="Columna a la derecha"
    page.horizontal_alignment = ft.CrossAxisAlignment.END

    columna = ft.Column(
        controls=[
            ft.Text("Elemento 1 en lacolumna derecha"),
            ft.Text("Elemento 2 en la columna derecha"),
            ft.Text("Elemento 3 en la columna derecha")
        ]
    )

    page.add(columna)

ft.app(target=main)