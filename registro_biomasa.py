import flet as ft
import airtable as at  # Para guardar en la nube
import main as menu_principal  # Para volver al menú

def main(page: ft.Page):
    page.title = "Registro de bioenergías de Tabasco"
    page.window_width = 1000
    page.window_height = 850
    page.scroll = ft.ScrollMode.ALWAYS
    page.horizontal_alignment = "center"
    page.bgcolor = "#E8FFD7"

    page.fonts = {"Poppins": "Poppins"}
    page.theme = ft.Theme(font_family="Poppins")

    # Encabezado
    encabezado = ft.Stack(
        controls=[
            ft.Image(
                src="https://images.pexels.com/photos/1871030/pexels-photo-1871030.jpeg",
                width=1500,
                height=200,
                fit=ft.ImageFit.COVER
            ),
            ft.Container(
                content=ft.Column([
                    ft.Text("Biomasa", size=30, weight="bold", color="white", text_align="center")
                ], alignment="center", horizontal_alignment="center"),
                width=1500,
                height=200,
                padding=20
            )
        ],
        width=1500,
        height=200
    )

    # Campos del formulario
    lista_cultivo = ft.Dropdown(
        hint_text="Seleccionar cultivo origen",
        options=[ft.dropdown.Option(c) for c in ["Caña de azúcar", "Cacao", "Maíz", "Coco", "Plátano"]],
        width=400
    )

    lista_parte = ft.Dropdown(
        hint_text="Seleccionar parte aprovechada",
        options=[ft.dropdown.Option(p) for p in ["Hoja", "Tallo", "Cáscara", "Bagazo", "Rastrojo"]],
        width=400
    )

    txt_cantidad = ft.TextField(label="Cantidad (ton)", width=400)
    txt_area = ft.TextField(label="Área cultivada", width=400)
    txt_humedad = ft.TextField(label="% Humedad", width=400)
    txt_energia = ft.TextField(label="Contenido energético", width=400)

    lista_municipio = ft.Dropdown(
        hint_text="Seleccionar municipio",
        options=[ft.dropdown.Option(m) for m in ["Balancán", "Cárdenas", "Centla", "Centro", "Comalcalco"]],
        width=400
    )

    txt_latitud = ft.TextField(label="Latitud", width=400)
    txt_longitud = ft.TextField(label="Longitud", width=400)

    # Función para guardar en Airtable
    def guardar_bioenergia(e):
        try:
            nuevo = at.Bioenergia(
                cultivo=lista_cultivo.value,
                parte=lista_parte.value,
                cantidad=float(txt_cantidad.value),
                area=float(txt_area.value),
                energia=float(txt_energia.value),
                municipio=lista_municipio.value,
                latitud=float(txt_latitud.value),
                longitud=float(txt_longitud.value)
            )
            nuevo.save()
            page.open(ft.SnackBar(ft.Text("Registro guardado correctamente"), bgcolor="green", show_close_icon=True))
        except Exception as error:
            page.open(ft.SnackBar(ft.Text(f"Error: {error}"), bgcolor="red", show_close_icon=True))

    # Función para cancelar → limpia los campos
    def cancelar(e):
        lista_cultivo.value = None
        lista_parte.value = None
        txt_cantidad.value = ""
        txt_area.value = ""
        txt_humedad.value = ""
        txt_energia.value = ""
        lista_municipio.value = None
        txt_latitud.value = ""
        txt_longitud.value = ""
        page.update()

    # Función para regresar al menú
    def regresar_menu(e):
        page.clean()
        menu_principal.main(page)

    # Botones
    btn_guardar = ft.FilledButton(text="Guardar", icon="save", bgcolor="green", on_click=guardar_bioenergia)
    btn_cancelar = ft.FilledButton(text="Cancelar", icon="cancel", bgcolor="red", on_click=cancelar)
    btn_regresar = ft.FilledButton(text="Regresar al menú", icon="arrow_back", bgcolor="blue", on_click=regresar_menu)

    fila_botones = ft.Row([btn_guardar, btn_cancelar, btn_regresar], alignment="center")

    # Agregar a la página
    page.add(
        encabezado,
        ft.Text("Cultivo origen", size=20, weight="bold"),
        lista_cultivo,
        ft.Text("Parte aprovechada", size=20, weight="bold"),
        lista_parte,
        txt_cantidad,
        txt_area,
        txt_humedad,
        txt_energia,
        ft.Text("Municipio", size=20, weight="bold"),
        lista_municipio,
        ft.Text("Coordenadas", size=16),
        txt_latitud,
        txt_longitud,
        fila_botones
    )

if __name__ == "__main__":
    ft.app(target=main)
