import flet as ft

def main(page: ft.Page):
    page.title="Fila"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.spacing=100

    texto_1 =ft.Text(value="elemento 1 fila 1")
    texto_2 =ft.Text(value="elemento 2 fila 1")
    texto_3 =ft.Text(value="elemento 1 fila 2")
    texto_4 =ft.Text(value="elemento 2 fila 2")

    fila = ft.Row(
        controls=[
            texto_1,
            texto_2,
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        spacing=2,
    )

    fila_2 = ft.Row(
        controls=[
            texto_3,
            texto_4,
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        spacing=1,
    )

    page.add(fila,fila_2)

ft.app(target=main)