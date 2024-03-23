import flet as ft

from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    border_radius,
    colors
)

def main(page: ft.page):
    page.title = "Calculadora app"
    resultado = ft.Text(value="0", color=colors.WHITE,size=20) #Guarda el valor del resultado por default

    page.add(
        Container(
            width=350,
            bgcolor=colors.BLACK,
            border_radius= border_radius.all(15),
            padding=10,
            content=Column(
                controls=[
                    Row(controls=[resultado],alignment="end"),
                    Row(
                        controls=[
                            ElevatedButton(
                                text="AC",
                                bgcolor=colors.YELLOW,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="+/-",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="%",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="/",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand= 1,
                            ),
                        ]
                    ),


                    Row(
                        controls=[
                            ElevatedButton(
                                text="7",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="8",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="9",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="*",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand= 1,
                            ),
                        ]
                    ),


                    Row(
                        controls=[
                            ElevatedButton(
                                text="4",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="5",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="6",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="-",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand= 1,
                            ),
                        ]
                    ),


                    Row(
                        controls=[
                            ElevatedButton(
                                text="1",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="2",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="3",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="+",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand= 1,
                            ),
                        ]
                    ),


                    Row(
                        controls=[
                            ElevatedButton(
                                text="0",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text=".",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="=",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand=1,
                            ),
                            ElevatedButton(
                                text="",
                                bgcolor=colors.WHITE,
                                color=colors.BLACK,
                                expand= 1,
                            ),
                        ]
                    ),


                ]
            )
        )
    )

"""
        ft.Row(controls=[resultado]), #Muestra el resultado en pantlla
        ft.Row(
            controls =[
                ft.ElevatedButton(text="AC"), #Pinta un botón con el string 'AC'
                ft.ElevatedButton(text="+/-"),
                ft.ElevatedButton(text="%"),
                ft.ElevatedButton(text="/"),
            ]
        ),
        
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7"),
                ft.ElevatedButton(text="8"),
                ft.ElevatedButton(text="9"),
                ft.ElevatedButton(text="*"),
            ]
        ),

        ft.Row(
            controls=[
                ft.ElevatedButton(text="4"),
                ft.ElevatedButton(text="5"),
                ft.ElevatedButton(text="6"),
                ft.ElevatedButton(text="-"),
            ]
        ),

        ft.Row(
            controls=[
                ft.ElevatedButton(text="1"),
                ft.ElevatedButton(text="2"),
                ft.ElevatedButton(text="3"),
                ft.ElevatedButton(text="+"),             
            ]
        ),

        ft.Row(
            controls=[
                ft.ElevatedButton(text="0"),
                ft.ElevatedButton(text="."),
                ft.ElevatedButton(text="="),   
            ]
        ),
    )
"""

ft.app(target=main)