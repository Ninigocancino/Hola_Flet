import flet as ft 

def main(page: ft.Page):

    def button_clicked(e):
        page.add(ft.Text("Haz click"))

    page.add(ft.ElevatedButton(text="Pulsa", on_click=button_clicked))

ft.app(target=main)