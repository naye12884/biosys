#from pyairtable import Api
from pyairtable.orm import Model
from pyairtable.orm import fields

class Usuario(Model):
    clave = fields.TextField("clave")
    contra = fields.TextField("contra")
    nombre = fields.TextField("nombre")
    admin = fields.CheckboxField("admin")
    class Meta:
        api_key = "patlnsRXqmAyRoDhM.6c92b470bbefe1bed3cbeec75e472f9c4fef490ecb1b3b610df844b3ecb3161b"
        base_id = "appftrZqM2IrYHEFd"
        table_name = "usuario"

class Bioenergia(Model):
    cultivo = fields.TextField("cultivo")
    parte = fields.TextField("parte")
    cantidad = fields.FloatField("cantidad")
    area = fields.FloatField("area")
    energia = fields.FloatField("energia")
    municipio =fields.SelectField("municipio")
    latitud = fields.FloatField("latitud")
    longitud = fields.FloatField("longitud")

    class Meta:
        api_key = "patlnsRXqmAyRoDhM.6c92b470bbefe1bed3cbeec75e472f9c4fef490ecb1b3b610df844b3ecb3161b"
        base_id = "appftrZqM2IrYHEFd"
        table_name = "bioenergia"

#cacao = Bioenergia(
#    cultivo="Cacao",
#    parte="Cascara",
#    cantidad=2.0,
#    area=3.0,
#    energia=18.0,
#    municipio="Cunduacán",
#    latitud=18.076169,
#    longitud=21.021114
#)
#cacao.save()
#api = Api("patlnsRXqmAyRoDhM.6c92b470bbefe1bed3cbeec75e472f9c4fef490ecb1b3b610df844b3ecb3161b")
#tabla = api.table("appftrZqM2IrYHEFd", "usuario")

#Altas
#yo = {'clave':'naye',
#'contra':'perla1',
#'nombre':'Nayeli Alvarado',
#'admin': 1
#}
#tabla.create(yo)
#registros =tabla.all()
#for r in registros:
#   print(r["fields"])