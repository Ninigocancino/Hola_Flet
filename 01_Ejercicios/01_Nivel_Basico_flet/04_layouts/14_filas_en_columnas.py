import flet as ft

def main(page: ft.Page):
    page.tite="Filas en columnas"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.spacing=10

    texto_1 = ft.Text(value="Elemento 1, fila 1")
    texto_2 = ft.Text(value="Elemento 2, fila 1")
    texto_3 = ft.Text(value="Elemento 1, fila 2")
    texto_4 = ft.Text(value="Elemento 2, fila 2")

    fila_1 = ft.Row(
        controls=[
            texto_1,
            texto_2
        ],
        alignment=ft.MainAxisAlignment.CENTER  
    )

    fila_2 = ft.Row(
        controls=[
            texto_3,
            texto_4
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND 
    )

    columna_1 = ft.Column(
        controls=[
            fila_1,
            fila_2
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15
    )

    page.add(columna_1)


ft.app(target=main)