import os 
import flet as ft 

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] ="8000000"

def main(page: ft.Page):
    gv = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)

    for i in range(5000):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(1, ft.colors.AMBER_400),
                border_radius=ft.border_radius.all(5)
            )
        )
    page.update()

#ft.app(target=main, view=ft.AppView.WEB_BROWSER)
    
ft.app(target=main)