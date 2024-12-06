import flet as ft 


def main(page: ft.Page):
    page.title="Columnas vecinas"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.END

    fila = ft.Row(
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[],
                    height=100,
                    width=300,
                ),
                bgcolor=ft.colors.BLUE_300,
                border_radius=40,
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    height=100,
                    width=300,
                ),
                bgcolor=ft.colors.GREEN_100,
                border_radius=40,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(fila)

ft.app(target=main)