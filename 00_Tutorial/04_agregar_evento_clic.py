import flet as ft 

def main(page: ft.Page):
    page.bgcolor = ft.colors.GREY_200
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Mi app con flet"
    texto = ft.Text("Esta es mi primera app con Python y Flet")
    texto2 = ft.Text("Estoy construyendo mi primera app con python y flet")

    def cambiar_texto(e):
        texto2.value = "Ahora tenemos un botón que ejecuta un evento clic"
        page.update()

    boton = ft.FilledButton(text="Cambiar texto", on_click=cambiar_texto)

    page.add(texto,texto2,boton)

ft.app(target=main)