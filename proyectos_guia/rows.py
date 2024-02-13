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
            ft.TextField(label="Soy un campo de texto: Puedes agregar tu nombre"),
            ft.ElevatedButton(text="Soy un botón")
        ], alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.update()

ft.app(target=main)