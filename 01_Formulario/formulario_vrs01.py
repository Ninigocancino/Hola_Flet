import flet as ft

def main(page: ft.page):
    page.title = "Formulario de registro - Versión 01"
    project_name = ft.Text("Formulario de registro", size=30, weight= "bold", color="blue")
    
    page.add(project_name)


ft.app(target=main)