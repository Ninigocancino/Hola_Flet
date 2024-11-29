import flet as ft

def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Proyecto Integrador"
    page.bgcolor = "#FFF45"  # Fondo oscuro personalizado

    # Alineación global de la página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centrado vertical para los elementos
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Texto centrado verticalmente
    titulo = ft.Text(
        "Texto h1",
        color="white",
        size=32,
        weight="bold",
    )

    #Espaciado 1
    esp_1 = ft.Text(
        " ",
        size=24,
    )

    # Texto alineado a la derecha
    subtitulo = ft.Text(
        "Texto h2",
        color="lightgray",
        size=23,
        weight="bold",
        italic=True
    )

    # Texto en la parte inferior de la ventana
    parrafo = ft.Text(
        "Texto en la parte inferior de la ventana",
        color="white",
        size=16,
    )


    # Agregar los textos en orden
    page.add(
        titulo,  
        esp_1,   # Texto alineado a la derecha (mantiene la alineación horizontal)
        subtitulo,  # Texto final que se ubica naturalmente en el flujo inferior
        parrafo
    )

# Ejecutamos la aplicación
ft.app(target=main)
