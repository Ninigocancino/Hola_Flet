import flet as ft

def main(page: ft.Page):
    page.tite="Filas en columnas"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.spacing=10

    texto_1 = ft.Text(value="Elemento 1, fila 1, col 1")
    texto_2 = ft.Text(value="Elemento 2, fila 1, col 1")
    texto_3 = ft.Text(value="Elemento 1, fila 2, col 1")
    texto_4 = ft.Text(value="Elemento 2, fila 2, col 1")
    texto_1b = ft.Text(value="Elemento 1, fila 1, col 2")
    texto_2b = ft.Text(value="Elemento 2, fila 1, col 2")
    texto_3b = ft.Text(value="Elemento 1, fila 2, col 2")
    texto_4b = ft.Text(value="Elemento 2, fila 2, col 2")


    fila_1 = ft.Row(
        controls=[
            texto_1,
            texto_2
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    fila_2 = ft.Row(
        controls=[
            texto_3,
            texto_4
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    #filas columna 2

    fila_1b = ft.Row(
        controls=[
            texto_1b,
            texto_2b
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    fila_2b = ft.Row(
        controls=[
            texto_3b,
            texto_4b
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )




    columna_1 = ft.Column(
        controls=[
            fila_1,
            fila_2
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=15
    )



    columna_2 = ft.Column(
        controls=[
            fila_1b,
            fila_2b
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=15
    )

    fila_principal = ft.Row(
        controls=[
            columna_1,
            columna_2
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        spacing=15

    )

    page.add(fila_principal)


ft.app(target=main)