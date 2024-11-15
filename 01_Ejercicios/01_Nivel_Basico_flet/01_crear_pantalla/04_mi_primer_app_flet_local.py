import flet as ft
  
def main(page: ft.Page):
    page.title = "Mi primer app flet en navegador"

    page.add()

ft.app(target=main, view=ft.WEB_BROWSER)