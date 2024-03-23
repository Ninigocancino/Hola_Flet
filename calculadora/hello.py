import flet as ft 

def main(page:ft.page):
    page.add(ft.Text(value="Hola mundo! Este es mi segundo hola en Flet"))

ft.app(target=main)