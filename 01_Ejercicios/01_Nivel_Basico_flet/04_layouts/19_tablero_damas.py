import flet as ft

def main(page: ft.Page):
    page.title="Tablero de damas"
    page.spacing=0

    fila_1 = ft.Row(
        controls=[

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200
                ),
                bgcolor=ft.colors.BLACK45
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200,
                ),
                bgcolor=ft.colors.GREY_300,
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200
                ),
                bgcolor=ft.colors.BLACK45
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200,
                ),
                bgcolor=ft.colors.GREY_300,
            ),
        ],
        spacing=0
    )

    fila_2 = ft.Row(
        controls=[

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200
                ),
                bgcolor=ft.colors.GREY_300
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200,
                ),
                bgcolor=ft.colors.BLACK45,
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200
                ),
                bgcolor=ft.colors.GREY_300
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200,
                ),
                bgcolor=ft.colors.BLACK45,
            ),
        ],
        spacing=0
    )

    fila_3 = ft.Row(
        controls=[

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200
                ),
                bgcolor=ft.colors.BLACK45
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200,
                ),
                bgcolor=ft.colors.GREY_300,
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200
                ),
                bgcolor=ft.colors.BLACK45
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200,
                ),
                bgcolor=ft.colors.GREY_300,
            ),
        ],
        spacing=0
    )


    fila_4 = ft.Row(
        controls=[

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200
                ),
                bgcolor=ft.colors.GREY_300
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200,
                ),
                bgcolor=ft.colors.BLACK45,
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200
                ),
                bgcolor=ft.colors.GREY_300
            ),

            ft.Container(
                content=ft.Column(
                    controls=[],
                    width=200,
                    height=200,
                ),
                bgcolor=ft.colors.BLACK45,
            ),
        ],
        spacing=0
    )

    page.add(fila_1,fila_2,fila_3,fila_4)


ft.app(target=main)