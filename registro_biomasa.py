import flet as ft
#import principal as pr

def main(page: ft.Page):
    page.title = "Registro de bioenergías de Tabasco"
    page.window_width = 1000  # Aumentar ancho de ventana
    page.window_height = 850
    page.scroll = ft.ScrollMode.ALWAYS
    page.horizontal_alignment = "center"
    page.bgcolor = "#E4DEBE"

    # Fuente global
    page.fonts = {"Poppins": "Poppins"}
    page.theme = ft.Theme(font_family="Poppins")

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

    # Títulos y campos
    titulo_cultivo = ft.Text("Cultivo origen", size=20, weight="bold")
    lista_cultivo = ft.Dropdown(
        hint_text="Seleccionar cultivo origen",
        options=[ft.dropdown.Option(c) for c in ["Caña de azúcar", "Cacao", "Maíz", "Coco", "Plátano"]],
        width=400
    )

    titulo_parte = ft.Text("Parte aprovechada", size=20, weight="bold")
    lista_parte = ft.Dropdown(
        hint_text="Seleccionar parte aprovechada",
        options=[ft.dropdown.Option(p) for p in ["Hoja", "Tallo", "Cáscara", "Bagazo", "Rastrojo"]],
        width=400
    )

    txt_cantidad = ft.TextField(label="Cantidad (ton)", width=400)
    txt_area = ft.TextField(label="Área cultivada", width=400)
    txt_humedad = ft.TextField(label="% Humedad", width=400)
    txt_energia = ft.TextField(label="Contenido energético", width=400)

    titulo_municipio = ft.Text("Municipio", size=20, weight="bold")
    lista_municipio = ft.Dropdown(
        hint_text="Seleccionar municipio",
        options=[ft.dropdown.Option(m) for m in ["Balancán", "Cárdenas", "Centla", "Centro", "Comalcalco"]],
        width=400
    )

    titulo_coord = ft.Text("Coordenadas", size=16)
    txt_latitud = ft.TextField(label="Latitud", width=400)
    txt_longitud = ft.TextField(label="Longitud", width=400)

    # Agregar todo a la interfaz
    page.add(
        encabezado,
        titulo_cultivo,
        lista_cultivo,
        titulo_parte,
        lista_parte,
        txt_cantidad,
        txt_area,
        txt_humedad,
        txt_energia,
        titulo_municipio,
        lista_municipio,
        titulo_coord,
        txt_latitud,
        txt_longitud
    )
if __name__== "__main__":
    ft.app(target=main)