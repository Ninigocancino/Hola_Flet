import flet as ft

def main(page: ft.Page):
    page.title = "Tamaño minimo de la ventana de previsualización"
    page.window_min_width = 300
    page.window_min_height = 300

    mensaje = ft.Text("Esta es mi primer ventana con tamaño minimo")

    page.add(mensaje)


ft.app(target=main)