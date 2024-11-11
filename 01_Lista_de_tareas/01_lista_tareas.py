import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.title = "Lista de tareas"
    page.horizontal_alignment =ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(value="Mi lista de tareas",
                     size=30,
                     color=ft.colors.WHITE,
                     weight=ft.FontWeight.BOLD)
    
    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(title=ft.Text(campo_tarea.value),
                                leading=ft.Checkbox(on_change=seleccionar_tarea))
            tareas.append(tarea)
            campo_tarea.value = ""
            actualizar_lista()
            
    def seleccionar_tarea(e):
        seleccionadas = [i.title.value for i in tareas if i.leading.value]
        tareas_seleccionadas.value = "Tareas seleccionadas: " + ", ".join(seleccionadas)
        page.update()

    def actualizar_lista():
        lista_tareas.controls.clear()
        lista_tareas.controls.extend(tareas)
        page.update()
    
    campo_tarea = ft.TextField(hint_text="Agrega una nueva tarea", border_color=ft.colors.WHITE, color=ft.colors.WHITE)
    boton_agregar = ft.FilledButton(text="Agregar tarea", on_click=agregar_tarea)
    lista_tareas = ft.ListView(expand=0, spacing=4)
    
    tareas= []

    tareas_seleccionadas = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    page.add(titulo, campo_tarea,boton_agregar, lista_tareas, tareas_seleccionadas)


ft.app(target=main)