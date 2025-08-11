import flet as ft
import airtable as at
import main as menu_principal  # Para regresar al menú

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Consultas"
    page.theme_mode = "light"
    page.window.width = 800
    page.window.height = 600
    page.appbar = ft.AppBar(
        title=ft.Text("Consulta de usuarios en la nube"),
        leading=ft.Icon("cloud"),
        center_title=True,
        bgcolor="green",
        color="white"
    )
    page.bgcolor = ft.Colors.WHITE

    # Tabla de usuarios
    encabezado = [
        ft.DataColumn(ft.Text("Clave")),
        ft.DataColumn(ft.Text("Contraseña")),
        ft.DataColumn(ft.Text("Nombre completo")),
        ft.DataColumn(ft.Text("Es administrador")),
    ]
    filas = []
    datos = at.Usuario.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.clave))
        celda2 = ft.DataCell(ft.Text(d.contra, color="white", selectable=True))
        celda3 = ft.DataCell(ft.Text(d.nombre))
        celda4 = ft.DataCell(ft.Checkbox(value=d.admin, disabled=True))
        fila = ft.DataRow([celda1, celda2, celda3, celda4])
        filas.append(fila)
    tbl_usuarios = ft.DataTable(encabezado, filas)

    # Función para regresar al menú
    def regresar_menu(e):
        page.clean()
        menu_principal.main(page)

    btn_regresar = ft.FilledButton(
        text="Regresar al menú",
        icon="arrow_back",
        bgcolor="blue",
        on_click=regresar_menu
    )

    # Añadir tabla y botón
    page.add(tbl_usuarios, ft.Divider(), btn_regresar)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
