import flet as ft

def main(page: ft.Page):
    page.title="Fila"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    texto_1 =ft.Text(value="elemento 1")
    texto_2 =ft.Text(value="elemento 2")

    fila = ft.Row(
        controls=[
            texto_1,
            texto_2,
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        spacing=20,
    )

    page.add(fila)

ft.app(target=main)