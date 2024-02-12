import flet as ft 

def main(page: ft.page):

    #t = ft.Text(value="Filas", color="Blue")

    page.add(
        ft.Row(controls=[
            ft.Text("Soy la fila "),
            ft.Text("Soy la fila "),
            ft.Text("Soy la fila ")
        ], alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.update()

    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ], alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.update()

ft.app(target=main)