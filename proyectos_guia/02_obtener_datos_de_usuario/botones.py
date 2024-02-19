import flet as ft 

def main(page: ft.page):

    btn = ft.ElevatedButton("Haz click")
    page.add(btn)

ft.app(target=main)   