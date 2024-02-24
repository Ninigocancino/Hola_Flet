import flet as ft 

def main(page: ft.page):
    lv = ft.ListView(expand=True, spacing=10)
    for i in range(5000):
        lv.controls.append(ft.Text(f"Lines {i}"))
    page.add(lv)

#ft.app(target=main, view=ft.AppView.WEB_BROWSER)

ft.app(target=main)