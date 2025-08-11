import flet as ft
import airtable as at
import main as menu_principal  # Para regresar al menú

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Consulta de Bioenergías"
    page.theme_mode = "light"
    page.window.width = 1000
    page.window.height = 600
    page.appbar = ft.AppBar(
        title=ft.Text("Consulta de bioenergías en la nube"),
        leading=ft.Icon("energy_savings_leaf"),
        center_title=True,
        bgcolor="green",
        color="white"
    )
    page.bgcolor = ft.Colors.WHITE

    # Encabezados de la tabla
    encabezado = [
        ft.DataColumn(ft.Text("Cultivo")),
        ft.DataColumn(ft.Text("Parte aprovechada")),
        ft.DataColumn(ft.Text("Cantidad (ton)")),
        ft.DataColumn(ft.Text("Área cultivada")),
        ft.DataColumn(ft.Text("Contenido energético")),
        ft.DataColumn(ft.Text("Municipio")),
        ft.DataColumn(ft.Text("Latitud")),
        ft.DataColumn(ft.Text("Longitud"))
    ]

    filas = []
    datos = at.Bioenergia.all()  # Obtiene todos los registros de bioenergía
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.cultivo))
        celda2 = ft.DataCell(ft.Text(d.parte))
        celda3 = ft.DataCell(ft.Text(str(d.cantidad)))
        celda4 = ft.DataCell(ft.Text(str(d.area)))
        celda5 = ft.DataCell(ft.Text(str(d.energia)))
        celda6 = ft.DataCell(ft.Text(d.municipio))
        celda7 = ft.DataCell(ft.Text(str(d.latitud)))
        celda8 = ft.DataCell(ft.Text(str(d.longitud)))

        fila = ft.DataRow([celda1, celda2, celda3, celda4, celda5, celda6, celda7, celda8])
        filas.append(fila)

    tbl_bioenergia = ft.DataTable(encabezado, filas)

    # Función para volver al menú
    def regresar_menu(e):
        page.clean()
        menu_principal.main(page)

    # Botón para regresar
    btn_regresar = ft.FilledButton(
        text="Regresar al menú",
        icon="arrow_back",
        bgcolor="green",
        on_click=regresar_menu
    )

    # Agregar tabla y botón a la página
    page.add(tbl_bioenergia, ft.Divider(), btn_regresar)
    page.update()

# Inicio de la aplicación
if __name__ == "__main__":
    ft.app(target=main)
