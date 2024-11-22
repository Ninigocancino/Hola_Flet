import flet as ft

def main(page: ft.Page):
    page.title = "Ventana con un tamaño maximo de pantalla"
    page.window_max_width = 600
    page.window_max_height = 600

    mensaje = ft.Text("Esta es una ventana con un tamaño maximo de pantalla")

    page.add(mensaje)

ft.app(target=main)