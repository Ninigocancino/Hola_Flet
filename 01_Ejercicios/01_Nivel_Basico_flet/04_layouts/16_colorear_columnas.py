import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Colorear columnas"
    page.spacing = 20  # Espaciado global entre elementos en la página

    # Crear la primera columna
    columna1 = ft.Container(
        content=ft.Column(
            controls=[
                #ft.Text("Columna 1: Elemento 1"),
                #ft.Text("Columna 1: Elemento 2"),
                #ft.Text(" ")
            ],
            alignment=ft.MainAxisAlignment.START,  # Alinear los elementos al inicio
            height=100,
            width=2000,
        ),
        bgcolor=ft.colors.BLUE,  # Fondo azul
        padding=0,  # Padding interno
        border_radius=0,  # Bordes redondeados
    )

    # Crear la segunda columna
    columna2 = ft.Container(
        content=ft.Column(
            controls=[
                #ft.Text("Columna 2: Elemento 1"),
                #ft.Text("Columna 2: Elemento 2"),
                #ft.Text("Columna 2: Elemento 3"),
                #ft.Text(" ")
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Centrar los elementos
            height=300,
            width=800,
        ),
        bgcolor=ft.colors.GREEN,  # Fondo verde
        padding=0,  # Padding interno
        border_radius=0,  # Bordes redondeados
    )
    
    """
    # Crear una fila que contenga ambas columnas
    fila = ft.Row(
        controls=[columna1, columna2],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,  # Espaciarlas uniformemente
    )
    """

    # Agregar la fila a la página
    page.add(columna1,columna2)

# Ejecutamos la aplicación
ft.app(target=main)
