import flet as ft

def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Proyecto Integrador 01"
    page.bgcolor = "#FFF45"  # Fondo oscuro personalizado

    # Alineación global de la página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centrado vertical para los elementos
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Texto centrado verticalmente
    titulo = ft.Text(
        "Primer proyecto integrador: Creando un\ntexto con estilos básicos",
        color="white",
        size=32,
        weight="bold",
    )

    #Espaciado 1
    esp_1 = ft.Text(
        " ",
        size=8,
    )

    # Texto alineado a la derecha
    subtitulo = ft.Text(
        "Un ejercicio para practicar el manejo de texto y estilos \nen Flet",
        color="lightgray",
        size=23,
        weight="bold",
        italic=True
    )

    #Espaciado 2
    esp_2 = ft.Text(
        " ",
        size=12,
        )

    # Texto en la parte inferior de la ventana
    parrafo = ft.Text(
        "En esta unidad haz aprendido a manejar de forma general caracteristicas de texto\nadmás haz aprendido a darle estilos básicos como:\n\n 1) Cambiar el tamaño de la fuente\n 2) Modificar el color de la fuente\n 3) Dar a la fuente un formato de negritas",
        color="white",
        size=16,
    )



    # Agregar los textos en orden
    page.add(
        titulo,  
        esp_1,   # Texto alineado a la derecha (mantiene la alineación horizontal)
        subtitulo,  # Texto final que se ubica naturalmente en el flujo inferior
        esp_2,
        parrafo
    )

# Ejecutamos la aplicación
ft.app(target=main)
