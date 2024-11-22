import flet as ft

def main(page: ft.Page):
    page.window_min_height =  820 #controla el alto minimo de la venta de previsualización
    page.window_min_width = 530 #controla el ancho minimo de la ventana de previsualización
    page.window_max_height = 1000
    page.window_max_width = 1500
    page.theme_mode = ft.ThemeMode.DARK
    page.add()

ft.app(target=main)