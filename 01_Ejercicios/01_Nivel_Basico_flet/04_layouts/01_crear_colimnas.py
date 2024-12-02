import flet as ft

def main(page: ft.Page):
    page.title = "Columna"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    columna = ft.Column(
        controls=[
            ft.Text("Elemto 1 de la columna"),
            ft.Text("Elemento 2 de la columna"),
            ft.Text("Elemento 3 de la columna")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    page.add(columna)


ft.app(target=main)